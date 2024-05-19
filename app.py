import boto3
import zipfile
import os

# Set your AWS parameters
s3_bucket = 'traindata-pyxer1'
s3_key_model = 'model/model.joblib'
s3_key_encoder = 'model/label_encoder.joblib'
lambda_function_name = 'pyxer'

# Upload model and label encoder to S3
s3 = boto3.client('s3')
s3.upload_file('model.joblib', s3_bucket, s3_key_model)
s3.upload_file('label_encoder.joblib', s3_bucket, s3_key_encoder)
print(f"Uploaded model to s3://{s3_bucket}/{s3_key_model}")
print(f"Uploaded label encoder to s3://{s3_bucket}/{s3_key_encoder}")

# Update Lambda function
lambda_client = boto3.client('lambda')

# Create a zip file containing the model and label encoder
with zipfile.ZipFile('/tmp/lambda_deployment.zip', 'w') as zipf:
    zipf.write('model.joblib')
    zipf.write('label_encoder.joblib')

# Update the Lambda function code
with open('/tmp/lambda_deployment.zip', 'rb') as f:
    lambda_client.update_function_code(
        FunctionName=lambda_function_name,
        ZipFile=f.read()
    )
print(f"Updated Lambda function: {lambda_function_name}")
