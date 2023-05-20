import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    items = client.scan(TableName='table_assignment_hire')
    # Adding responseBody as a tuple (score, item) so that sorting can be carried out using score.
    responseBody=[]
    for item in items['Items']:
        server_status = item['server_status']['S']
        if server_status == 'inactive':
            responseBody.append(item)


    if len(responseBody) != 0:
        sns_topic_arn = "arn:aws:sns:eu-north-1:459756656750:hire_test_topic"
        message = "Servers which are in alarm: \n {}".format(responseBody)
        subject = "Servers in ALARM!!"
        send_sns(message, subject, sns_topic_arn)

    return {'statusCode': 200}



def send_sns(message, subject, sns_topic_arn):
    try:
        client = boto3.client("sns")
        result = client.publish(TopicArn=sns_topic_arn, Message=message, Subject=subject)
        if result['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(result)
            print("Notification send successfully..!!!")
            return True
    except Exception as e:
        print("Error occured while publish notifications and error is : ", e)
        return True
