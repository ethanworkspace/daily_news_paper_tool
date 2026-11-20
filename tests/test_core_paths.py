import tempfile
import unittest
from datetime import date
from pathlib import Path

from core.paths import (
    PathSafetyError,
    atomic_write_text,
    day_dir,
    digest_path,
    ensure_day_tree,
    expected_output_names,
    news_path,
    paper_path,
    project_root,
    repo_path,
    safe_join,
    slugify,
    tech_path,
    week_folder,
)


class TestWeekAndPaths(unittest.TestCase):
    def test_week_folder_monday_to_sunday(self):
        self.assertEqual(week_folder(date(2026, 9, 14)), "1")  # 週一
        self.assertEqual(week_folder(date(2026, 9, 20)), "7")  # 週日
        self.assertEqual(week_folder(date(2026, 11, 21)), "6")  # 週六

    def test_day_and_file_paths(self):
        root = Path("root")
        self.assertEqual(day_dir(root, date(2026, 9, 14)), root / "1" / "2026-09-14")
        self.assertEqual(news_path(root, date(2026, 9, 14)).name, "01_新聞_10篇.md")
        self.assertEqual(tech_path(root, date(2026, 9, 14)).name, "04_AI技術架構_深度拆解.md")
        self.assertEqual(
            digest_path(root, date(2026, 9, 14)).as_posix(),
            "root/每日匯報/2026-09-14_每日匯報.md",
        )

    def test_paper_and_repo_paths_use_two_digit_index_and_slug(self):
        paper = paper_path(Path("r"), date(2026, 9, 14), 3, "A/B: Test Paper")
        self.assertEqual(paper.parent.as_posix(), "r/1/2026-09-14")
        self.assertRegex(paper.name, r"^02_論文_03_.+\.md$")
        self.assertNotIn("/", paper.name)
        self.assertNotIn(":", paper.name)
        repo = repo_path(Path("r"), date(2026, 9, 14), 1, "owner/repo")
        self.assertRegex(repo.name, r"^03_專案_01_owner-repo\.md$")

    def test_invalid_index(self):
        with self.assertRaises(ValueError):
            paper_path(Path("r"), date(2026, 9, 14), 0, "x")

    def test_expected_output_names(self):
        names = expected_output_names()
        self.assertEqual(len(names), 13)

    def test_project_root_exists(self):
        self.assertTrue(project_root().is_dir())


class TestSlugify(unittest.TestCase):
    def test_removes_windows_illegal_chars(self):
        slug = slugify('a<b>c:d"e/f\\g|h?i*j')
        for char in '<>:"/\\|?*':
            self.assertNotIn(char, slug)
        self.assertTrue(slug)

    def test_collapses_whitespace_and_separators(self):
        self.assertEqual(slugify("  hello   world  "), "hello-world")

    def test_preserves_cjk(self):
        self.assertEqual(slugify("海事 AI 醫療應用"), "海事-AI-醫療應用")

    def test_reserved_name(self):
        self.assertEqual(slugify("CON"), "CON_file")

    def test_empty_fallback(self):
        self.assertEqual(slugify("   ", fallback="item"), "item")

    def test_truncates(self):
        self.assertLessEqual(len(slugify("x" * 100, 20)), 20)


class TestSafeJoinAndWrite(unittest.TestCase):
    def test_safe_nested_join(self):
        with tempfile.TemporaryDirectory() as tmp:
            joined = safe_join(tmp, "1", "2026-09-14", "a.md")
            self.assertTrue(str(joined).startswith(str(Path(tmp).resolve())))

    def test_blocks_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(PathSafetyError):
                safe_join(tmp, "..", "evil.txt")
            with self.assertRaises(PathSafetyError):
                safe_join(tmp, str(Path(tmp).resolve().parent / "evil"))
            with self.assertRaises(PathSafetyError):
                safe_join(tmp, "C:evil")

    def test_atomic_write_leaves_no_temp(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sub" / "file.md"
            atomic_write_text(target, "內容\n")
            self.assertEqual(target.read_text(encoding="utf-8"), "內容\n")
            self.assertEqual([p.name for p in target.parent.iterdir()], ["file.md"])

    def test_ensure_day_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = ensure_day_tree(tmp, date(2026, 9, 14))
            self.assertTrue(paths["day"].is_dir())
            self.assertTrue(paths["assets"].is_dir())
            self.assertTrue(paths["digest"].is_dir())


if __name__ == "__main__":
    unittest.main()
