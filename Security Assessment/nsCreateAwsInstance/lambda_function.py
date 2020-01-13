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

	#Set Netskope URL
	nsURL = "https://" + nsDomain + "/api/v1/introspection_instance?token=" + nsToken + "&op=create"

	#Call Netskope Tenant for Create Instance
	nsResponse= requests.post(nsURL, json={'app': 'aws', 
									'instance_name': event['ResourceProperties']['instanceName'], 
									'role_arn': event['ResourceProperties']['roleArn'],
									'admin_email': event['ResourceProperties']['adminEmail'],
									'use_for': event['ResourceProperties']['useFor'],
									'securityscan_interval': event['ResourceProperties']['interval']})
	logger.info(nsResponse.json())
	if nsResponse.json()['status'] != "success":
		helper.init_failure(nsResponse.json())
	return "MyResourceId"

@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    # Delete never returns anything. Should not fail if the underlying resources are already deleted. Desired state.

def lambda_handler(event, context):
	helper(event, context)