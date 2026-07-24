from fastapi import FastAPI, UploadFile, File
import shutil
import os

from ml.inference import predict_audio

app = FastAPI()

UPLOAD_FOLDER = "ml/audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict_audio(file_path)

    return result