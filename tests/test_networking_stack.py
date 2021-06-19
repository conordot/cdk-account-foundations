import pytest
import os
import json
# from aws_cdk import core as cdk
from aws_cdk import core
from account_foundations.networking_stack import NetworkingStack


def test_networking_stack():
    app = core.App()
    subnets = [
            {
                "name": "public-cdk",
                "cidr": 24,
                "type": "public"
            },
            {
                "name": "private-cdk",
                "cidr": 24,
                "type": "private"
            }
        ]
    networking_stack = NetworkingStack(app, "NetworkingModule", env="test", subnets=subnets, vpc_name="test-vpc-cdk", cidr="10.1.0.0/16")
    app.synth()
    template_path = f'{app.outdir}/{networking_stack.template_file}'
    with open(template_path, 'r') as template_file:
        template_object = json.load(template_file)
        print(template_object)
    assert False == True
    # check_function(template_object)
    # check_log_group(template_object)
    # check_p5_alarm(template_object)
    # check_p3_alarm(template_object)

def check_private_subnet():
    """ """

def check_public_subnet():
    """ """