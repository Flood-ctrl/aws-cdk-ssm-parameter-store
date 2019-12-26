import os
import json
from aws_cdk import (
    core,
    aws_ssm as _ssm,
)


class SsmParameterStoreStack(core.Stack):

    def __init__(self, scope: core.Stack, id: str,
                 ssm_parameters_file: str = 'ssm_parameters.json',
                 ssm_parameters_dir: str = 'ssm_parameters',
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        for filename in os.listdir(ssm_parameters_dir):
            with open(os.path.join(ssm_parameters_dir, filename), 'rb') as f:
                ssm_parameters = json.load(f)

            for key, value in ssm_parameters.items():
                if 'lifecycle' in ssm_parameters and key != 'lifecycle':
                    key = '/' + ssm_parameters['lifecycle'] + key

                if key == 'lifecycle':
                    continue

                _ssm.StringParameter(
                    self, f'{key}',
                    string_value=value,
                    parameter_name=key
                )
