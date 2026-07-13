from fastapi import APIRouter

from app.schemas.request import PredictionRequest
from app.schemas.response import PredictionResponse
from app.services.prediction_service import prediction_serivice

route = APIRouter()

@route.post(
    "/predic",
    response_model=PredictionResponse,
    summary="Predict calories burnt",
    tags=["Prediction"]
)

def predict(request:PredictionRequest):
    prediction = prediction_serivice.predict(request)
    
    return PredictionResponse(
        predict_calories = prediction
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