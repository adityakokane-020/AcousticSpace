from pathlib import Path


UPLOAD_FOLDER = "uploads"

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SUPPORTED_FORMATS = (".wav", ".mp3", ".webm")

MAX_FILE_SIZE = 20 * 1024 * 1024 

MODEL_PATH = PROJECT_ROOT / "ml" / "model" / "best_model.pth"

TEMP_PATH = "uploads/temp.png"

FFMPEG_PATH = r"C:\Users\adity\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffmpeg.exe"