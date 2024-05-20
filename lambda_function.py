import boto3
import zipfile
import os

# Set your AWS parameters
s3_bucket = 'traindata-pyxer1'  # Replace with your S3 bucket name
s3_key_appspec = 'appspec.yml'
s3_key_lambda = 'lambda_deployment.zip'
lambda_function_name = 'pyxer'  # Replace with your Lambda function name

# Upload appspec.yml to S3
s3 = boto3.client('s3')
s3.upload_file('appspec.yml', s3_bucket, s3_key_appspec)
print(f"Uploaded AppSpec file to s3://{s3_bucket}/{s3_key_appspec}")

# Create a zip file containing the Lambda function code and model artifacts
with zipfile.ZipFile('/tmp/lambda_deployment.zip', 'w') as zipf:
    zipf.write('lambda_function.py')
    zipf.write('model/model.joblib')
    zipf.write('model/label_encoder.joblib')
    zipf.write('appspec.yml')
    for root, dirs, files in os.walk('package'):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), 'package'))

# Upload Lambda function code to S3
s3.upload_file('/tmp/lambda_deployment.zip', s3_bucket, s3_key_lambda)
print(f"Uploaded Lambda deployment package to s3://{s3_bucket}/{s3_key_lambda}")

# Update Lambda function
lambda_client = boto3.client('lambda')
with open('/tmp/lambda_deployment.zip', 'rb') as f:
    lambda_client.update_function_code(
        FunctionName=lambda_function_name,
        ZipFile=f.read()
    )
print(f"Updated Lambda function: {lambda_function_name}")
