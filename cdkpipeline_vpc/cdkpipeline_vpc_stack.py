from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import (
        aws_ec2 as ec2,
        core
        )


class CdkpipelineVpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        az_count=1
        subnet_config = []
        subnet_config.append(ec2.SubnetConfiguration(
            name='subnet-1',
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24,
            ))
        subnet_config.append(ec2.SubnetConfiguration(
            name='subnet-2',
            subnet_type=ec2.SubnetType.PRIVATE,
            cidr_mask=24,
            ))

        vpc = ec2.Vpc(self, "The_vpc",
                cidr="15.0.0.0/16",
                subnet_configuration=subnet_config,
                max_azs=az_count,
               )
