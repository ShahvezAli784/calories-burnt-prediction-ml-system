from xgboost import XGBRegressor
from src.utils.logger import logger

from src.config import RANDOM_STATE , XGB_PARAMS
import pandas as pd
from xgboost import XGBRegressor

def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> XGBRegressor:
    """
    Train an XGBoost regression model.

    Args:
        X_train: Training feature matrix.
        y_train: Training labels.

    Returns:
      Trained XGBRegressor.
    """
    
    logger.info("initializing XGBoost regressor")
    
    model = XGBRegressor(**XGB_PARAMS)  
    
    logger.info("Training model...")
    model.fit(X_train,y_train)
    return model