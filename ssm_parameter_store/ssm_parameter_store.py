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
                 lifecycle: str = 'lifecycle',
                 ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        """Adds arameters to SSM parameter store from json files.

        :param ssm_parameters_file: Json file with parameters. (Depricated)
        :param ssm_parameters_dir: Directory with json files contain parameters.
        :param lifecycle: The name (value) of the prefix for adding to key. 
                          It will not be added if ${lifecycle} key and value are abesnt in the json file.
                          For instance if lifecycle = 'lifecycle', then for adding prefix to key,
                          in the json file it has be "lifecycle": "dev1".
                          Elif lifecycle = 'environment', then in the json file it has be "environment": "dev1".
        """

        for filename in os.listdir(ssm_parameters_dir):
            if filename.endswith('.json'):
                with open(os.path.join(ssm_parameters_dir, filename), 'rb') as f:
                    ssm_parameters = json.load(f)

                for key, value in ssm_parameters.items():
                    if lifecycle in ssm_parameters and key != lifecycle:
                        key = '/' + ssm_parameters[lifecycle] + key

                    if key == lifecycle:
                        continue

                    _ssm.StringParameter(
                        self, f'{key}',
                        string_value=value,
                        parameter_name=key
                    )
