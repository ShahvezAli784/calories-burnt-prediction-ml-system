"""
Data preprocessing utilities.

This module is responsible for:
- Validating the dataset
- Encoding categorical features
- Preparing features and target variables

No model training or prediction should happen here.
"""

from typing import Tuple

import pandas as pd

from src.utils.logger import logger


REQUIRED_COLUMNS = [
    "User_ID",
    "Gender",
    "Age",
    "Height",
    "Weight",
    "Duration",
    "Heart_Rate",
    "Body_Temp",
    "Calories",
]


def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate that all required columns exist.

    Args:
        df: Input dataframe.

    Raises:
        ValueError: If required columns are missing.
    """

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )


def encode_gender(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode gender column.

    male -> 0
    female -> 1

    Args:
        df: Input dataframe.

    Returns:
        Encoded dataframe.
    """

    logger.info("Encoding gender column...")

    df = df.copy()

    df["Gender"] = (
        df["Gender"]
        .str.lower()
        .map({
            "male": 0,
            "female": 1,
        })
    )

    return df


def create_features_and_target(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Split dataframe into features and target.

    Returns:
        X, y
    """

    X = df.drop(columns=["User_ID", "Calories"])

    y = df["Calories"]

    return X, y


def preprocess_data(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Complete preprocessing pipeline.

    Returns:
        X, y
    """

    logger.info("Starting preprocessing...")

    validate_dataframe(df)

    df = encode_gender(df)

    X, y = create_features_and_target(df)

    logger.info("Preprocessing completed successfully.")

    return X, y