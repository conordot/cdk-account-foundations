from aws_cdk import core as cdk
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from account_foundations.lib.networking import NetworkingModule as NetworkingModule


class NetworkingStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, *, env, subnets, vpc_name, cidr) -> None:
        super().__init__(scope, construct_id)
        vpc = NetworkingModule(self, "NetworkingModule", cidr=cidr, vpc_name=vpc_name, subnets=subnets)