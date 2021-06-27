# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods
from yaml import load, FullLoader


class Config:
    """Quick config loader for YAML config to allow users to override specific config"""

    @staticmethod
    def load_config(path):
        config_content = ""
        with open(path, "r") as file_handler:
            config_content = file_handler.read()

        config_yaml = load(config_content, Loader=FullLoader)
        return config_yaml
