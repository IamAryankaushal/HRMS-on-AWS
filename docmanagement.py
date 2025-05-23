import json
import boto3
import base64
import uuid

s3 = boto3.client('s3')
BUCKET_NAME = 'hrms-documents'

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        # GET document
        document_key = event['queryStringParameters']['key']
        
        try:
            response = s3.get_object(
                Bucket=BUCKET_NAME,
                Key=document_key
            )
            
            # Generate a presigned URL instead of returning the file directly
            presigned_url = s3.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': BUCKET_NAME,
                    'Key': document_key
                },
                ExpiresIn=3600  # URL expires in 1 hour
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps({'url': presigned_url})
            }
            
        except Exception as e:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': str(e)})
            }
            
    elif http_method == 'POST':
        # Upload document
        body = json.loads(event['body'])
        file_content = body.get('fileContent', '')  # Base64 encoded
        file_name = body.get('fileName', '')
        employee_id = body.get('employeeId', '')
        document_type = body.get('documentType', '')
        
        if not file_content or not file_name or not employee_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required parameters'})
            }
            
        try:
            # Decode base64 content
            decoded_content = base64.b64decode(file_content)
            
            # Generate a unique key for the document
            document_key = f"{employee_id}/{document_type}/{str(uuid.uuid4())}-{file_name}"
            
            # Upload to S3
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=document_key,
                Body=decoded_content
            )
            
            return {
                'statusCode': 201,
                'body': json.dumps({'message': 'Document uploaded successfully', 'key': document_key})
            }
            
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
            
    elif http_method == 'DELETE':
        # Delete document
        document_key = event['queryStringParameters']['key']
        
        try:
            s3.delete_object(
                Bucket=BUCKET_NAME,
                Key=document_key
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Document deleted successfully'})
            }
            
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }