"""Template file management for project scaffolding."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import List

# 项目根目录相对于此文件的位置
_PACKAGE_ROOT = Path(__file__).resolve().parent

# 从安装包中查找模板，回退到开发模式下的仓库根目录
_TEMPLATE_CANDIDATES = [
    _PACKAGE_ROOT / "template",          # pip install 后的打包路径
    _PACKAGE_ROOT.parent,                 # 开发模式下的仓库根目录
]

# 复制时排除的模式
IGNORE_PATTERNS = shutil.ignore_patterns(
    ".git",
    ".pytest_cache",
    "__pycache__",
    "venv",
    ".venv",
    "*.pyc",
    "*.egg-info",
    "dist",
    "build",
    "agent_memory.json",
    "artifacts",
    ".env",
)

# 复制后需要从目标中删除的路径（打包专用文件）
CLEANUP_AFTER_COPY: List[str] = [
    "pyproject.toml",
    "src/cli.py",
    "src/template_files.py",
]


def get_template_root() -> Path:
    """Locate the template root directory.

    Returns:
        Path to the template root.

    Raises:
        FileNotFoundError: If no template root is found.
    """
    for candidate in _TEMPLATE_CANDIDATES:
        # 验证至少包含 src/ 和 requirements.txt
        if (candidate / "src").is_dir() and (candidate / "requirements.txt").exists():
            return candidate
    raise FileNotFoundError(
        "Template root not found. Ensure the package is installed correctly."
    )
