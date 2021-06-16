from aws_cdk import (
    core,
    aws_ec2 as ec2
)

class VpcModule(core.Construct):
    def __init__(self, scope: core.Construct, id: str, *, cidr: str, vpc_name: str, subnets: list):
        super().__init__(scope, id)
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
            subnet_configuration=subnet_conf
        )