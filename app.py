#!/usr/bin/env python3
import os
from aws_cdk import core


from ssm_parameter_store.ssm_parameter_store import SsmParameterStoreStack

try:
    cdk_account = os.environ['CDK_AWS_ACCOUNT']
except KeyError:
    cdk_account = ''
    print(
        f'ENV CDK_AWS_ACCOUNT is not set, using default value: {cdk_account}')

app = core.App()
SsmParameterStoreStack(app, 'ssm-parameter-store',
                       description='Stack for creating parameters in SMM Parameter store',
                       lifecycle='lifecycle',
                       ssm_parameters_file='ssm_parameters.json',
                       ssm_parameters_dir='ssm_parameters',
                       env={
                           'account': cdk_account,
                           'region': 'us-east-1'
                       },
                       )

app.synth()
