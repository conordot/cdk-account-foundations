#!/usr/bin/env python3
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods
import os
from aws_cdk import core

from account_foundations.networking_stack import NetworkingStack
from account_foundations.lib.config import Config

config_yaml = Config.load_config(os.path.abspath("account_foundations/config/all.yaml"))

app = core.App()

# Networking Construct
NetworkingStack(app, "NetworkingStack",
    env=core.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION', 'ap-southeast-2')),
    subnets=config_yaml.get('vpc', {}).get('subnets', []),
    vpc_name = config_yaml.get('vpc', {}).get('name', ""),
    cidr = config_yaml.get('vpc', {}).get('cidr', "")
)

app.synth()
