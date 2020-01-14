
# AWS CDK SSM Parameter Store (python)

Stack for creating SSM parameters from `json` files.
`json` files should be inside `ssm_parameters_dir`.
If `lifecycle` key and value are present it will add `lifecycle` prefix for all keys, for instace if we have `json` file with content:

	{
	    "lifecycle": "env1",
	    "/five/value": "5",
	    "/six/value": "6"
	}

it will create keys - **"/env1/five/value"**, **"/env1/five/value"** etc.
But "lifecycle" key will not be created in the SSM Parameter store.