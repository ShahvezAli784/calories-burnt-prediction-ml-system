from fastapi import APIRouter

from app.schemas.request import PredictionRequest
from app.schemas.response import PredictionResponse
from app.services.prediction_service import prediction_service

router = APIRouter()

@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict calories burnt",
    tags=["Prediction"]
)

def predict(request:PredictionRequest):
    prediction = prediction_service.predict(request)
    
    return PredictionResponse(
        predicted_calories = prediction
    )
    
@router.get(
    "/health",
    tags=["Health"],
    summary="Health Check"
)
def health_check():
    return {
        "status": "healthy"
    }    