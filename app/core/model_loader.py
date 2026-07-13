from functools import lru_cache
import pickle

from src.config import TRAINED_MODEL_DIR


DEFAULT_MODEL_NAME = "xgb_model.pkl"


@lru_cache(maxsize=1)
def load_model(
    model_name: str = DEFAULT_MODEL_NAME,
):
    """
    Load and cache the trained model.
    """

    model_path = TRAINED_MODEL_DIR / model_name

    with open(model_path, "rb") as file:
        return pickle.load(file)