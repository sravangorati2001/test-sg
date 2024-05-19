import json
import joblib
import boto3
import os

s3 = boto3.client('s3')
s3_bucket = 'traindata-pyxer1'
s3_key = 'model/model.joblib'
model_path = '/tmp/model.joblib'

def lambda_handler(event, context):
    # Download model from S3
    s3.download_file(s3_bucket, s3_key, model_path)
    model = joblib.load(model_path)

    # Example input
    input_data = event['data']

    # Predict
    prediction = model.predict([input_data])
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'prediction': prediction.tolist()
        })
    }
