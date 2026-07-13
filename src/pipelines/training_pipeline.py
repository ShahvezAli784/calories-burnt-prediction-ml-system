"""
Training pipeline.

This module orchestrates the complete machine learning workflow:

1. Load data
2. Preprocess data
3. Split dataset
4. Train model
5. Evaluate model
6. Save trained model
7. Return evaluation metrics
"""

from src.data.loader import load_data
from src.data.preprocessing import preprocess_data
from src.data.splitter import split_data

from src.models.train import train_model
from src.models.evaluate import evaluate_model
from src.models.save_model import save_model
from src.models.save_metrics import save_metrics

from src.utils.logger import logger


def run_training_pipeline():
    """
    Execute the complete training pipeline.

    Returns:
        dict: Evaluation metrics.
    """

    logger.info("=" * 60)
    logger.info("Starting training pipeline")
    logger.info("=" * 60)

    # Load data
    df = load_data()

    # Preprocess data
    X, y = preprocess_data(df)

    # Split dataset
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    metrics = evaluate_model(model, X_test, y_test)

    # Save model
    save_model(model)
    
    #save metrics
    save_metrics(metrics)

    logger.info("Training pipeline completed successfully.")

    return metrics