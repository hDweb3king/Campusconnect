import json
import boto3
import uuid
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('campus_connect_opportunities')


def lambda_handler(event, context):

    method = (
        event.get('requestContext', {}).get('http', {}).get('method')
        or event.get('httpMethod')
        or 'GET'
    )

    if method == 'POST':

        body = event.get('body')

        if isinstance(body, str):
            body = json.loads(body)

        opportunity = {
            'OpportunityId': str(uuid.uuid4()),
            'title': body.get('title', ''),
            'category': body.get('category', ''),
            'description': body.get('description', ''),
            'link': body.get('link', ''),
            'createdAt': datetime.now(timezone.utc).isoformat()
        }

        table.put_item(Item=opportunity)

        return {
            'statusCode': 201,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(opportunity)
        }

    response = table.scan()

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(response['Items'])
    }
