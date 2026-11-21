"""P4 repo 解析測試。"""
from __future__ import annotations

import unittest

from collectors.repo_parse import (
    RepoCandidate,
    build_repo_sections,
    clean_readme,
    decode_readme_content,
    evaluate_repo_quality,
    extract_paper_urls,
    github_repo_full_name,
    is_collection_repo_name,
    parse_github_repo_json,
)


class RepoParseTests(unittest.TestCase):
    def test_parse_github_repo_json(self):
        data = {
            "full_name": "org/MaritimeAI",
            "html_url": "https://github.com/org/MaritimeAI",
            "description": "Autonomous vessel perception",
            "stargazers_count": 123,
            "forks_count": 10,
            "language": "Python",
            "license": {"spdx_id": "Apache-2.0"},
            "topics": ["maritime", "ai"],
            "updated_at": "2026-11-20T00:00:00Z",
            "created_at": "2026-01-01T00:00:00Z",
            "pushed_at": "2026-11-19T00:00:00Z",
            "homepage": "https://arxiv.org/abs/2601.01234",
            "default_branch": "main",
            "owner": {"login": "org"},
            "archived": False,
        }
        repo = parse_github_repo_json(data)
        self.assertIsNotNone(repo)
        assert repo is not None
        self.assertEqual(repo.full_name, "org/MaritimeAI")
        self.assertEqual(repo.stars, 123)
        self.assertEqual(repo.license_name, "Apache-2.0")
        self.assertIn("maritime", repo.topics)

    def test_decode_readme_content_base64(self):
        data = {"content": "SGVsbG8gQUk=", "encoding": "base64"}
        self.assertEqual(decode_readme_content(data), "Hello AI")

    def test_clean_readme_strips_code_and_images(self):
        raw = "# Title\n\n![img](x.png)\n\n```py\nprint('x')\n```\n\nSee [paper](https://arxiv.org/abs/2601.01234)."
        text = clean_readme(raw)
        self.assertIn("Title", text)
        self.assertNotIn("print('x')", text)
        self.assertIn("paper", text)
        self.assertIn("2601.01234", text)

    def test_extract_paper_urls(self):
        text = "arxiv: 2601.01234v2 and doi 10.1000/XYZ and https://doi.org/10.2000/abc"
        urls = extract_paper_urls(text)
        self.assertTrue(any("arxiv.org/abs/2601.01234" in u for u in urls))
        self.assertTrue(any("doi.org/10.1000/xyz" in u.lower() for u in urls))

    def test_build_repo_sections_fallback(self):
        cand = RepoCandidate(
            full_name="org/repo",
            html_url="https://github.com/org/repo",
            description="Medical AI segmentation toolkit",
            language="Python",
            topics=["medical", "segmentation"],
            readme_excerpt="## Overview\n\nThis project does medical segmentation.\n\n## Architecture\n\nPipeline: input -> model -> output",
            paper_urls=["https://arxiv.org/abs/2601.01234"],
        )
        sections = build_repo_sections(cand)
        self.assertIn("Medical AI", sections["what"])
        self.assertTrue(sections["tech"])
        self.assertIn("Pipeline", sections["architecture"])
        self.assertIn("2601.01234", sections["architecture"])

    def test_collection_repo_name_detection(self):
        self.assertTrue(is_collection_repo_name("owner/awesome-maritime-ai"))
        self.assertTrue(is_collection_repo_name("owner/AI-paper-list"))
        self.assertTrue(is_collection_repo_name("owner/llm-survey"))
        self.assertTrue(is_collection_repo_name("owner/awesome-toolkit"))  # awesome 前綴視為清單型
        self.assertFalse(is_collection_repo_name("owner/maritime-vessel-detection"))
        self.assertFalse(is_collection_repo_name("owner/vessel-tracker"))

    def test_github_repo_full_name(self):
        self.assertEqual(github_repo_full_name("https://github.com/org/repo/tree/main/src"), "org/repo")
        self.assertEqual(github_repo_full_name("https://github.com/org/repo.git"), "org/repo")
        self.assertEqual(github_repo_full_name("not a url"), "")

    def test_quality_collection_penalized(self):
        quality = evaluate_repo_quality(
            "owner/awesome-ai-papers",
            "A curated list of AI papers and resources",
            ["awesome", "papers"],
            "# Awesome AI Papers\n\nA collection of papers.",
            language="",
            stars=5000,
        )
        self.assertTrue(quality.collection)
        self.assertLessEqual(quality.score, 2)
        self.assertIn("collection", quality.flags)

    def test_quality_implementation_repo_scores_high(self):
        readme = """
        # Maritime Detector
        ## Installation
        pip install maritime-detector
        ## Quickstart
        python -m maritime_detector.infer --input image.jpg
        ## Architecture
        sensor -> model -> alert
        """ + ("Detailed implementation notes. " * 80)
        quality = evaluate_repo_quality(
            "org/maritime-detector",
            "Autonomous vessel detection with deep learning",
            ["pytorch", "computer-vision"],
            readme,
            language="Python",
            stars=350,
            paired=True,
        )
        self.assertFalse(quality.collection)
        self.assertGreaterEqual(quality.score, 6)
        self.assertIn("implementation_signals", quality.flags)


if __name__ == "__main__":
    unittest.main()
