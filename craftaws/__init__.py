from aws_cdk import (
    core,
    aws_ec2,
)

class infrastructure(core.NestedStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = aws_ec2.Vpc(self, "craftwas-vpc",
            cidr="10.100.0.0/16",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    name='craftwas-vpc',
                    subnet_type=aws_ec2.SubnetType.ISOLATED,
                    cidr_mask=24
                )
            ]
        )

