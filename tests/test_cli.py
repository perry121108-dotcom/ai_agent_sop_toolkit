from pathlib import Path

from click.testing import CliRunner

from ai_sop_toolkit.cli import main


def test_init_creates_template_files():
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(main, ["init"])

        assert result.exit_code == 0
        assert Path(".cursorrules").exists()
        assert Path("CLAUDE.md").exists()
        assert Path("TASK.md").exists()
        assert Path("PROJECT_RULES.md").exists()
        assert Path("AGENTS.md").exists()


def test_init_keeps_existing_file_when_overwrite_is_declined():
    runner = CliRunner()

    with runner.isolated_filesystem():
        target = Path("TASK.md")
        target.write_text("custom task file", encoding="utf-8")

        result = runner.invoke(main, ["init"], input="n\n")

        assert result.exit_code == 0
        assert target.read_text(encoding="utf-8") == "custom task file"
