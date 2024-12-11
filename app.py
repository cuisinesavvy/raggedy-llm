from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import aiplatform
from typing import List
import os

# Initialize FastAPI
app = FastAPI()

# Configure Google Cloud project and endpoint
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
REGION = os.getenv("GOOGLE_CLOUD_REGION", "your-region")  # e.g., us-central1
ENDPOINT_ID = os.getenv("VERTEX_AI_ENDPOINT_ID", "your-endpoint-id")
MODEL_LOCATION = f"projects/{PROJECT_ID}/locations/{REGION}/endpoints/{ENDPOINT_ID}"

# Set up the request schema
class PredictionRequest(BaseModel):
    instances: List[dict]
    parameters: dict = {}

# Initialize Vertex AI client
def get_vertex_ai_client():
    return aiplatform.gapic.PredictionServiceClient()

# Health check route
@app.get("/")
def read_root():
    return {"message": "Vertex AI FastAPI Service is running!"}

# Prediction route
@app.post("/predict")
def predict(data: PredictionRequest):
    try:
        client = get_vertex_ai_client()

        # Prepare the request payload
        request = {
            "endpoint": MODEL_LOCATION,
            "instances": data.instances,
            "parameters": data.parameters,
        }

        # Make the prediction
        response = client.predict(request=request)

        # Parse the prediction results
        predictions = [dict(prediction) for prediction in response.predictions]
        return {"predictions": predictions}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))