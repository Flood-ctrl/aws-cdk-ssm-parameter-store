from aws_cdk import (
    core,
    aws_ssm as _ssm,
)


class SsmParameterStoreStack(core.Stack):

    def __init__(self, scope: core.Stack, id: str,
                ssm_parameters: dict,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        for parameter_name,string_value in ssm_parameters.items():

            ssm_parameter_store = _ssm.StringParameter(
                self, f'{parameter_name}',
                string_value=string_value,
                parameter_name=parameter_name,
            )