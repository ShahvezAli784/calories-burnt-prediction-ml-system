"""
Prediction pipeline.

This module orchestrates the complete prediction workflow:

1. Load trained model
2. Preprocess input data
3. Generate predictions
4. Return prediction results
"""

from typing import Any

import pandas as pd

from src.models.save_model import load_model
from src.models.predict import predict
from src.utils.logger import logger

from src.data.preprocessing import preprocess_input

def run_prediction_pipeline(
    input_data: pd.DataFrame,
    model_name: str = "xgb_model.pkl",
) -> Any:
    """
    Execute the complete prediction pipeline.

    Args:
        input_data: Input feature dataframe.
        model_name: Saved model filename.

    Returns:
        Model predictions.
    """

    logger.info("=" * 60)
    logger.info("Starting prediction pipeline")
    logger.info("=" * 60)

    # Load trained model
    model = load_model(model_name)

    # TODO:
    # Apply preprocessing here if new user input requires it.
    # Example:
    # input_data = preprocess_input(input_data)

    processed_input = preprocess_input(input_data)
    predictions = predict(model, processed_input)
    logger.info("Prediction pipeline completed successfully.")

    return predictions