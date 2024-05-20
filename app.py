import boto3
import zipfile
import os
import subprocess
import shutil

# Set your AWS parameters
s3_bucket = 'traindata-pyxer1'  # Replace with your S3 bucket name
s3_key_lambda = 'lambda_deployment.zip'
lambda_function_name = 'pyxer'  # Replace with your Lambda function name

# Create a virtual environment
venv_dir = '/tmp/venv'
subprocess.check_call(['python3', '-m', 'venv', venv_dir])

# Install dependencies in the virtual environment
subprocess.check_call([f'{venv_dir}/bin/pip', 'install', '-r', 'requirements.txt', '-t', './python'])

# Create a zip file containing the Lambda function code, model artifacts, and dependencies
with zipfile.ZipFile('/tmp/lambda_deployment.zip', 'w') as zipf:
    zipf.write('lambda_function.py')
    zipf.write('appspec.yml')
    zipf.write('model/model.joblib')
    zipf.write('model/label_encoder.joblib')
    for root, dirs, files in os.walk('python'):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), 'python'))

# Upload Lambda function code to S3
s3 = boto3.client('s3')
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

# Cleanup
shutil.rmtree('python')
shutil.rmtree(venv_dir)
