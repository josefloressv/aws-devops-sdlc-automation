"""Unit tests. Two always pass; the third is the FORCE_FAIL toggle."""

import json
import os

from app import handler


def test_handler_returns_200():
    result = handler.lambda_handler({}, None)
    assert result["statusCode"] == 200


def test_handler_body_contains_env_key():
    result = handler.lambda_handler({}, None)
    body = json.loads(result["body"])
    assert "env" in body
    assert body["version"] == "1.0"


def test_force_fail_toggle():
    """Set FORCE_FAIL=1 in the CodeBuild project to turn this test red."""
    assert os.environ.get("FORCE_FAIL") != "1"
