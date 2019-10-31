#!/usr/bin/env python3

import os
from aws_cdk import core
from aws_cdk_ssm_parameter_store.aws_cdk_ssm_parameter_store_stack import AwsCdkSsmParameterStoreStack


app = core.App()
AwsCdkSsmParameterStoreStack(app, "ssm-parameter-store",
                             env={
                                   'account': os.environ['CDK_ACCOUNT'],
                                   'region': 'us-east-1'
                             },
                             shared_subnet_1='subnet-0b0d12a344cd55cce',
                             shared_subnet_2='subnet-0b0d12a344cd55cce',
                             centos_ami_id='ami-0b898040803850657',
                             ubuntu_ami_id='ami-01d9d5f6cecc31f85',

                            )

app.synth()
