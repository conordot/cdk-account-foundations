#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from aws_cdk import core

from account_foundations.networking_stack import NetworkingStack
from account_foundations.lib.config import Config

config_yaml = Config.load_config(os.path.abspath("account_foundations/config/all.yaml"))
print(config_yaml)

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
