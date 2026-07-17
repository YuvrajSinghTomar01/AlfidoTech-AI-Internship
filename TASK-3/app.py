from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("best_classification_model.pkl")
scaler = joblib.load("scaler.pkl")

# Create FastAPI app
app = FastAPI(
    title="Breast Cancer Prediction API",
    description="API to predict breast cancer using a trained Random Forest model.",
    version="1.0"
)

# Home Endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the Breast Cancer Prediction API!"
    }

# Input Schema
class PatientData(BaseModel):
    mean_radius: float
    mean_texture: float
    mean_perimeter: float
    mean_area: float
    mean_smoothness: float
    mean_compactness: float
    mean_concavity: float
    mean_concave_points: float
    mean_symmetry: float
    mean_fractal_dimension: float
    radius_error: float
    texture_error: float
    perimeter_error: float
    area_error: float
    smoothness_error: float
    compactness_error: float
    concavity_error: float
    concave_points_error: float
    symmetry_error: float
    fractal_dimension_error: float
    worst_radius: float
    worst_texture: float
    worst_perimeter: float
    worst_area: float
    worst_smoothness: float
    worst_compactness: float
    worst_concavity: float
    worst_concave_points: float
    worst_symmetry: float
    worst_fractal_dimension: float

# Prediction Endpoint
# Prediction Endpoint
@app.post("/predict")
def predict(data: PatientData):

    input_data = np.array([[
        data.mean_radius,
        data.mean_texture,
        data.mean_perimeter,
        data.mean_area,
        data.mean_smoothness,
        data.mean_compactness,
        data.mean_concavity,
        data.mean_concave_points,
        data.mean_symmetry,
        data.mean_fractal_dimension,
        data.radius_error,
        data.texture_error,
        data.perimeter_error,
        data.area_error,
        data.smoothness_error,
        data.compactness_error,
        data.concavity_error,
        data.concave_points_error,
        data.symmetry_error,
        data.fractal_dimension_error,
        data.worst_radius,
        data.worst_texture,
        data.worst_perimeter,
        data.worst_area,
        data.worst_smoothness,
        data.worst_compactness,
        data.worst_concavity,
        data.worst_concave_points,
        data.worst_symmetry,
        data.worst_fractal_dimension
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    probabilities = model.predict_proba(input_scaled)[0]
    confidence = float(max(probabilities))

    result = "Malignant" if prediction == 0 else "Benign"

    return {
        "prediction": result,
        "class": int(prediction),
        "confidence": round(confidence * 100, 2),
        "model": "Random Forest",
        "status": "Prediction Successful"
    }