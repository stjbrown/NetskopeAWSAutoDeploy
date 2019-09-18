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

@helper.create
def create(event, context):
	logger.info("Got Create")

	#Set Vars from CFT Request
	nsDomain = event['ResourceProperties']['nsDomain']
	nsToken = event['ResourceProperties']['nsToken']

	#SET NETSKOPE URL
	nsURL = "https://" + nsDomain + "/api/v1/introspection_instance?token=" + nsToken + "&op=get_aws_role_prep_info"

	nsResponse= requests.post(nsURL, json={'use_for': ['introspection', 'malware', 'securityscan']})
	nsAccountId= nsResponse.json()['data']['account_id']
	nsExternalId= nsResponse.json()['data']['external_id']
	nsPermissions= nsResponse.json()['data']['permissions'][0] 
	
	helper.Data.update({"nsAccountId": nsAccountId })
	helper.Data.update({"nsExternalId": nsExternalId }) 
	helper.Data.update({"nsPermissions": nsPermissions })
	return "MyResourceId"

@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    # Delete never returns anything. Should not fail if the underlying resources are already deleted. Desired state.

def lambda_handler(event, context):
	helper(event, context)