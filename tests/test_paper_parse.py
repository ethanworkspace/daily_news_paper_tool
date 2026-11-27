import unittest
from datetime import timezone

from collectors.paper_parse import (
    PaperCandidate,
    arxiv_id_from_text,
    canonical_venue,
    extract_github_urls,
    extract_text_from_html,
    extract_text_from_pdf,
    first_github_url,
    format_impact_factor,
    parse_arxiv_atom,
    parse_openalex_work,
    parse_pubmed_xml,
    parse_semantic_scholar_paper,
    venue_tier,
)

ARXIV_ATOM = b"""<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2601.01234v2</id>
    <updated>2026-11-10T10:00:00Z</updated>
    <published>2026-11-09T09:00:00Z</published>
    <title>  Test LLM Paper for Maritime AI  </title>
    <summary>We propose a large language model for vessel routing. https://github.com/owner/repo </summary>
    <arxiv:comment>Code: https://github.com/owner/repo</arxiv:comment>
    <arxiv:doi>10.1000/test.doi</arxiv:doi>
    <author><name>Alice Smith</name></author>
    <author><name>Bob Lee</name></author>
    <link href="http://arxiv.org/abs/2601.01234v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2601.01234v2" rel="related" type="application/pdf"/>
  </entry>
</feed>
"""

PUBMED_XML = b"""<?xml version="1.0"?>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation>
      <PMID>123456</PMID>
      <Article>
        <ArticleTitle>AI model for clinical diagnosis</ArticleTitle>
        <Journal>
          <Title>Journal of Medical AI</Title>
          <JournalIssue>
            <PubDate><Year>2026</Year><Month>Nov</Month><Day>01</Day></PubDate>
          </JournalIssue>
        </Journal>
        <Abstract>
          <AbstractText Label="BACKGROUND">Background text.</AbstractText>
          <AbstractText Label="RESULTS">Results text.</AbstractText>
        </Abstract>
        <AuthorList>
          <Author><ForeName>Ann</ForeName><LastName>Doe</LastName></Author>
        </AuthorList>
        <ELocationID EIdType="doi">10.2000/med.1</ELocationID>
      </Article>
    </MedlineCitation>
    <PubmedData>
      <ArticleIdList>
        <ArticleId IdType="pmc">PMC99999</ArticleId>
      </ArticleIdList>
    </PubmedData>
  </PubmedArticle>
</PubmedArticleSet>
"""


class TestExtractors(unittest.TestCase):
    def test_extract_text_from_html(self):
        html = "<html><body><h1>Title</h1><script>x()</script><p>Hello <b>world</b>.</p><nav>menu</nav></body></html>"
        text = extract_text_from_html(html)
        self.assertIn("Title", text)
        self.assertIn("Hello world", text)
        self.assertNotIn("x()", text)
        self.assertNotIn("menu", text)

    def test_github_urls(self):
        text = "code at https://github.com/Org/Repo and https://github.com/org/repo.git"
        urls = extract_github_urls(text)
        self.assertEqual(urls, ["https://github.com/Org/Repo"])
        self.assertEqual(first_github_url("none"), "")
        self.assertEqual(extract_github_urls("https://github.com/topics/ai"), [])

    def test_arxiv_doi_helpers(self):
        self.assertEqual(arxiv_id_from_text("https://arxiv.org/abs/2601.01234v3"), "2601.01234")
        self.assertEqual(arxiv_id_from_text("arxiv:2601.01234"), "2601.01234")

    def test_canonical_venue_marks_preprints(self):
        self.assertEqual(canonical_venue("arXiv", "arXiv preprint", "https://arxiv.org/abs/2601.01234"), "arXiv preprint")
        self.assertEqual(canonical_venue("", "", "https://www.biorxiv.org/content/10.1101/x"), "bioRxiv preprint")
        self.assertEqual(
            canonical_venue("Nature Machine Intelligence", "Nature Machine Intelligence", "https://doi.org/10.1/x"),
            "Nature Machine Intelligence",
        )

    def test_semantic_scholar_preprint_vs_journal(self):
        preprint = parse_semantic_scholar_paper(
            {
                "title": "A preprint",
                "venue": "arXiv",
                "externalIds": {"ArXiv": "2601.01234"},
                "year": 2026,
            }
        )
        self.assertIsNotNone(preprint)
        assert preprint is not None
        self.assertEqual(preprint.source_tier, 5)
        self.assertIn("preprint", preprint.impact_factor.lower())

        journal = parse_semantic_scholar_paper(
            {
                "title": "A journal paper",
                "venue": "Nature Machine Intelligence",
                "journal": {"name": "Nature Machine Intelligence"},
                "externalIds": {"ArXiv": "2601.01234"},
                "year": 2026,
            }
        )
        self.assertIsNotNone(journal)
        assert journal is not None
        self.assertEqual(journal.source_tier, 1)
        self.assertEqual(journal.impact_factor, "N/A")

    def test_extract_text_from_pdf(self):
        # 以 mock PdfReader 測試萃取邏輯，不依賴 pypdf 內部寫入 API
        import collectors.pdf_text as pdf_text

        class FakePage:
            def __init__(self, text):
                self._text = text

            def extract_text(self, extraction_mode=None):
                return self._text

        class FakeReader:
            def __init__(self, _buf):
                self.pages = [FakePage(f"Page {i} content about maritime AI model.") for i in range(1, 46)]

        old = pdf_text.PdfReader
        try:
            pdf_text.PdfReader = FakeReader
            text = extract_text_from_pdf(b"%PDF-1.4 fake", ocr=False)
            self.assertIn("Page 1 content", text)
            self.assertIn("Page 45 content", text)  # 不限頁數
            self.assertIn("[Page 45]", text)
        finally:
            pdf_text.PdfReader = old

    def test_extract_text_from_pdf_empty(self):
        self.assertEqual(extract_text_from_pdf(b""), "")


