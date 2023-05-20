## Server Status Notification System

This is a machine coding round I recieved from XXX company.

### Problem Statement:
Task: To create a server monitoring system using AWS Lambda, DynamoDB, Eventbridge, SNS, Cloudwatch Alarms and API Gateway.

### STEPS:

1. Upload /cloudFormationFile/iamRole.json to cloud formation AWS using upload template method and give it some name such as: 'server-ns-iam-role' and wait for it to deploy properly.
2. Upload /cloudFormationFile/lambdas.json to cloud formation AWS using upload template method and give it some name such as: 'server-ns-lambdas' and wait for it to deploy properly.
3. Upload /cloudFormationFile/dynamodb.json to cloud formation AWS using upload template method and give it some name such as: 'server-ns-dynamodb' and wait for it to deploy properly.
4. 