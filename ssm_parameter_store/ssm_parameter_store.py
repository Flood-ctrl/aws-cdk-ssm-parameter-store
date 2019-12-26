import json
from aws_cdk import (
    core,
    aws_ssm as _ssm,
)


class SsmParameterStoreStack(core.Stack):

    def __init__(self, scope: core.Stack, id: str,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        with open("ssm_parameters.json", 'rb') as f:
            ssm_parameters = json.load(f)

        for key, value in ssm_parameters.items():
            if 'lifecycle' in ssm_parameters and key != 'lifecycle':
                key = '/' + ssm_parameters['lifecycle'] + key

            _ssm.StringParameter(
                self, f'{key}',
                string_value=value,
                parameter_name=key
            )