class TestImpactFactor(unittest.TestCase):
    def test_formats_openalex_stats(self):
        text, source = format_impact_factor({"2yr_mean_citedness": 21.44, "h_index": 1981, "i10_index": 125324}, "Nature")
        self.assertIn("2yr_mean_citedness=21.44", text)
        self.assertIn("h_index=1981", text)
        self.assertIn("(OpenAlex)", text)
        self.assertIn("Nature", source)

    def test_na(self):
        self.assertEqual(format_impact_factor({}, ""), ("N/A", ""))
        self.assertEqual(format_impact_factor(None, ""), ("N/A", ""))

    def test_venue_tier(self):
        self.assertEqual(venue_tier(journal="Nature Medicine"), 1)
        self.assertEqual(venue_tier(journal="IEEE TPAMI"), 1)
        self.assertEqual(venue_tier(journal="JMLR"), 1)
        self.assertEqual(venue_tier(journal="NeurIPS"), 2)
        self.assertEqual(venue_tier(journal="Ocean Engineering"), 3)
        self.assertEqual(venue_tier(journal="PLOS ONE"), 4)
        self.assertEqual(venue_tier(journal="arXiv"), 5)
        # 避免被泛稱誤判為頂刊
        self.assertNotEqual(venue_tier(journal="Measurement Science and Technology"), 1)
        self.assertNotEqual(venue_tier(journal="Applied Sciences"), 1)
        self.assertEqual(venue_tier(journal="Science Advances"), 4)
        self.assertEqual(venue_tier(journal="Neural Networks"), 4)
        self.assertEqual(venue_tier(journal="JMIR Nursing"), 4)


class TestParseArxiv(unittest.TestCase):
    def test_parses_entry(self):
        papers = parse_arxiv_atom(ARXIV_ATOM)
        self.assertEqual(len(papers), 1)
        p = papers[0]
        self.assertIn("Maritime AI", p.title)
        self.assertEqual(p.arxiv_id, "2601.01234")
        self.assertEqual(p.doi, "10.1000/test.doi")
        self.assertEqual(p.code_url, "https://github.com/owner/repo")
        self.assertTrue(p.pdf_url.endswith(".pdf"))
        self.assertEqual(p.source_tier, 5)
        self.assertIn("preprint", p.impact_factor.lower())
        self.assertIsNotNone(p.published_at)


