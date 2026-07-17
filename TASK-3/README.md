# Breast Cancer Prediction API

## Description
This project deploys a trained Random Forest classifier using FastAPI to predict whether a breast tumor is Benign or Malignant.

## Technologies
- Python
- FastAPI
- Scikit-learn
- Joblib
- Docker

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Endpoint

POST /predict

Returns the predicted class for the provided breast cancer features.