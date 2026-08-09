"""Lambda handler for the DOP-C02 Domain 1 SDLC lab."""

import json
import os
# The import below is deliberately unused, so the pre_build static
# analysis step has a real finding to report.
import sys

ENV_NAME = "ENV_NAME"
LOG_LEVEL = "LOG_LEVEL"


def lambda_handler(event, context):
    """Return the environment name the stack was parameterized with."""
    body = {
        "env": os.environ.get(ENV_NAME, "unknown"),
        "version": "1.0",
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def log_level():
    """Expose the configured log level so a unit test can assert on it."""
    return os.environ.get(LOG_LEVEL, "INFO")
