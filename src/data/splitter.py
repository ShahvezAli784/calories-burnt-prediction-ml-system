"""
Data splitting utilities.

This module is responsible for splitting the dataset into
training and testing sets.

No preprocessing or model training should happen here.
"""

from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import TEST_SIZE, RANDOM_STATE
from src.utils.logger import logger


def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
    shuffle: bool = True,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split the dataset into training and testing sets.

    Args:
        X: Feature matrix.
        y: Target variable.
        test_size: Fraction of data used for testing.
        random_state: Random seed for reproducibility.
        shuffle: Whether to shuffle the data before splitting.

    Returns:
        Tuple containing:
            - X_train
            - X_test
            - y_train
            - y_test
    """

    logger.info("Splitting dataset...")
    logger.info(
        "Parameters -> test_size=%.2f | random_state=%d | shuffle=%s",
        test_size,
        random_state,
        shuffle,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        shuffle=shuffle,
    )

    logger.info(
        "Training samples: %d | Testing samples: %d",
        len(X_train),
        len(X_test),
    )

    return X_train, X_test, y_train, y_test