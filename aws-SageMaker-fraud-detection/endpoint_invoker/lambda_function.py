import boto3
import json
from time import gmtime, strftime
import time
import datetime
  
client = boto3.client('runtime.sagemaker')
sns = boto3.client('sns')
  
ENDPOINT_NAME = <SECRET>
  
def lambda_handler(event, context):
    # TODO implement
    # print(event['body'])
    # print(type(event['body']))
    # list(event['body'])
    target = json.loads(event['body'])
    result = client.invoke_endpoint(EndpointName=ENDPOINT_NAME,Body=json.dumps(target))
    response = json.loads(result['Body'].read())
  
    print(response)
    fraud_rate = response['result']['classifications'][0]['classes'][1]['score']
    fraud = float(fraud_rate)*100
  
    if fraud>=90:
        now = datetime.datetime.now()
        tdelta = datetime.timedelta(hours=8)
        mytime = now + tdelta
  
        mail_response = sns.publish(
        TopicArn=<SECRET>,
        Message='Hey, Do you remember this transaction?' + '\n' + mytime.strftime("%Y-%m-%d %H:%M:%S") + '\n Please check your credit card account \n it might be a fraud transaction',
        Subject='Transaction Alert')
  
    http_response = {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers':{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        }
    }
    return http_response
