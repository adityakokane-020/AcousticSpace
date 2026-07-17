from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.preprocess import load_audio, extract_spectrogram
from app.model import predict_audio

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

@router.get("/health")
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

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_path = os.path.join("uploads",file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    audio_info = load_audio(file_path)
    spectogram_info = extract_spectrogram(file_path)
    prediction = predict_audio(spectogram_info)
    return {
        "filename": file.filename,
        "message": "Audio received and processed successfully",
        "saved_location": file_path,
        "audio_info": audio_info,
        "spectogram_info": spectogram_info,
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

@router.get("/model-status")
def model_status():
    return{
        "model": "Not loaded",
        "framework": "PyTorch",
        "status": "Waiting for trained model"
    }
@router.get("/server-info")
def server_info():
    return {
        "project": "AcousticSpace",
        "backend": "FastAPI",
        "framework": "Python",
        "api_version": "1.0.0",
        "status": "Running"
    }