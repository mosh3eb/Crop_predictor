from collections import defaultdict

import pandas as pd
from data import cropRecommendation  # Import data from data.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import models  # Import models from models.py
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI()

# Allow CORS from any origin
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input data model
class CropInfo(BaseModel):
    nitrogen: int
    phosphorus: int
    potassium: int
    temperature: int
    humidity: int
    ph: int
    rainfall: int

# Prediction endpoint with point system
@app.post("/predict")
async def predict_crop(crop_info: CropInfo):
    # Extract the input values from the user
    input_data = [
        [
            crop_info.nitrogen,
            crop_info.phosphorus,
            crop_info.potassium,
            crop_info.temperature,
            crop_info.humidity,
            crop_info.ph,
            crop_info.rainfall,
        ]
    ]

    # Convert input data to DataFrame for prediction
    df_input = pd.DataFrame(
        input_data,
        columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    )

    # Initialize the points system
    points = defaultdict(int)

    # Make predictions from each model
    decision_tree_prediction = models["decision_tree"].predict(df_input)[0]
    logistic_regression_prediction = models["logistic_regression"].predict(df_input)[0]
    nb_classifier_prediction = models["nb_classifier"].predict(df_input)[0]
    random_forest_prediction = models["random_forest"].predict(df_input)[0]

    # Assign points based on the model's accuracy weight
    points[decision_tree_prediction] += 1  # 1 point for Decision Tree
    points[logistic_regression_prediction] += 2  # 2 points for Logistic Regression
    points[nb_classifier_prediction] += 3  # 3 points for MBC Classifier
    points[random_forest_prediction] += 3  # 3 points for Random Forest

    # Find the crop with the maximum points
    final_crop = max(points, key=points.get)

    # Return the result
    return {"predicted_crop": final_crop}