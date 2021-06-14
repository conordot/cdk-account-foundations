import aws_cdk.aws_ec2 as ec2

class Vpc:
    def __init__(self, *kwargs):
        self.setup_vpc(kwargs.cidr.get("cidr", "10.0.0.0/16"))
        self.subnets = []

    def setup_vpc(self, *kwargs):
        cidr = kwargs.get("cidr")
        self.vpc = ec2.Vpc(self, kwargs.vpc_name,
            cidr=cidr
        )

    def add_subnet(self, *kwargs):
        az = kwargs.get("az", "ap-southeast-a")
        cidr = kwargs.get("cidr", "10.0.0.0/16")
        subnet = ec2.Subnet(self, kwargs.subnet_id, az, cidr, self.vpc.vpc_id)
        self.subnets.append(subnet)