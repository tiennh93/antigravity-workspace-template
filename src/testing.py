"""Shared testing utilities."""

from __future__ import annotations

import os
import sys


class DummyGenAIClient:
    """Lightweight stand-in for genai.Client in test environments.

    Returns canned responses to avoid external API calls in tests.
    """

    class _Models:
        def generate_content(self, model: str, contents: str):
            return DummyGenAIClient._Response()

    class _Response:
        text: str = "I have completed the task"

    def __init__(self):
        self.models = self._Models()


def is_test_environment() -> bool:
    """Check if running under pytest."""
    return "PYTEST_CURRENT_TEST" in os.environ or "pytest" in sys.modules
