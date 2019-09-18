from urllib import parse
import os, json
import boto3
from botocore.vendored import requests
from crhelper import CfnResource
import logging

#Intiate Logger
logger = logging.getLogger(__name__)

# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL')


#Define Netskope Vars
try:
	apiOp = "create"
	nsToken = os.environ['nsToken']
	nsURL = "https://" + os.environ['nsDomain'] + "/api/v1/introspection_instance?token=" + nsToken + "&op=" + apiOp
	pass
except Exception as e:
	helper.init_failure(e)


@helper.create
def create(event, context):
	logger.info("Got Create")

	#Call Netskope Tenant for Create Instance
	nsResponse= requests.post(nsURL, json={'app': 'aws', 
									'instance_name': event['instanceName'], 
									'role_arn': 'arn:aws:iam::534321463187:role/stack-NetskopeIAMRole-QKIJPLB9A3SG',
									'trail_name': 'stack-NetskopeCloudTrail-18JX9IEXI0L4T',
									'trail_region': 'us-east-1',
									'admin_email': 'sbrown@netskope.com',
									'use_for': ['introspection', 'malware', 'securityscan'],
									'securityscan_interval': '30'})
	return "MyResourceId"

@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    # Delete never returns anything. Should not fail if the underlying resources are already deleted. Desired state.

def lambda_handler(event, context):
	helper(event, context)