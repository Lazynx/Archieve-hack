# src/aws/s3_service.py
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import logging
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

s3_client = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

async def upload_file(bucket_name: str, file: bytes, file_name: str):
    try:
        response = s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file
        )
        return f"https://{bucket_name}.s3.{AWS_REGION}.amazonaws.com/{file_name}"
    except NoCredentialsError:
        logging.error("Credentials not available")
        return None
    except ClientError as e:
        logging.error(e)
        return None

async def delete_file(bucket_name: str, file_name: str):
    try:
        response = s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        return True
    except ClientError as e:
        logging.error(e)
        return False
