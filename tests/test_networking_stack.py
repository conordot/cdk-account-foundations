# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods,inconsistent-return-statements,redefined-outer-name
import json
import pytest
from aws_cdk import core
from account_foundations.networking_stack import NetworkingStack

@pytest.fixture
def setup_networking_stack():
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
    networking_stack = NetworkingStack(
        app,
        "NetworkingModule",
        env="test",
        subnets=subnets,
        vpc_name="test-vpc-cdk",
        cidr="10.1.0.0/16"
    )
    app.synth()
    template_path = f'{app.outdir}/{networking_stack.template_file}'
    with open(template_path, 'r') as template_file:
        template_object = json.load(template_file)
    return template_object

def test_vpc(setup_networking_stack):
    template = setup_networking_stack['Resources']
    vpc = _get_resource_by_prefix(template, "NetworkingModuletestvpccdk")
    assert vpc["Properties"]["CidrBlock"] == "10.1.0.0/16"

def test_private_subnet(setup_networking_stack):
    template = setup_networking_stack['Resources']
    private_subnet = _get_resource_by_prefix(template, "privatecdk")
    tags_to_check = [
        {
            "key": "aws-cdk:subnet-type",
            "expected_value": "Private"
        }
    ]
    _check_resource_tags(private_subnet, tags_to_check)

def test_public_subnet(setup_networking_stack):
    template = setup_networking_stack['Resources']
    public_subnet = _get_resource_by_prefix(template, "publiccdk")
    tags_to_check = [
        {
            "key": "aws-cdk:subnet-type",
            "expected_value": "Public"
        }
    ]
    _check_resource_tags(public_subnet, tags_to_check)

def _get_resource_by_prefix(content, prefix: str) -> dict:
    for key in content:
        if prefix in key:
            return content[key]
    return

def _check_resource_tags(subnet, tags_to_check):
    for tag in subnet['Properties']['Tags']:
        for tag_check in tags_to_check:
            if tag["Key"] == tag_check["key"]:
                assert tag["Value"] == tag_check["expected_value"]
