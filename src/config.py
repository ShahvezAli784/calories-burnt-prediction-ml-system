"""
Project-wide configuration and path definitions.
"""

from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parents[1]

# Data Directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Model Directories
MODEL_DIR = BASE_DIR / "models"
TRAINED_MODEL_DIR = MODEL_DIR / "trained"
CHECKPOINT_DIR = MODEL_DIR / "checkpoints"
METRICS_DIR = MODEL_DIR / "metrics"