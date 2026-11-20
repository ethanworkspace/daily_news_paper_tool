import tempfile
import unittest
from pathlib import Path

from core.logging_utils import reset_logger, setup_logger


class TestLoggingRedaction(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.log_dir = Path(self.tmp.name)
        self.logger = setup_logger("test_logger", log_dir=self.log_dir, console=False)
        self.log_file = self.log_dir / "run.log"

    def tearDown(self):
        reset_logger("test_logger")
        self.tmp.cleanup()

    def test_writes_to_file(self):
        self.logger.info("hello %s", "world")
        content = self.log_file.read_text(encoding="utf-8")
        self.assertIn("hello world", content)

    def test_redacts_secret_in_message(self):
        secret = "sk-" + "Q7" * 12
        self.logger.info("using key %s", secret)
        content = self.log_file.read_text(encoding="utf-8")
        self.assertNotIn(secret, content)
        self.assertIn("****", content)

    def test_redacts_secret_in_exception(self):
        secret = "sk-" + "W3" * 12
        try:
            raise ValueError(f"token={secret}")
        except ValueError:
            self.logger.exception("failed")
        content = self.log_file.read_text(encoding="utf-8")
        self.assertNotIn(secret, content)
        self.assertIn("ValueError", content)

    def test_setup_is_idempotent(self):
        setup_logger("test_logger", log_dir=self.log_dir, console=False)
        self.assertEqual(len(self.logger.handlers), 1)


if __name__ == "__main__":
    unittest.main()
