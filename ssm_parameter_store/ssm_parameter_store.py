import json
from aws_cdk import (
    core,
    aws_ssm as _ssm,
)


class SsmParameterStoreStack(core.Stack):

    def __init__(self, scope: core.Stack, id: str,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # for parameter_name,string_value in ssm_parameters.items():

        #     ssm_parameter_store = _ssm.StringParameter(
        #         self, f'{parameter_name}',
        #         string_value=string_value,
        #         parameter_name=parameter_name,
        #     )

        
        with open("ssm_parameters.json", 'rb') as f:
            ssm_parameters = json.load(f)
        
        for key, value in ssm_parameters.items():
            if 'lifecycle' in ssm_parameters:
                key = '/' + ssm_parameters['lifecycle'] + key

            _ssm.StringParameter(
                self, 'SsmParameters',
                string_value=value,
                parameter_name=key

            )