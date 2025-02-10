from dotenv import load_dotenv

from {{cookiecutter.project_name_snakecase}}.src.core.entities.opencti.connector_config import (
    ConnectorConfig,
)
from {{cookiecutter.project_name_snakecase}}.src.core.entities.opencti.opencti_config import (
    OpenCTIConfig,
)
from {{cookiecutter.project_name_snakecase}}.src.core.entities.opencti.{{cookiecutter.project_name_snakecase}}_config import (
    {{cookiecutter.project_name}}Config,
)


class Config:

    def __init__(self):
        load_dotenv()
        self.opencti = OpenCTIConfig()
        self.connector = ConnectorConfig()
        self.{{cookiecutter.project_name_snakecase}} = {{cookiecutter.project_name}}Config()

        self.to_dict()

    def to_dict(self) -> dict:
        return {
            "opencti": OpenCTIConfig().to_dict(),
            "connector": ConnectorConfig().to_dict(),
            "{{cookiecutter.project_name_snakecase}}": {{cookiecutter.project_name}}Config().to_dict(),
        }
