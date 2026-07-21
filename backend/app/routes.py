from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.preprocess import load_audio, extract_spectrogram
from app.model import predict_audio
from app.schema import (
    PredictionResponse,
    ModelStatusResponse,
    HealthResponse,
    ServerInfoResponse
)

router = APIRouter()


@router.get("/")
def home():
    return{
        "message": "Welcome to the Backend of AcousticSpace .",
        "status" : "Running"
    }
@router.get("/user")
def user_greet():
    return{
        "message": "Welcome !"
    }

@router.get("/health", response_class=HealthResponse)
def health_check_server():
    return{
        "status" : "OK"
    }

@router.get("/about")
def about():
    return {
        "project": "AcousticSpace",
        "theme": "Deepfake Audio Detection",
        "backend": "FastAPI",
        "version": "1.0.0"
    }

@router.post("/predict", response_class=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    file_path = os.path.join("uploads",file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    if not file.filename.endswith(('wav', 'mp3')):
       return{
        "message": "only wav and mp3 formats are supported"
    }
    audio_info = load_audio(file_path)
    spectrogram_info = extract_spectrogram(file_path)
    prediction = predict_audio(spectrogram_info)
    return {
        "filename": file.filename,
        "message": "Audio received and processed successfully",
        "saved_location": file_path,
        "audio_info": audio_info,
        "spectrogram_info": spectrogram_info,
        "prediction": prediction
    }

@router.get("/test")
def test_route():
    return {
        "message": "Routes module is working successfully."
    }

@router.get("/supported-formats")
def data_format():
    return{
        "supported_format": [".wav",".mp3"],
        "message": "These are the supported audio formats."
    }

@router.get("/model-status", response_class=ModelStatusResponse)
def model_status():
    return{
        "model": "Not loaded",
        "framework": "PyTorch",
        "status": "Waiting for trained model"
    }
@router.get("/server-info", response_class=ServerInfoResponse)
def server_info():
    return {
        "project": "AcousticSpace",
        "backend": "FastAPI",
        "framework": "Python",
        "api_version": "1.0.0",
        "status": "Running"
    }
@router.get("/prediction-history")
def prediction_history():
    return {
        "total_predictions": 0,
        "history": [],
        "message": "No predictions available yet."
    }

