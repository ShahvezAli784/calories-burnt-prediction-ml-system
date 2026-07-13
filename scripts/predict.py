"""
Prediction script.

Entry point for running predictions.
"""

import pandas as pd

from src.pipelines.predict_pipeline import run_prediction_pipeline


def create_sample() -> pd.DataFrame:
    """
    Create sample input data for testing.
    """

    return pd.DataFrame(
        {
            "Gender": ["Male"],
            "Age": [24],
            "Height": [180],
            "Weight": [75],
            "Duration": [30],
            "Heart_Rate": [110],
            "Body_Temp": [40.0],
        }
    )


def main():
    sample = create_sample()

    prediction = run_prediction_pipeline(sample)

    print("\nPrediction")
    print("-" * 20)
    print(f"Predicted Calories Burned: {prediction[0]:.2f}")


if __name__ == "__main__":
    main()