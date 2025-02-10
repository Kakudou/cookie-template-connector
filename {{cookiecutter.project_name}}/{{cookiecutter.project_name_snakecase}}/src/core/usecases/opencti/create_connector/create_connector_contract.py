from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from {{cookiecutter.project_name_snakecase}}.src.application.connector import Connector


@dataclass
class CreateConnectorContract:
    error: str | None = None
    connector: "Connector" = None
