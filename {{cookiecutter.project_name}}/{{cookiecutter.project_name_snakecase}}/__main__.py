"""Entry point for the {{cookiecutter.project_name_snakecase}} package."""

from os import environ as os_environ
from sys import exit
from unittest.mock import patch
from uuid import uuid4

from {{cookiecutter.project_name_snakecase}}.src.application.connector import Connector


def dev_env() -> dict[str, str]:
    """Development environment variables used for testing through mock patching."""
    return {
        "OPENCTI_URL": "http://localhost:8080",
        "OPENCTI_TOKEN": f"{os_environ.get('OCTI_TOKEN')}",
        "CONNECTOR_ID": f"{uuid4()}",
        "CONNECTOR_TYPE": "EXTERNAL_IMPORT",
        "CONNECTOR_NAME": "{{cookiecutter.project_name}}",
        "CONNECTOR_SCOPE": "all",
        "CONNECTOR_DURATION_PERIOD": "PT1M",
        "CONNECTOR_LOG_LEVEL": "debug",
    }


def connector() -> int:
    """Entry point for the {{cookiecutter.project_name_snakecase}} package."""
    env_vars = dev_env() if os_environ.get("OCTI_DEV") == "DEV" else os_environ

    dev_patch = patch.dict(os_environ, env_vars)
    dev_patch.start()

    connector = Connector()

    connector.start()

    dev_patch.stop()
    return 0


if __name__ == "__main__":
    exit(connector())
