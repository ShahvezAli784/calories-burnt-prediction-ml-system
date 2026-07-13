"""
Data loading utilities.

This module is responsible for:
- Locating dataset files
- Loading datasets
- Validating datasets
- Combining datasets

No preprocessing or feature engineering should happen here.
"""

from pathlib import Path

import pandas as pd



from src.config import RAW_DATA_DIR
from src.utils.logger import logger

CALORIES_PATH = RAW_DATA_DIR / "calories.csv"
EXERCISE_PATH = RAW_DATA_DIR / "exercise.csv"



def _validate_file_exists(file_path: Path) -> None:
    """
    Ensure a dataset file exists.

    Args:
        file_path: Path to dataset file.

    Raises:
        FileNotFoundError: If file does not exist.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")


def _validate_dataset(calories: pd.DataFrame,
                      exercise: pd.DataFrame) -> None:
    """
    Validate datasets before merging.

    Raises:
        ValueError:
            - Missing Calories column
            - Different number of rows
    """

    if "Calories" not in calories.columns:
        raise ValueError(
            "'Calories' column not found in calories dataset."
        )

    if len(calories) != len(exercise):
        raise ValueError(
            "Calories and Exercise datasets contain different numbers of rows."
        )



def load_calories() -> pd.DataFrame:
    """
    Load calories dataset.

    Returns:
        Loaded calories dataframe.
    """

    logger.info("Loading calories dataset...")

    _validate_file_exists(CALORIES_PATH)

    df = pd.read_csv(CALORIES_PATH)

    logger.info("Calories dataset loaded successfully.")

    return df


def load_exercise() -> pd.DataFrame:
    """
    Load exercise dataset.

    Returns:
        Loaded exercise dataframe.
    """

    logger.info("Loading exercise dataset...")

    _validate_file_exists(EXERCISE_PATH)

    df = pd.read_csv(EXERCISE_PATH)

    logger.info("Exercise dataset loaded successfully.")

    return df



def load_data() -> pd.DataFrame:
    """
    Load and combine project datasets.

    Returns:
        Combined dataframe containing exercise features
        and target calories.
    """

    logger.info("Loading complete dataset...")

    calories = load_calories()
    exercise = load_exercise()

    _validate_dataset(calories, exercise)

    dataset = exercise.copy()
    dataset["Calories"] = calories["Calories"]

    logger.info(
        "Dataset successfully created with shape %s",
        dataset.shape,
    )

    return dataset