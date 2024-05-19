import json
import joblib
import boto3
import os

s3 = boto3.client('s3')
s3_bucket = 'traindata-pyxer1'
s3_key_model = 'model/model.joblib'
s3_key_encoder = 'model/label_encoder.joblib'
model_path = '/tmp/model.joblib'
encoder_path = '/tmp/label_encoder.joblib'

def lambda_handler(event, context):
    # Download model and label encoder from S3
    s3.download_file(s3_bucket, s3_key_model, model_path)
    s3.download_file(s3_bucket, s3_key_encoder, encoder_path)
    
    model = joblib.load(model_path)
    label_encoder = joblib.load(encoder_path)
    
    

    # Parse input data
    input_data = json.loads(event['body'])['data']

    # Predict
    prediction = model.predict([input_data])
    prediction_label = label_encoder.inverse_transform(prediction)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'prediction': prediction_label.tolist()
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