class TestParseOpenAlex(unittest.TestCase):
    def test_maps_work(self):
        work = {
            "id": "https://openalex.org/W1",
            "title": "Medical LLM Study",
            "publication_date": "2026-11-10",
            "doi": "https://doi.org/10.1234/abc",
            "cited_by_count": 7,
            "authorships": [{"author": {"display_name": "Jane Doe"}}],
            "abstract_inverted_index": {"Large": [0], "language": [1], "model": [2]},
            "primary_location": {
                "landing_page_url": "https://example.org/paper",
                "pdf_url": "https://example.org/paper.pdf",
                "source": {
                    "id": "https://openalex.org/S1",
                    "display_name": "Nature Medicine",
                    "type": "journal",
                    "summary_stats": {"2yr_mean_citedness": 50.1, "h_index": 400, "i10_index": 5000},
                },
            },
            "best_oa_location": {"landing_page_url": "https://example.org/paper", "pdf_url": "https://example.org/paper.pdf"},
            "open_access": {"oa_url": "https://example.org/paper"},
            "locations": [],
        }
        p = parse_openalex_work(work)
        self.assertIsNotNone(p)
        self.assertEqual(p.doi, "10.1234/abc")
        self.assertEqual(p.cited_by_count, 7)
        self.assertIn("Large language model", p.abstract)
        self.assertIn("2yr_mean_citedness=50.10", p.impact_factor)
        self.assertEqual(p.source_tier, 1)  # nature
        self.assertEqual(p.authors, ["Jane Doe"])

    def test_published_journal_with_arxiv_keeps_tier(self):
        work = {
            "id": "https://openalex.org/W2",
            "title": "Published LLM",
            "publication_date": "2026-11-10",
            "doi": "https://doi.org/10.1234/xyz",
            "cited_by_count": 1,
            "authorships": [],
            "abstract_inverted_index": {"AI": [0]},
            "primary_location": {
                "landing_page_url": "https://doi.org/10.1234/xyz",
                "source": {
                    "id": "https://openalex.org/S2",
                    "display_name": "JMLR",
                    "type": "journal",
                    "summary_stats": {"2yr_mean_citedness": 8.0, "h_index": 100, "i10_index": 200},
                },
            },
            "best_oa_location": {"landing_page_url": "https://doi.org/10.1234/xyz"},
            "open_access": {"oa_url": "https://doi.org/10.1234/xyz"},
            "locations": [{"landing_page_url": "https://arxiv.org/abs/2601.00001"}],
            "ids": {"arxiv": "https://arxiv.org/abs/2601.00001"},
        }
        p = parse_openalex_work(work)
        self.assertIsNotNone(p)
        self.assertEqual(p.arxiv_id, "2601.00001")
        self.assertEqual(p.source_tier, 1)  # JMLR 為頂級期刊，不被 arXiv 連結降級
        self.assertIn("2yr_mean_citedness", p.impact_factor)


class TestParseSemanticScholar(unittest.TestCase):
    def test_maps_paper(self):
        paper = {
            "title": "Embodied AI",
            "year": 2026,
            "publicationDate": "2026-11-05",
            "venue": "ICLR",
            "citationCount": 3,
            "externalIds": {"DOI": "10.9/x", "ArXiv": None},
            "openAccessPdf": {"url": "https://openreview.net/pdf?id=1"},
            "url": "https://www.semanticscholar.org/paper/1",
            "abstract": "A robot foundation model.",
            "authors": [{"name": "A"}, {"name": "B"}],
            "journal": {"name": "ICLR"},
        }
        p = parse_semantic_scholar_paper(paper)
        self.assertIsNotNone(p)
        self.assertEqual(p.doi, "10.9/x")
        self.assertEqual(p.cited_by_count, 3)
        self.assertEqual(p.authors, ["A", "B"])
        self.assertEqual(p.parse_level, "abstract")


class TestParsePubmed(unittest.TestCase):
    def test_parses_xml(self):
        papers = parse_pubmed_xml(PUBMED_XML)
        self.assertEqual(len(papers), 1)
        p = papers[0]
        self.assertEqual(p.doi, "10.2000/med.1")
        self.assertIn("BACKGROUND", p.abstract)
        self.assertIn("PMC99999", p.pdf_url)
        self.assertEqual(p.authors, ["Ann Doe"])
        self.assertIsNotNone(p.published_at)


if __name__ == "__main__":
    unittest.main()
