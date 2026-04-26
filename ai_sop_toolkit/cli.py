import shutil
from pathlib import Path

import click


@click.group()
def main():
    """AI 開發系統化 SOP 工具套件 (V1.3 - Agent Team 架構)"""


@main.command()
def init():
    """在當前目錄初始化 Agent Team 架構開發環境"""
    template_dir = Path(__file__).parent / "templates"
    current_dir = Path.cwd()

    click.echo("🚀 正在注入 Agent Team 開發小隊技能 (V1.3)...")

    mapping = {
        "cursorrules.tpl": ".cursorrules",
        "claude_md.tpl": "CLAUDE.md",
        "task_md.tpl": "TASK.md",
        "project_rules_tpl.md": "PROJECT_RULES.md",
        "agents_md.tpl": "AGENTS.md",
    }

    for tpl, target in mapping.items():
        source = template_dir / tpl
        dest = current_dir / target

        if dest.exists():
            if click.confirm(f"⚠️ {target} 已存在，是否覆蓋？", default=False):
                shutil.copy(source, dest)
                click.echo(f"✅ 已更新 {target}")
        else:
            shutil.copy(source, dest)
            click.echo(f"✅ 已建立 {target}")

    click.echo("\n🎉 初始化成功！")
    click.echo("💡 AI 現在會根據 AGENTS.md 自動切換職位（PM, Architect, Builder, Tester, Liaison）。")


if __name__ == "__main__":
    main()
