"""Canary target function. Bump VERSION to trigger a new deployment."""

import json

VERSION = "v3"


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"version": VERSION}),
    }
