from xgboost import XGBRegressor
from src.utils.logger import logger

from src.config import RANDOM_STATE , XGB_PARAMS
def train_model(
    X_train,
    y_train,
    random_state = RANDOM_STATE
):
    """
    TrainXGBoost model
    
    X_train :Training Features
    y_train:Training Labels
    random state:random seed
    """ 
    
    logger.info("initializing XGBoost regressor")
    
    model = XGBRegressor(**XGB_PARAMS)  
    
    logger.info("Training model...")
    model.fit(X_train,y_train)
    return model