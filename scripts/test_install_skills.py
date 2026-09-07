"""Installer integration tests; all destinations are isolated temporary folders."""
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("installer", Path(__file__).with_name("install_skills.py"))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="agent-toolkit-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.dest = self.root / "profile with spaces" / "skills"

    def install(self):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(self.dest)

    def test_complete_copy_and_idempotent_rerun(self):
        self.install()
        skills = list(installer.SOURCE.iterdir())
        mtimes = {p: p.stat().st_mtime_ns for p in self.dest.rglob("*") if p.is_file()}
        self.install()
        for source in skills:
            self.assertEqual(installer.manifest(source), installer.manifest(self.dest / source.name))
        self.assertEqual(mtimes, {p: p.stat().st_mtime_ns for p in mtimes})

    def test_collision_preflight_preserves_customizations(self):
        target = self.dest / "software-design-document"
        target.mkdir(parents=True)
        custom = target / "SKILL.md"
        custom.write_text("custom skill", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "exists and differs"):
            self.install()
        self.assertEqual(custom.read_text(), "custom skill")
        self.assertFalse((self.dest / "requirements-engineer").exists())

    def test_extra_files_are_a_conflict(self):
        self.install()
        extra = self.dest / "requirements-engineer" / "local-notes.md"
        extra.write_text("keep me", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "exists and differs"):
            self.install()
        self.assertEqual(extra.read_text(), "keep me")

    def test_failed_copy_exposes_no_partial_skills(self):
        copytree = installer.shutil.copytree

        def fail_second(source, target, *args, **kwargs):
            if Path(source).name == "software-design-document":
                raise OSError("simulated copy failure")
            return copytree(source, target, *args, **kwargs)

        with patch.object(installer.shutil, "copytree", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "simulated copy failure"):
                self.install()
        self.assertEqual(list(self.dest.iterdir()), [])
        self.assertEqual(list(self.dest.parent.glob("agent-toolkit-install-*")), [])

    def test_source_overlap_rejected(self):
        for destination in (installer.SOURCE, installer.SOURCE.parent, installer.SOURCE / "nested"):
            with self.assertRaisesRegex(ValueError, "overlap"):
                installer.install(destination)

    def test_missing_entrypoint_rejected_before_writes(self):
        source = self.root / "source"
        (source / "broken-skill").mkdir(parents=True)
        with patch.object(installer, "SOURCE", source):
            with self.assertRaisesRegex(ValueError, "Missing entrypoint"):
                self.install()
        self.assertFalse(self.dest.exists())

    def test_codex_home_and_fallback(self):
        with patch.dict(os.environ, {"CODEX_HOME": str(self.root / "custom codex")}):
            self.assertEqual(installer.default_destination(), self.root / "custom codex" / "skills")
        with patch.dict(os.environ, {"CODEX_HOME": ""}):
            self.assertEqual(installer.default_destination(), Path.home() / ".codex" / "skills")

    def test_cli_error_is_nonzero(self):
        with contextlib.redirect_stderr(io.StringIO()) as error:
            result = installer.main(["--dest", str(installer.SOURCE)])
        self.assertEqual(result, 1)
        self.assertIn("overlap", error.getvalue())


if __name__ == "__main__":
    unittest.main()
