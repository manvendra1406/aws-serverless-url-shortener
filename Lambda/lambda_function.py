import json
import string
import random
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    method = event['httpMethod']

    if method == 'POST':
        body = json.loads(event['body'])
        long_url = body['url']

        short_id = generate_id()

        table.put_item(Item={
            'shortId': short_id,
            'longUrl': long_url
        })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'shortUrl': f"/{short_id}"
            })
        }

    if method == 'GET':
        short_id = event['pathParameters']['id']

        res = table.get_item(Key={'shortId': short_id})

        if 'Item' not in res:
            return {'statusCode': 404}

        return {
            'statusCode': 302,
            'headers': {
                'Location': res['Item']['longUrl']
            }
        }
