"""Tests for the antigravity CLI."""

import os
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from src.cli import main, init_command


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def tmp_dest(tmp_path):
    """Provide a clean temporary destination directory."""
    return tmp_path / "dest"


class TestInitCommand:
    """Tests for the init subcommand."""

    def test_init_creates_project_directory(self, runner, tmp_dest):
        result = runner.invoke(init_command, [
            "test-project",
            "--dest", str(tmp_dest),
        ])
        assert result.exit_code == 0
        project_dir = tmp_dest / "test-project"
        assert project_dir.is_dir()
        assert (project_dir / "src").is_dir()
        assert (project_dir / "requirements.txt").exists()

    def test_init_refuses_existing_directory(self, runner, tmp_dest):
        project_dir = tmp_dest / "test-project"
        project_dir.mkdir(parents=True)
        result = runner.invoke(init_command, [
            "test-project",
            "--dest", str(tmp_dest),
        ])
        assert result.exit_code != 0
        assert "already exists" in result.output.lower()

    def test_init_invalid_project_name(self, runner, tmp_dest):
        result = runner.invoke(init_command, [
            "bad name with spaces",
            "--dest", str(tmp_dest),
        ])
        assert result.exit_code != 0

    def test_init_creates_env_file(self, runner, tmp_dest):
        result = runner.invoke(init_command, [
            "test-project",
            "--dest", str(tmp_dest),
            "--provider", "openai",
        ])
        assert result.exit_code == 0
        env_file = tmp_dest / "test-project" / ".env"
        assert env_file.exists()
        content = env_file.read_text()
        assert "OPENAI" in content

    def test_init_with_git(self, runner, tmp_dest):
        result = runner.invoke(init_command, [
            "test-project",
            "--dest", str(tmp_dest),
            "--git",
        ])
        assert result.exit_code == 0
        assert (tmp_dest / "test-project" / ".git").is_dir()


class TestMainGroup:
    """Tests for the top-level CLI group."""

    def test_help(self, runner):
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "init" in result.output
