from aws_cdk import core as cdk
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from account_foundations.lib.vpc import VpcModule as VpcModule


class VpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
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
        vpc = VpcModule(self, "VpcModule", cidr="10.1.0.0/16", vpc_name="test-vpc-cdk", subnets=subnets)