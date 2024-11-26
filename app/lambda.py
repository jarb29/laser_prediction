import json
import pandas as pd
import logging
from pycaret.regression import load_model, predict_model

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the saved pipeline
logging.info("Loading the model.")
pipeline = load_model('/var/task/model/ilaser_pycaret_pipeline')


def lambda_handler(event, context):
    logging.info("Received event: %s", event)

    try:
        # Extract input features from the event
        longitude_corte = event['longitude_corte']
        espesor = event['espesor']

        logging.info("Extracted features - longitude_corte: %s, espesor: %s", longitude_corte, espesor)

        # Create input DataFrame
        input_data = {
            'Longitude Corte (m)': [longitude_corte],
            'Espesor': [espesor]
        }
        input_df = pd.DataFrame(input_data)

        logging.info("Created input DataFrame: %s", input_df)

        # Make prediction
        prediction = predict_model(pipeline, data=input_df)

        # Log the prediction DataFrame details
        logging.info("Prediction DataFrame columns: %s", str(prediction.columns.tolist()))  # Log columns as a string
        logging.info("Prediction DataFrame shape: %s", str(prediction.shape))  # Log shape
        logging.info("Prediction DataFrame content:\n%s", str(prediction))  # Log full content

        # Extract the prediction result
        total_machining = prediction.at[0, 'prediction_label']  # Modified to use .at accessor for robustness

        logging.info("Prediction result: %s", total_machining)

        # Create response
        response = {
            'statusCode': 200,
            'body': json.dumps({'total_machining': total_machining})
        }

        logging.info("Response: %s", response)
    except Exception as e:
        logging.error("Error during processing: %s", str(e))
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response