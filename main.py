import pickle
from collections import defaultdict

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Load the CSV data
cropRecommendation = pd.read_csv("crop_recommendation.csv")

# Load multiple models
decision_tree_model = pickle.load(open("DecisionTree.pkl", "rb"))
logistic_regression_model = pickle.load(open("LogisticRegression.pkl", "rb"))
nb_classifier_model = pickle.load(open("NBClassifier.pkl", "rb"))
random_forest_model = pickle.load(open("RandomForest.pkl", "rb"))

# Define the input data model
class CropInfo(BaseModel):
    nitrogen: int
    phosphorus: int
    potassium: int
    temperature: int
    humidity: int
    ph: int
    rainfall: int

# Root endpoint to check the server status
@app.get("/")
def read_root():
    return {"message": "Backend is running"}

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
    decision_tree_prediction = decision_tree_model.predict(df_input)[0]
    logistic_regression_prediction = logistic_regression_model.predict(df_input)[0]
    nb_classifier_prediction = nb_classifier_model.predict(df_input)[0]
    random_forest_prediction = random_forest_model.predict(df_input)[0]

    # Assign points based on the model's accuracy weight
    points[decision_tree_prediction] += 1  # 1 point for Decision Tree
    points[logistic_regression_prediction] += 2  # 2 points for Logistic Regression
    points[nb_classifier_prediction] += 3  # 3 points for MBC Classifier
    points[random_forest_prediction] += 3  # 3 points for Random Forest

    # Find the crop with the maximum points
    final_crop = max(points, key=points.get)

    # Return the result
    return {"predicted_crop": final_crop}

