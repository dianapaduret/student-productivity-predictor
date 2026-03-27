from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(title="Student Productivity Predictor API")

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "productivity_model.pkl"

model = joblib.load(MODEL_PATH)


class StudentInput(BaseModel):
    sleep_hours: float
    phone_usage_hours: float
    study_hours_per_day: float


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: StudentInput):
    input_df = pd.DataFrame([{
        "sleep_hours": data.sleep_hours,
        "phone_usage_hours": data.phone_usage_hours,
        "study_hours_per_day": data.study_hours_per_day
    }])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_productivity": round(float(prediction), 2)
    }