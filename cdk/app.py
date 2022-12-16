#!/usr/bin/env python3

import os

import aws_cdk as cdk
from stacks.cdk_cms_provider_datasets_lambda import CMSProviderDatasetsLambdaStack


DEPLOYMENT_ENVIRONMENT = "prod"
NAME_PREFIX = ""
MAIN_RESOURCES_NAME = "cms-provider-data-download"

print("CDK_DEFAULT_ACCOUNT", os.getenv("CDK_DEFAULT_ACCOUNT"))
print("CDK_DEFAULT_REGION", os.getenv("CDK_DEFAULT_REGION"))


app = cdk.App()
stack = CMSProviderDatasetsLambdaStack(
    app,
    "CMSProviderDatasetsLambdaStack",
    NAME_PREFIX,
    MAIN_RESOURCES_NAME,
    DEPLOYMENT_ENVIRONMENT,
    env={
        "account": os.getenv("CDK_DEFAULT_ACCOUNT"), 
        "region": os.getenv("CDK_DEFAULT_REGION"),
    },
    description="Stack for {} infrastructure in {} environment".format(MAIN_RESOURCES_NAME, DEPLOYMENT_ENVIRONMENT),
)

cdk.Tags.of(stack).add("Environment", DEPLOYMENT_ENVIRONMENT)
cdk.Tags.of(stack).add("MainResourceName", MAIN_RESOURCES_NAME)

app.synth()
