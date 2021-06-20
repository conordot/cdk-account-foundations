import pytest
import os
import json
from account_foundations.lib.config import Config

@pytest.fixture
def _config_path():
    return os.path.abspath("account_foundations/config/all.yaml")

@pytest.fixture
def load_config():
    return Config.load_config(os.path.abspath("account_foundations/config/all.yaml"))

def test_config_loader(_config_path):
    yaml_config = Config.load_config(_config_path)
    assert yaml_config is not None
    assert type(yaml_config) == dict

def test_config_general_attributes(load_config):
    yaml_config = load_config
    assert "general" in yaml_config
    assert type(yaml_config["general"]) == dict
    assert "region" in yaml_config["general"]

def test_config_vpc_attributes(load_config):
    yaml_config = load_config
    assert "vpc" in yaml_config
    assert type(yaml_config["vpc"]) == dict
    assert "name" in yaml_config["vpc"]