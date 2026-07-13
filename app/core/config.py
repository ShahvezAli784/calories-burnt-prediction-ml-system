from pathlib import Path 


# Project Root
BASE_DIR = Path(__file__).resolve().parents[2]

# Model Path
MODEL_PATH = BASE_DIR / "models" / "xgb_model.pkl"