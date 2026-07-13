"""
Prediction service.

Handles prediction requests coming from the FastAPI layer.
"""

import pandas as pd

from app.schemas.request import PredictionRequest
from src.pipelines.predict_pipeline import run_prediction_pipeline


class PredictionService:
    """
    Service responsible for handling prediction requests.
    """

    def predict(
        self,
        request: PredictionRequest,
    ) -> float:
        """
        Predict calories burned from the request data.

        Args:
            request: Validated prediction request.

        Returns:
            Predicted calories burned.
        """

        input_data = pd.DataFrame([
            {
                "Gender": request.gender,
                "Age": request.age,
                "Height": request.height,
                "Weight": request.weight,
                "Duration": request.duration,
                "Heart_Rate": request.heart_rate,
                "Body_Temp": request.body_temp,
            }
        ])

        prediction = run_prediction_pipeline(input_data)

        return float(prediction[0])


prediction_service = PredictionService()