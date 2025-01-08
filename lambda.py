import json
import boto3

ENDPOINT_NAME = "huggingface-pytorch-tgi-inference-2024-07-10-14-24-36-825"
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    body = event['body']

    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                  ContentType="application/json",
                                  Body=body,
                                  CustomAttributes="accept_eula=true")

    response_content = response['Body'].read().decode()
    result = json.loads(response_content)
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'origin',
            'Access-Control-Allow-Methods': 'POST'
        },
        'body': json.dumps(result[0]['generated_text'])
    }
