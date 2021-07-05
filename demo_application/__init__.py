from aws_cdk import (
    core,
)
import craftaws

class bmt_graviton2_aurora(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        infra = craftaws.infrastructure(self, 'Infra')

        craftaws.aurora(self, 'Aurora', bmt_vpc=infra.vpc)

