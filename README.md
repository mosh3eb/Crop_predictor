# Crop Prediction AI System

## Overview

The Crop Prediction AI System is a machine learning application designed to predict optimal crop yields based on various environmental and soil parameters. By leveraging multiple predictive models, including Decision Tree, Logistic Regression, Naive Bayes Classifier, and Random Forest, this system provides accurate recommendations for farmers and agricultural stakeholders.


![BEfore sending a Request](https://github.com/mosh3eb/Crop_predictor/blob/main/Examples/Ex1.png)


![After getting a Response](https://github.com/mosh3eb/Crop_predictor/blob/main/Examples/Ex2.png)


## Features

- **Multi-Model Prediction**: Utilizes various machine learning algorithms to enhance prediction accuracy.
- **User-Friendly API**: Built using FastAPI, allowing easy integration and interaction with the prediction system.
- **CORS Support**: Configured to allow requests from any origin, facilitating cross-origin resource sharing.

## Technologies Used

- **Python**: The primary programming language used for development.
- **FastAPI**: A modern web framework for building APIs with Python.
- **Pandas**: A data manipulation library used for handling input data.
- **Machine Learning Libraries**: Includes popular libraries for model training and prediction.

## Installation

1. Clone the repository:
 
   ```bash
   git clone https://github.com/mosh3eb/Crop_predictor.git
   cd Crop_predictor


3. Install the required dependencies:
 
   ```bash
   pip install -r requirements.txt

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload


2. Send a POST request to the /predict endpoint with the following JSON body:

   ```bash
   {
    "nitrogen": <value>,
    "phosphorus": <value>,
    "potassium": <value>,
    "temperature": <value>,
    "humidity": <value>,
    "ph": <value>,
    "rainfall": <value>
   }


3. The response will include the predicted crop:
 
   ```bash
   {
    "predicted_crop": "crop_name"
   }

## Contribution

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
