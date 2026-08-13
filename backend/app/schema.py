from pydantic import BaseModel
from typing import Any

class PredictionResponse(BaseModel):
    filename: str
    message: str
    saved_location: str
    audio_info: dict[str, Any]
    prediction: dict[str, Any]

class ModelStatusResponse(BaseModel):
    model: str
    framework: str
    status: str

class HealthResponse(BaseModel):
    status: str

class ServerInfoResponse(BaseModel):
    project: str
    backend: str
    framework: str
    api_version: str
    status: str