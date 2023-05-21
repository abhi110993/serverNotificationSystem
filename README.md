## Server Status Notification System

This is a machine coding round I recieved from XXX company.

### Problem Statement:
Task: To create a server monitoring system using AWS Lambda, DynamoDB, Eventbridge, SNS, Cloudwatch Alarms and API Gateway.

### STEPS:

1. Upload /cloudFormationFile/iamRole.json to cloud formation AWS using upload template method and give it some name such as: 'server-ns-iam-role' and wait for it to deploy properly.
2. Upload /cloudFormationFile/lambdas.json to cloud formation AWS using upload template method and give it some name such as: 'server-ns-lambdas' and wait for it to deploy properly.
3. Upload /cloudFormationFile/dynamodb.json to cloud formation AWS using upload template method and give it some name such as: 'server-ns-dynamodb' and wait for it to deploy properly.
4. Upload /cloudFormationFile/apigateway.json to cloud formation AWS using upload template method and give it some name such as: 'server-ns-apigateway' and wait for it to deploy properly.

### Resource for which cloud formation is not created:
1. Create SNS topic with name 'hire_test_topic'.
2. Create Event bridge which calls lambda function: 'lambda-server-notify-server-status'
   1. Add configuration to execute it for every 5 mins.

### Assumptions:
1. Servers are updating the dynamodb table 'dynamo_table_server_status'
2. The Lambda 'lambda-server-notify-server-status' running every 5 mins checking the status of server
   1. If the server is inactive then it sends the mail else it doesn't

### Testing (This will not work after 30th May):
1. The service is currently running fine on my personal AWS account ID.
2. GET Request:
   1. URL: https://yh3bkoar04.execute-api.us-east-1.amazonaws.com/prod/gateway_resource_hire
      1. Add x-api-key : vFrPzkiRzh83XsYOe7T3I6WduEXoajto9id6oppn
      2. It will show the result in decreasing order of their 'server_score'
3. POST Request:
   1. URL: https://yh3bkoar04.execute-api.us-east-1.amazonaws.com/dev/gateway_resource_hire
   2. Add x-api-key : vFrPzkiRzh83XsYOe7T3I6WduEXoajto9id6oppn
   3. Give a body to it like:
   ```
   {
         "server_status": "active",
         "server_score": "35",
         "server_name": "us-east-1",
         "server_ip": "172.1.1.16"
   }
   ```
   
   4. This will either add/update the server configuration and report the latest status of all the server status

### Curl Commands for testing

1. GET Request:
```
   curl --location 'https://yh3bkoar04.execute-api.us-east-1.amazonaws.com/prod/gateway_resource_hire'
```
OUTPUT:
```
{
    "statusCode": 200,
    "body": "[{\"server_status\": {\"S\": \"active\"}, \"server_score\": {\"S\": \"35\"}, \"server_name\": {\"S\": \"us-east-1\"}, \"server_ip\": {\"S\": \"172.1.1.16\"}}, {\"server_status\": {\"S\": \"inactive\"}, \"server_score\": {\"S\": \"30\"}, \"server_name\": {\"S\": \"us-west-2\"}, \"server_ip\": {\"S\": \"172.1.1.15\"}}, {\"server_status\": {\"S\": \"active\"}, \"server_score\": {\"S\": \"20\"}, \"server_name\": {\"S\": \"us-west-1\"}, \"server_ip\": {\"S\": \"172.1.1.12\"}}]",
    "headers": {
        "Content-Type": "application/json"
    }
}

```
1. POST Request:
```
  curl --location 'https://yh3bkoar04.execute-api.us-east-1.amazonaws.com/dev/gateway_resource_hire' \
--header 'x-api-key: vFrPzkiRzh83XsYOe7T3I6WduEXoajto9id6oppn' \
--header 'Content-Type: text/plain' \
--data '{
    "server_status": "active",
    "server_score": "35",
    "server_name": "us-east-1",
    "server_ip": "172.1.1.16"
}'
```
OUTPUT:
```
[
    {
        "server_status": {
            "S": "active"
        },
        "server_score": {
            "S": "35"
        },
        "server_name": {
            "S": "us-east-1"
        },
        "server_ip": {
            "S": "172.1.1.16"
        }
    },
    {
        "server_status": {
            "S": "inactive"
        },
        "server_score": {
            "S": "30"
        },
        "server_name": {
            "S": "us-west-2"
        },
        "server_ip": {
            "S": "172.1.1.15"
        }
    },
    {
        "server_status": {
            "S": "active"
        },
        "server_score": {
            "S": "20"
        },
        "server_name": {
            "S": "us-west-1"
        },
        "server_ip": {
            "S": "172.1.1.12"
        }
    }
]

```
