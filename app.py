#!/usr/bin/env python3
import os
from aws_cdk import core


from ssm_parameter_store.ssm_parameter_store import SsmParameterStoreStack

# try:
#     cdk_account = os.environ['CDK_AWS_ACCOUNT']
# except KeyError:
#     cdk_account = ''
#     print(
#         f'ENV CDK_AWS_ACCOUNT is not set, using default value: {cdk_account}')

app = core.App()
SsmParameterStoreStack(app, 'ssm-parameter-store',
                       env={
                           'account': "846580235911",
                           'region': 'us-east-1'
                       },
                       )

app.synth()
