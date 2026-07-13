"""
Model evaluation utilities.

This module is responsible for evaluating regression models
using prediction results.

No prediction or model training logic should be implemented here.
"""

from typing import Dict

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score,
)

from src.models.predict import predict
from src.utils.logger import logger

from typing import Any
import pandas as pd

def evaluate_model(
    model: Any,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Dict[str, float]:
    """
    Evaluate a trained regression model.

    Args:
        model: Trained model.
        X_test: Test features.
        y_test: Ground truth labels.

    Returns:
        Dictionary containing evaluation metrics.
    """

    predictions = predict(model, X_test)

    logger.info("Calculating evaluation metrics...")

    metrics = {
        "MAE": round(
            mean_absolute_error(y_test, predictions),
            4,
        ),
        "RMSE": round(
            root_mean_squared_error(
                y_test,
                predictions,
            ),
            4,
        ),
        "R2": round(
            r2_score(
                y_test,
                predictions,
            ),
            4,
        ),
    }

    logger.info("Evaluation completed.")
    logger.info("Metrics: %s", metrics)

    return metrics