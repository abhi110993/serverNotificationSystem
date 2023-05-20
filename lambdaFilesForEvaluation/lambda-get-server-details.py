import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    items = client.scan(TableName='table_assignment_hire')
    # Adding responseBody as a tuple (score, item) so that sorting can be carried out using score.
    responseBody=[]
    for item in items['Items']:
        responseBody.append((int(item['server_score']['S']),item))

    # Sorting in descending order
    responseBody.sort(reverse=True)

    #Preparing response body by retrieving item after removal of score we used for sorting,
    data = []
    for item in responseBody:
        data.append(item[1])
    response = {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
        }
    }

    return response