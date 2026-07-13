from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Calories Burnt Prediction API",
    description="""
    A production-ready Machine Learning API built with FastAPI.

    Features:
    - Predict calories burnt during exercise
    - Input validation using Pydantic
    - XGBoost model inference
    - Automatic interactive API documentation
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(router)