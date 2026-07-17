# 🤖 Alfido Tech AI Internship Projects

This repository contains the projects completed during my **AI Internship at Alfido Tech**. The internship focused on applying Machine Learning, Deep Learning, Transfer Learning, and Model Deployment to solve real-world problems.

---

## 📌 Internship Details

- **Intern:** Yuvraj Singh Tomar
- **CID:** IS-2026-9762
- **Internship:** Alfido Tech AI Internship

---

# 📂 Projects

## 🔹 Task 1 – Customer Churn Prediction Using Machine Learning

### Description
Developed a machine learning model to predict whether a customer is likely to churn using supervised learning algorithms.

### Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

### Machine Learning Models
- Logistic Regression
- Random Forest Classifier

### Features
- Data Preprocessing
- Exploratory Data Analysis
- Feature Scaling
- Hyperparameter Tuning
- Cross Validation
- Model Evaluation
- Model Saving

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- ROC Curve
- ROC-AUC Score
- Confusion Matrix

---

## 🌸 Task 2 – Flower Image Classification Using MobileNetV2

### Description
Implemented a deep learning image classifier using **Transfer Learning** with MobileNetV2 to classify flower images into five categories.

### Technologies Used
- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

### Dataset
TensorFlow Flowers Dataset

### Flower Classes
- Daisy
- Dandelion
- Roses
- Sunflowers
- Tulips

### Features
- Image Preprocessing
- Data Augmentation
- Transfer Learning
- MobileNetV2
- Model Training
- Performance Evaluation

---

## 🩺 Task 3 – Breast Cancer Prediction API

### Description
Developed a REST API using **FastAPI** to predict whether a breast tumor is benign or malignant using a trained Random Forest model.

### Technologies Used
- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Joblib
- Docker

### Features
- REST API
- JSON Request & Response
- Swagger UI Documentation
- Docker Support
- Model Deployment

### API Endpoints

#### GET /

Returns a welcome message.

#### POST /predict

Accepts patient diagnostic measurements and returns:

- Prediction
- Class
- Confidence Score
- Model Name

---

# 📁 Repository Structure

```
AlfidoTech-AI-Internship
│
├── Task1_Customer_Churn/
│   ├── Task1.ipynb
│   ├── Report.pdf
│   ├── best_classification_model.pkl
│   ├── scaler.pkl
│   └── README.md
│
├── Task2_Flower_Classification/
│   ├── Task2.ipynb
│   ├── Report.pdf
│   ├── cifar10_mobilenetv2.keras
│   └── README.md
│
├── Task3_BreastCancer_API/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── README.md
│   ├── best_classification_model.pkl
│   └── scaler.pkl
│
└── README.md
```

---

# 🚀 How to Run

## Task 1

Open the notebook and run all cells.

```
jupyter notebook
```

---

## Task 2

Open the notebook and execute all cells.

```
jupyter notebook
```

---

## Task 3

Install dependencies

```bash
pip install -r requirements.txt
```

Start the FastAPI server

```bash
uvicorn app:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📊 Skills Demonstrated

- Machine Learning
- Deep Learning
- Transfer Learning
- Computer Vision
- Data Preprocessing
- Model Evaluation
- Hyperparameter Tuning
- FastAPI
- REST API Development
- Docker
- Python
- TensorFlow
- Scikit-learn

---

# 📜 License

This repository was created for educational and internship purposes as part of the **Alfido Tech AI Internship**.

---

## 👨‍💻 Author

**Yuvraj Singh Tomar**

AI & Machine Learning Enthusiast

GitHub: https://github.com/YuvrajSinghTomar01