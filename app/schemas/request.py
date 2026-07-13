from enum import Enum

from pydantic import BaseModel, Field


class Gender(str, Enum):
    male = "male"
    female = "female"


class PredictionRequest(BaseModel):
    gender: Gender
    age: int = Field(..., gt=0, examples=[25])
    height: float = Field(..., gt=0, examples=[175])
    weight: float = Field(..., gt=0, examples=[70])
    duration: float = Field(..., gt=0, examples=[30])
    heart_rate: float = Field(..., gt=0, examples=[120])
    body_temp: float = Field(..., gt=0, examples=[38.5])