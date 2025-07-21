# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.classification import load_model, predict_model
import os

# Load model
model_path = os.path.join("models", "best_model")
model = load_model(model_path)

# Create app
app = FastAPI(title="Credit Risk Prediction API")

# Define input schema
class InputData(BaseModel):
    status: str
    duration: int
    credit_history: str
    purpose: str
    amount: int
    savings: str
    employment_duration: str
    installment_rate: int
    personal_status_sex: str
    other_debtors: str
    present_residence: int
    property: str
    age: int
    other_installment_plans: str
    housing: str
    number_credits: int
    job: str
    people_liable: int
    telephone: str
    foreign_worker: str

# Define predict route
@app.post("/predict")
def predict(data: InputData):
    # Convert input to dataframe
    input_df = pd.DataFrame([data.model_dump()])
    
    # Make prediction
    prediction_df = predict_model(model, data=input_df)
    
    # Get first prediction
    pred_value = int(prediction_df["prediction_label"].values[0])
    
    # Map numeric prediction to human-readable risk
    risk_label = "Good" if pred_value == 1 else "Bad"
    
    return {"prediction": pred_value, "risk": risk_label}   
