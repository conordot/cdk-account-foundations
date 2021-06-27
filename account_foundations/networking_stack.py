"""Provisions Networking components in an AWS account via CDK stack
using CDK constructs."""
from aws_cdk import core as cdk
from account_foundations.lib.networking import NetworkingModule
# from account_foundations.lib.logger import Logger

# LOGGER = Logger()


class NetworkingStack(cdk.Stack):
    """Used for all networking components within an AWS account."""

    def __init__(self, scope: cdk.Construct, construct_id: str, *,
        env, subnets, vpc_name, cidr) -> None:
        print(env)
        super().__init__(scope, construct_id)
        NetworkingModule(self,
            "NetworkingModule",
            cidr=cidr,
            vpc_name=vpc_name,
            subnets=subnets
        )
