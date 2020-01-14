# Netskope AWS Cloudformation Template - All Features


This CloudFormation Template will build a stack that enables all the requirements for the Netskope Security Assessment/Storage Scanning Features and configures them in a Netskope Tenant.


#### Before running the template you will need to collect information from the Netskope Tenant. Specifically you will need the tenant hostname (<tenantname>.goskope.com) and the REST API token.

###### Parameters required to run the template
* AWS Account Name
* Admin Email
* Netskope API Token
* Netskope Tenant Hostname

#### To launch the CFT click the link below or upload the yaml file in the nsAwsAutoDeployCFT folder

<a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=Netskope-AWS-CF&templateURL=https://netskope-autodeploy-us-east-1.s3.amazonaws.com/All_Features/nsAwsAutoDeploy.yaml"><img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/></a>
