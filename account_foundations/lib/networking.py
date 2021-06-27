"""Sets up networking components in the target AWS account via the
    NetworkingModule CDK construct."""
from aws_cdk import (
    core,
    aws_ec2 as ec2
)

class NetworkingModule(core.Construct):
    """CDK construct to set up networking components in the target AWS account.
    Generic implementation that uses YAML config."""
    def __init__(self, scope: core.Construct, construct_id: str, *,
        cidr: str, vpc_name: str, subnets: list):
        super().__init__(scope, construct_id)
        self._setup_vpc(cidr, vpc_name, subnets)

    def _setup_vpc(self, cidr, vpc_name, subnets):
        subnet_conf = []
        for subnet in subnets:
            if subnet["type"] == "public":
                subnet_type = ec2.SubnetType.PUBLIC
            elif subnet["type"] == "restricted":
                subnet_type = ec2.SubnetType.ISOLATED
            else:
                subnet_type = ec2.SubnetType.PRIVATE
            subnet_conf.append(
                {
                   "cidrMask": subnet['cidr'] ,
                   "name": subnet['name'],
                   "subnetType": subnet_type
                }
            )
        self.vpc = ec2.Vpc(self, vpc_name,
            cidr=cidr,
            subnet_configuration=subnet_conf,
            enable_dns_hostnames=False,
            nat_gateways=None,
            vpn_gateway=False,
            max_azs=1
        )
