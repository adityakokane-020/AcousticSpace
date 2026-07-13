from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()


@router.get("/")
def home():
    return{
        "message": "Welcome to the Backend of AcousticSpace .",
        "status" : "Running"
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
    file_path = os.path.join("updates",file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "filename": file.filename,
        "message": "Audio received successfully",
        "saved_location": file_path
    }
@router.get("/test")
def test_route():
    return {
        "message": "Routes module is working successfully."
    }

@router.get("/user")
def user_greet():
    return{
        "message": "Welcome !"

    }