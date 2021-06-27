# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods
import os
import pytest
from account_foundations.lib.config import Config

@pytest.fixture
def _config_path():
    return os.path.abspath("account_foundations/config/all.yaml")

@pytest.fixture
def _load_config():
    return Config.load_config(os.path.abspath("account_foundations/config/all.yaml"))

def test_config_loader(_load_config):
    yaml_config = _load_config
    assert yaml_config is not None
    assert isinstance(yaml_config, dict)

def test_config_general_attributes(_load_config):
    yaml_config = _load_config
    assert "general" in yaml_config
    assert isinstance(yaml_config["general"], dict)
    assert "region" in yaml_config["general"]

def test_config_vpc_attributes(_load_config):
    yaml_config = _load_config
    assert "vpc" in yaml_config
    assert isinstance(yaml_config["vpc"], dict)
    assert "name" in yaml_config["vpc"]
