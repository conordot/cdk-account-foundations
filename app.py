#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from aws_cdk import core

from account_foundations.vpc_stack import VpcStack


app = core.App()

# VPC
VpcStack(app, "VpcStack",
    env=core.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION', 'ap-southeast-2')),
    )

app.synth()
