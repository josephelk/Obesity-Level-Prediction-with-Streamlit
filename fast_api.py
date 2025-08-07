from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
import uvicorn
import pickle

# Load saved model
with open('best_obesity_classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load saved preprocessor
with open('data_preprocessor.pkl', 'rb') as preprocessor_file:
    preprocessor = pickle.load(preprocessor_file)

# Load saved label encoder
with open('label_encoder.pkl', 'rb') as encoder_file:
    label_encoder = pickle.load(encoder_file)


# FastAPI app
app = FastAPI(title="Obesity Prediction")

# Define input schema using Pydantic
class ObesityInput(BaseModel):
    Gender: str
    Age: float
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

@app.get("/")
def index():
    return {"message": "Hello, this is a backend to predict The Obesity Level!"}

@app.post("/predict")
def predict(input_data: ObesityInput):
    # Convert input to DataFrame
    data = pd.DataFrame([input_data.dict()])

    # Langsung prediksi pakai pipeline
    prediction = model.predict(data)

    predicted_label = label_encoder.inverse_transform(prediction)[0]

    return {
        "predicted_class": predicted_label,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)