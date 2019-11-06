#!/usr/bin/env python3

from aws_cdk import core

from ssm_parameter_store.ssm_parameter_store import SsmParameterStoreStack


app = core.App()
SsmParameterStoreStack(app, "ssm-parameter-store",
                                 env={
                                      'region': 'us-east-1'
                                  },
                                  ssm_parameters={
                                      'Shared Security Group': 'sg-02dc8ab580036c627',
                                      'Shared_Services_VPC': 'vpc-00c32da90392ef045',
                                      'Shared_Services Services1 Subnet': 'subnet-075678082726036af',
                                      'Shared_Services Services2 Subnet ': 'subnet-08e1e07990c846c76',
                                      'Shared_Services WebTier1 Subnet': 'subnet-0239ab1050c926743',
                                      'Shared_Services WebTier2 Subnet': 'subnet-09e747db29f47da05',

                                  }
                                )

app.synth()
