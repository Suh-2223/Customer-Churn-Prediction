# Customer Churn Prediction

## Project Overview

Customer churn prediction is a machine learning project that predicts whether a customer is likely to leave a service or continue using it.

The goal of this project is to help businesses identify customers who are at risk of churning and take preventive actions.

---

## Problem Statement

Customer retention is important for businesses. By predicting churn, companies can understand customer behavior and create strategies to improve customer satisfaction.

This project uses machine learning classification algorithms to predict customer churn.

---

## Dataset

The project uses the Telco Customer Churn dataset.

The dataset contains customer information such as:

- Customer demographics
- Services subscribed
- Contract details
- Payment methods
- Monthly charges
- Total charges
- Churn status

Target Variable:

- Churn
  - No → Customer stays
  - Yes → Customer leaves

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## Project Workflow
Data Collection
        |
        ↓
Exploratory Data Analysis
        |
        ↓
Data Cleaning
        |
        ↓
Feature Engineering
       |
       ↓
Model Training
       |
       ↓
Model Evaluation
       |
       ↓
Model Saving
       |
       ↓
Prediction Function
        |
        ↓
Streamlit Application


---

## Machine Learning Models Used

The following models were trained and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbors
5. Naive Bayes

---

## Model Performance

| Model | Accuracy |
|---|---|
| Logistic Regression | 80.31% |
| Random Forest | 78.96% |
| Decision Tree | 77.83% |
| KNN | 74.63% |
| Naive Bayes | 64.39% |

### Best Model

Logistic Regression was selected as the final model because it achieved the highest accuracy.

---

## Project Structure


Customer-Churn-Prediction/

│
├── artifacts/
│ ├── churn_model.pkl
│ ├── feature_names.pkl
│ └── numerical_cols.pkl
│
├── data/
│
├── notebooks/
│ └── 01_eda.ipynb
│
├── src/
│ ├── preprocessing.py
│ └── predict.py
│
├── app.py
├── requirements.txt
└── README.md