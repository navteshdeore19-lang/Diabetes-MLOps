from fastapi import FastAPI
import joblib
import csv
from datetime import datetime 

app = FastAPI()

# Load the trained ML model
model = joblib.load("diabetes_model.pkl")


@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "loaded"
    }


@app.post("/predict")
def predict(data: dict):

    # Get patient data
    patient = [[
        data["Pregnancies"],
        data["Glucose"],
        data["BloodPressure"],
        data["SkinThickness"],
        data["Insulin"],
        data["BMI"],
        data["DiabetesPedigreeFunction"],
        data["Age"]
    ]]

    # Make prediction
    prediction = model.predict(patient)

    # Log prediction for monitoring
    with open("prediction_log.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            data["Glucose"],
            data["BMI"],
            data["Age"],
            int(prediction[0])
        ])

    # Return result
    if prediction[0] == 1:
        result = "Diabetes"
    else:
        result = "No Diabetes"

    return {
        "prediction": int(prediction[0]),
        "result": result
    }