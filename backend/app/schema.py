from pydantic import BaseModel
from typing import Any

class PredictionRESPONSE(BaseModel):
    filename: str
    message: str
    saved_location: str
    audio_info:  dict[str, Any] 
    spectrogram_info: dict[str, Any]
    prediction: dict[str, Any]

class ModelSTATUS(BaseModel):
    model: str
    framework: str
    status: str

class HealthSTATUS(BaseModel):
    status: str

class ServerINFO(BaseModel):
    project: str
    backend: str
    framework: str
    api_version: str
    status: str