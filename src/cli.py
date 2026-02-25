"""Antigravity CLI - project scaffolding and agent runner."""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import click

from src.template_files import get_template_root, IGNORE_PATTERNS, CLEANUP_AFTER_COPY


def _validate_name(ctx, param, value):
    """Validate project name contains only safe characters."""
    if not re.fullmatch(r"[a-zA-Z0-9._-]+", value):
        raise click.BadParameter(
            "Project name must contain only letters, numbers, '.', '_', or '-'."
        )
    return value


def _write_env(project_dir, provider, project_name):
    """Generate .env file from .env.example with provider defaults."""
    env_example = project_dir / ".env.example"
    env_file = project_dir / ".env"

    lines = []
    if env_example.exists():
        lines = env_example.read_text(encoding="utf-8").splitlines()

    lines.append(f"AGENT_NAME={project_name}")
    if provider == "openai":
        lines.append("OPENAI_BASE_URL=https://api.openai.com/v1")
        lines.append("OPENAI_MODEL=gpt-4o-mini")
        lines.append("# Set your OPENAI_API_KEY below")
        lines.append("OPENAI_API_KEY=")
    else:
        lines.append("GEMINI_MODEL_NAME=gemini-2.0-flash-exp")
        lines.append("# Set your GOOGLE_API_KEY below")
        lines.append("GOOGLE_API_KEY=")

    env_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_mission(project_dir, project_name):
    """Write a starter mission.md."""
    content = (
        f"# {project_name}\n\n"
        "## Objective\n"
        "Define your agent's mission here.\n\n"
        "## Success Criteria\n"
        "- [ ] Criterion 1\n"
        "- [ ] Criterion 2\n"
    )
    (project_dir / "mission.md").write_text(content, encoding="utf-8")


@click.group()
@click.version_option(version="0.1.0", prog_name="antigravity")
def main():
    """Antigravity - Zero-Config AI Agent Workspace."""
    pass


@main.command("init")
@click.argument("project_name", callback=_validate_name)
@click.option("--dest", default=".", help="Parent directory for the new project.")
@click.option(
    "--provider",
    type=click.Choice(["gemini", "openai"], case_sensitive=False),
    default="gemini",
    help="Default LLM provider.",
)
@click.option("--git", is_flag=True, help="Initialize a git repository.")
def init_command(project_name, dest, provider, git):
    """Create a new Antigravity agent project.

    PROJECT_NAME is the name of the directory to create.
    """
    template_root = get_template_root()
    dest_path = Path(dest).expanduser().resolve()
    dest_path.mkdir(parents=True, exist_ok=True)
    project_dir = dest_path / project_name

    if project_dir.exists():
        raise click.ClickException(f"Directory already exists: {project_dir}")

    click.echo(f"🚀 Creating project '{project_name}'...")
    shutil.copytree(template_root, project_dir, ignore=IGNORE_PATTERNS)

    # Remove packaging-only files from the new project
    for rel in CLEANUP_AFTER_COPY:
        target = project_dir / rel
        if target.exists():
            target.unlink()

    # Ensure workspace dirs exist
    (project_dir / "artifacts" / "logs").mkdir(parents=True, exist_ok=True)
    (project_dir / ".context").mkdir(parents=True, exist_ok=True)

    # Write config files
    _write_env(project_dir, provider, project_name)
    _write_mission(project_dir, project_name)

    # Git init
    if git:
        subprocess.run(
            ["git", "init"], cwd=project_dir,
            check=True, capture_output=True,
        )
        click.echo("   ✓ Git repository initialized")

    click.echo(f"   ✓ Project created at {project_dir}")
    click.echo()
    click.echo("Next steps:")
    click.echo(f"   cd {project_dir}")
    click.echo("   python3 -m venv venv && source venv/bin/activate")
    click.echo("   pip install -r requirements.txt")
    click.echo("   # Edit .env with your API key")
    click.echo("   python src/agent.py \"Your task here\"")


@main.command("run")
@click.argument("task")
def run_command(task):
    """Run the agent with a task (convenience wrapper)."""
    from src.agent import GeminiAgent

    agent = GeminiAgent()
    try:
        agent.run(task)
    finally:
        agent.shutdown()
