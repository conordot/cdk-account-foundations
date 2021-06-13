from aws_cdk import core as cdk
from aws_cdk import core
from lib.vpc import Vpc


class CdkEncVpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = Vpc(cidr="10.8.0.0/16")
        vpc.add_subnet(az="ap-southeast-2", cidr="10.8.0.0/24", subnet_id="public-a")
        vpc.add_subnet(az="ap-southeast-2", cidr="10.9.0.0/24", subnet_id="private-a")
        print(vpc.subnets)
        