"""Integration test. Runs against a deployed HTTP API, URL from env API_URL."""

import os

import requests


def test_api_returns_200_and_env_key():
    api_url = os.environ["API_URL"]
    response = requests.get(api_url, timeout=10)
    assert response.status_code == 999
    assert "env" in response.json()
