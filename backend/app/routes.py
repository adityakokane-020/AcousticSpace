from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import logging
from app.preprocess import load_audio, extract_spectrogram
from app.model import predict_audio
from app.schema import (
    PredictionResponse,
    ModelStatusResponse,
    HealthResponse,
    ServerInfoResponse
)
from app.config import(
    UPLOAD_FOLDER,
    SUPPORTED_FORMATS,
    MAX_FILE_SIZE,
    TEMP_PATH
)

router = APIRouter()
prediction_history = []


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

@router.get("/health", response_model=HealthResponse)
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

@router.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    try:
        if not file.filename.lower().endswith((SUPPORTED_FORMATS)):
            return{
                     "message": "only wav and mp3 formats are supported"
                    }
        
        contents = await file.read()

        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail = "File size exceeds 20 MB"
            )
        await file.seek(0)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER,file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        audio_info = load_audio(file_path)
        spectrogram_tensor = extract_spectrogram(file_path)
        prediction = predict_audio(spectrogram_tensor)

        prediction_history.append({
            "filename": file.filename,
            "prediction": prediction["prediction"],
            "confidence": prediction["confidence"]
        })

        if os.path.exists(file_path):
            os.remove(file_path)

        temp_path = TEMP_PATH

        if os.path.exists(temp_path):
            os.remove(temp_path)

        return {
            "filename": file.filename,
            "message": "Audio received and processed successfully",
            "saved_location": file_path,
            "audio_info": audio_info,
            "prediction": prediction
        }
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
             status_code=500,
             detail = "Invalid Audio Input"
        )
           
        
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

@router.get("/model-status", response_model=ModelStatusResponse)
def model_status():
    return{
        "model": "AcousticCNN",
        "framework": "PyTorch",
        "status": "Loaded"
    }
@router.get("/server-info", response_model=ServerInfoResponse)
def server_info():
    return {
        "project": "AcousticSpace",
        "backend": "FastAPI",
        "framework": "Python",
        "api_version": "1.0.0",
        "status": "Running"
    }
@router.get("/prediction-history")
def get_prediction_history():
    return {
        "total_predictions": len(prediction_history),
        "history": prediction_history
    }

