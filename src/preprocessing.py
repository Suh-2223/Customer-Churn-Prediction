import pandas as pd

def preprocess_input(input_df, feature_names):
    """
    Preprocess user input for prediction.
    """

    # One-Hot Encode categorical columns
    input_encoded = pd.get_dummies(input_df)

    # Add missing columns
    for col in feature_names:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    # Keep only the columns used during training
    input_encoded = input_encoded[feature_names]

    return input_encoded