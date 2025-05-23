import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hrms-employees')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        # GET all employees or a specific employee
        if 'employeeId' in event['queryStringParameters']:
            employee_id = event['queryStringParameters']['employeeId']
            response = table.get_item(Key={'employeeId': employee_id})
            return {
                'statusCode': 200,
                'body': json.dumps(response.get('Item', {}))
            }
        else:
            response = table.scan()
            return {
                'statusCode': 200,
                'body': json.dumps(response.get('Items', []))
            }
            
    elif http_method == 'POST':
        # Create a new employee
        body = json.loads(event['body'])
        employee_id = str(uuid.uuid4())
        
        item = {
            'employeeId': employee_id,
            'firstName': body.get('firstName', ''),
            'lastName': body.get('lastName', ''),
            'email': body.get('email', ''),
            'phone': body.get('phone', ''),
            'department': body.get('department', ''),
            'position': body.get('position', ''),
            'joinDate': body.get('joinDate', datetime.now().strftime('%Y-%m-%d')),
            'managerId': body.get('managerId', ''),
            'status': 'Active'
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Employee created successfully', 'employeeId': employee_id})
        }
        
    elif http_method == 'PUT':
        # Update an employee
        body = json.loads(event['body'])
        employee_id = event['pathParameters']['employeeId']
        
        update_expression = "set "
        expression_attribute_values = {}
        
        for key, value in body.items():
            if key != 'employeeId':
                update_expression += f"{key} = :{key}, "
                expression_attribute_values[f":{key}"] = value
        
        # Remove trailing comma and space
        update_expression = update_expression[:-2]
        
        table.update_item(
            Key={'employeeId': employee_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Employee updated successfully'})
        }
        
    elif http_method == 'DELETE':
        # Delete an employee (or set as inactive)
        employee_id = event['pathParameters']['employeeId']
        
        # Instead of deleting, set status to Inactive
        table.update_item(
            Key={'employeeId': employee_id},
            UpdateExpression="set #status = :status",
            ExpressionAttributeNames={
                '#status': 'status'
            },
            ExpressionAttributeValues={
                ':status': 'Inactive'
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Employee set to inactive'})
        }