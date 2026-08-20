from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import subprocess
import logging
import uuid

from backend.app.preprocess import load_audio, extract_spectrogram
from backend.app.model import predict_audio

from backend.app.schema import (
    PredictionResponse,
    ModelStatusResponse,
    HealthResponse,
    ServerInfoResponse
)
from backend.app.config import (
    UPLOAD_FOLDER,
    SUPPORTED_FORMATS,
    MAX_FILE_SIZE,
    TEMP_PATH,
    FFMPEG_PATH
)

router = APIRouter()

prediction_history = []

# FFMPEG_PATH = r"C:\Users\adity\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffmpeg.exe"

@router.get("/")
def home():
    return {
        "message": "Welcome to the Backend of AcousticSpace.",
        "status": "Running"
    }


@router.get("/user")
def user_greet():
    return {
        "message": "Welcome!"
    }


@router.get("/health", response_model=HealthResponse)
def health_check_server():
    return {
        "status": "OK"
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

    original_path = None
    converted_path = None

    try:


        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="No file selected."
            )

        original_filename = file.filename.lower()


        contents = await file.read()

        if not contents:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds 20 MB."
            )

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        unique_id = uuid.uuid4().hex[:8]

        original_extension = os.path.splitext(
            original_filename
        )[1]

        original_name = f"audio_{unique_id}{original_extension}"

        original_path = os.path.join(
            UPLOAD_FOLDER,
            original_name
        )


        with open(original_path, "wb") as buffer:
            buffer.write(contents)

        print("Audio saved:", original_path)


        extension = original_extension.lower()

        if extension == ".webm":

            converted_filename = f"converted_{unique_id}.wav"

            converted_path = os.path.join(
                UPLOAD_FOLDER,
                converted_filename
            )

            print("Converting WebM to WAV...")


            if not os.path.exists(FFMPEG_PATH):
                raise RuntimeError(
                    f"FFmpeg not found at: {FFMPEG_PATH}"
                )


            result = subprocess.run(
                [
                    FFMPEG_PATH,
                    "-y",
                    "-i",
                    original_path,
                    "-ac",
                    "1",
                    "-ar",
                    "16000",
                    "-c:a",
                    "pcm_s16le",
                    converted_path
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode != 0:

                print("FFmpeg ERROR:")
                print(result.stderr)

                raise RuntimeError(
                    "Unable to convert microphone recording to WAV."
                )

            if not os.path.exists(converted_path):
                raise RuntimeError(
                    "WAV file was not created."
                )

            print(
                "Converted WAV:",
                converted_path
            )

            processing_path = converted_path

        else:

            processing_path = original_path


        print("Loading audio...")

        audio_info = load_audio(
            processing_path
        )

        print(
            "Audio info:",
            audio_info
        )


        print("Creating spectrogram...")

        spectrogram_tensor = extract_spectrogram(
            processing_path
        )

        print(
            "Spectrogram created successfully."
        )


        print("Running prediction...")

        prediction = predict_audio(
            spectrogram_tensor
        )

        print(
            "Prediction:",
            prediction
        )


        prediction_history.append(
            {
                "filename": file.filename,
                "prediction": prediction.get(
                    "prediction"
                ),
                "confidence": prediction.get(
                    "confidence"
                )
            }
        )

        return {
            "filename": file.filename,
            "message": "Audio received and processed successfully",
            "saved_location": processing_path,
            "audio_info": audio_info,
            "prediction": prediction
        }

    except HTTPException:
        raise

    except Exception as e:

        logging.exception(
            "Prediction error"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        if original_path and os.path.exists(original_path):

            try:
                os.remove(original_path)

            except PermissionError:
                print(
                    "Could not delete original file yet:",
                    original_path
                )

            except Exception as cleanup_error:
                print(
                    "Original cleanup error:",
                    cleanup_error
                )

        if converted_path and os.path.exists(converted_path):

            try:
                os.remove(converted_path)

            except PermissionError:
                print(
                    "Could not delete converted file yet:",
                    converted_path
                )

            except Exception as cleanup_error:
                print(
                    "Converted cleanup error:",
                    cleanup_error
                )

        try:

            if os.path.exists(TEMP_PATH):
                os.remove(TEMP_PATH)

        except PermissionError:

            print(
                "Could not delete temporary file yet."
            )

        except Exception as cleanup_error:

            print(
                "Temporary cleanup error:",
                cleanup_error
            )

@router.get("/test")
def test_route():
    return {
        "message": "Routes module is working successfully."
    }

@router.get("/supported-formats")
def data_format():
    return {
        "supported_format": [
            ".wav",
            ".mp3",
            ".webm"
        ],
        "message": "These are the supported audio formats."
    }


@router.get(
    "/model-status",
    response_model=ModelStatusResponse
)
def model_status():

    return {
        "model": "AcousticCNN",
        "framework": "PyTorch",
        "status": "Loaded"
    }

@router.get(
    "/server-info",
    response_model=ServerInfoResponse
)
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
        "total_predictions": len(
            prediction_history
        ),
        "history": prediction_history
    }