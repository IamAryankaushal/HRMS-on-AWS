import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hrms-leave-requests')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        # GET leave requests
        if 'employeeId' in event['queryStringParameters']:
            employee_id = event['queryStringParameters']['employeeId']
            response = table.query(
                KeyConditionExpression='employeeId = :employeeId',
                ExpressionAttributeValues={
                    ':employeeId': employee_id
                }
            )
            return {
                'statusCode': 200,
                'body': json.dumps(response.get('Items', []))
            }
        else:
            response = table.scan()
            return {
                'statusCode': 200,
                'body': json.dumps(response.get('Items', []))
            }
            
    elif http_method == 'POST':
        # Create a new leave request
        body = json.loads(event['body'])
        request_id = str(uuid.uuid4())
        
        item = {
            'requestId': request_id,
            'employeeId': body.get('employeeId', ''),
            'startDate': body.get('startDate', ''),
            'endDate': body.get('endDate', ''),
            'leaveType': body.get('leaveType', ''),
            'reason': body.get('reason', ''),
            'status': 'Pending',
            'approverComments': ''
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Leave request created successfully', 'requestId': request_id})
        }
        
    elif http_method == 'PUT':
        # Update a leave request (approve/reject)
        body = json.loads(event['body'])
        request_id = event['pathParameters']['requestId']
        employee_id = event['pathParameters']['employeeId']
        
        table.update_item(
            Key={
                'requestId': request_id,
                'employeeId': employee_id
            },
            UpdateExpression="set #status = :status, approverComments = :comments",
            ExpressionAttributeNames={
                '#status': 'status'
            },
            ExpressionAttributeValues={
                ':status': body.get('status', 'Pending'),
                ':comments': body.get('approverComments', '')
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Leave request updated successfully'})
        }