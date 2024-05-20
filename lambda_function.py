import json
import pickle
import boto3

def lambda_handler(event, context):
    # Download the model from S3 to /tmp/model.pkl
    s3 = boto3.client('s3')
    s3_bucket = 'traindata-pyxer1'
    s3_key = 'model.pkl'
    s3.download_file(s3_bucket, s3_key, '/tmp/model.pkl')
    
    # Load the model
    with open('/tmp/model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Process the input data (assuming it's passed in the event)
    input_data = event['data']
    
    # Make predictions
    predictions = model.predict(input_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps(predictions.tolist())
    }
