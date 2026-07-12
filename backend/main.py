from fastapi import FastAPI, UploadFile, File
import os
import shutil
from app.routes import router


app = FastAPI(
    title = "AcousticSpace",
    version = "1.0.0",
    description = "Backend API of AcousticSpace Project."
)

app.include_router(router)


# @app.get("/")
# def home():
#     return{
#         "message": "Welcome to the Backend of AcousticSpace .",
#         "status" : "Running"
#     }

# @app.get("/health")
# def health_check_server():
#     return{
#         "status" : "OK"
#     }

# @app.get("/about")
# def about():
#     return {
#         "project": "AcousticSpace",
#         "theme": "Deepfake Audio Detection",
#         "backend": "FastAPI",
#         "version": "1.0.0"
#     }

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     file_path = os.path.join("updates",file.filename)
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     return {
#         "filename": file.filename,
#         "message": "Audio received successfully",
#         "saved_location": file_path
#     }