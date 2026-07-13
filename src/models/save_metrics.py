"""
Utilities for saving evaluation metrics.
"""

import json
from pathlib import Path
from typing import Dict

from src.config import METRICS_DIR
from src.utils.logger import logger


DEFAULT_FILENAME = "metrics.json"


def save_metrics(
    metrics: Dict[str, float],
    filename: str = DEFAULT_FILENAME,
) -> Path:
    """
    Save evaluation metrics to a JSON file.

    Args:
        metrics: Dictionary containing evaluation metrics.
        filename: Output filename.

    Returns:
        Path to saved metrics file.
    """

    METRICS_DIR.mkdir(parents=True, exist_ok=True)

    file_path = METRICS_DIR / filename

    with open(file_path, "w") as file:
        json.dump(metrics, file, indent=4)

    logger.info("Metrics saved to %s", file_path)

    return file_path