import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Adding item came from the post request
    print("Event::")
    print(event)
    print("Event::")

    body = json.loads(event['body'])
    item={}
    if('server_status' in body and 'server_score' in body and 'server_name' in body and 'server_ip' in body):
        item = {
            'server_status': { 'S': body['server_status'] },
            'server_score': { 'S': body['server_score'] },
            'server_name': { 'S': body['server_name'] },
            'server_ip': { 'S': body['server_ip'] }
        }
        client.put_item(TableName='table_assignment_hire',  Item=item)
        print('Item has been added to the table using post method')

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