import pandas as pd


def preprocess_input(input_df, feature_names):
    """
    Preprocess customer input for churn prediction.
    """

    # One-hot encode categorical columns
    input_encoded = pd.get_dummies(input_df)

    # Create all missing columns at once
    missing_columns = {
        col: 0
        for col in feature_names
        if col not in input_encoded.columns
    }

    if missing_columns:
        input_encoded = pd.concat(
            [input_encoded, pd.DataFrame(missing_columns, index=input_encoded.index)],
            axis=1
        )

    # Keep only the features used during model training
    input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)

    return input_encoded