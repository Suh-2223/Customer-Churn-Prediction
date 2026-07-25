import joblib
import pandas as pd

from src.preprocessing import preprocess_input

# Load model
model = joblib.load("artifacts/churn_model.pkl")

# Load feature names
feature_names = joblib.load("artifacts/feature_names.pkl")


def predict_churn(user_input):
    """
    Predict customer churn.
    """

    input_df = pd.DataFrame([user_input])

    processed_data = preprocess_input(input_df, feature_names)

    prediction = model.predict(processed_data)[0]

    if prediction == 1:
        return "Customer is likely to Churn"
    else:
        return "Customer is likely to Stay"