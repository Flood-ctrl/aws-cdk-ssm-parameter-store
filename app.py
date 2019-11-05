#!/usr/bin/env python3

from aws_cdk import core

from ssm_parameter_store.ssm_parameter_store import SsmParameterStoreStack


app = core.App()
SsmParameterStoreStack(app, "ssm-parameter-store",
                                 env={
                                      'region': 'us-east-1'
                                  },
                                  ssm_parameters={
                                      'shared_subnet_id': 'some_subnet_id',
                                      'shared_subnet_id_2': 'some_subnet_id_2',

                                  }
                                )

app.synth()
