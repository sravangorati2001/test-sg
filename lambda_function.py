import json
import pickle
import pandas as pd

def lambda_handler(event, context):
    # Load the model
    with open('/tmp/model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Process the input data (assuming it's passed in the event)
    input_data = pd.DataFrame(event['data'])
    
    # Make predictions
    predictions = model.predict(input_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps(predictions.tolist())
    }
