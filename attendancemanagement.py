import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hrms-attendance')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        # GET attendance records
        employee_id = event['queryStringParameters']['employeeId']
        start_date = event['queryStringParameters'].get('startDate', None)
        end_date = event['queryStringParameters'].get('endDate', None)
        
        if start_date and end_date:
            response = table.query(
                KeyConditionExpression='employeeId = :employeeId AND #date BETWEEN :startDate AND :endDate',
                ExpressionAttributeNames={
                    '#date': 'date'
                },
                ExpressionAttributeValues={
                    ':employeeId': employee_id,
                    ':startDate': start_date,
                    ':endDate': end_date
                }
            )
        else:
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
            
    elif http_method == 'POST':
        # Create/update attendance record (check-in)
        body = json.loads(event['body'])
        employee_id = body.get('employeeId', '')
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')
        action = body.get('action', '')  # check-in or check-out
        
        if action == 'check-in':
            item = {
                'employeeId': employee_id,
                'date': date,
                'checkIn': time,
                'checkOut': '',
                'totalHours': 0,
                'status': 'Present'
            }
            
            table.put_item(Item=item)
            
        elif action == 'check-out':
            response = table.get_item(
                Key={
                    'employeeId': employee_id,
                    'date': date
                }
            )
            
            if 'Item' in response:
                check_in = response['Item'].get('checkIn', '')
                
                if check_in:
                    check_in_time = datetime.strptime(check_in, '%H:%M:%S')
                    check_out_time = datetime.strptime(time, '%H:%M:%S')
                    
                    total_hours = (check_out_time - check_in_time).total_seconds() / 3600
                    
                    table.update_item(
                        Key={
                            'employeeId': employee_id,
                            'date': date
                        },
                        UpdateExpression="set checkOut = :checkOut, totalHours = :totalHours",
                        ExpressionAttributeValues={
                            ':checkOut': time,
                            ':totalHours': round(total_hours, 2)
                        }
                    )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Attendance {action} recorded successfully'})
        }