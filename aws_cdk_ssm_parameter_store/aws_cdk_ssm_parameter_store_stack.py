from aws_cdk import (
    core,
    aws_ssm as _ssm,
)


class AwsCdkSsmParameterStoreStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, 
                 shared_subnet_1: str=None,
                 shared_subnet_2: str=None,
                 centos_ami_id: str=None,
                 ubuntu_ami_id: str=None,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        def add_ssm_string_parameter(id: str, string_value: str,
                                     parameter_type=None, description: str=None,
                                     parameter_name: str=None,) -> _ssm.StringParameter:
            ssm_string_parameter = _ssm.StringParameter(
                self, id,
                type=parameter_type,
                parameter_name=parameter_name,
                string_value=string_value,
                description=description,
            )

        add_ssm_string_parameter(
            "SharedSubnet1",
            parameter_name='shared_subnet_1_id',
            string_value=shared_subnet_1,
        )

        add_ssm_string_parameter(
            "UbuntuAmiId",
            parameter_name='ubuntu_16.04_ami_id',
            string_value=ubuntu_ami_id,
        )





