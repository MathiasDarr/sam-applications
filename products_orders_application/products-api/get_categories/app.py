"""
The lambda function defined here queries the category GSI

"""
import json
import boto3


dynamo_resource = boto3.resource('dynamodb') #, endpoint_url='http://localhost:8000')
TABLE_NAME = 'Categories'
categories_table = dynamo_resource.Table(TABLE_NAME)


def scan_categories():
    scan_results = categories_table.scan()
    return scan_results['Items']

scan_categories()


def lambda_handler(event, context):
    """

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    categories = scan_categories()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "categories": categories,
        }),
    }
