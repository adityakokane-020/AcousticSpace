from fastapi import FastAPI
<<<<<<< HEAD
from backend.app.routes import router
from fastapi.middleware.cors import CORSMiddleware
=======
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

>>>>>>> 13c6cb6adc3b5d46636f713b3a2c1d4f13b20d61

app = FastAPI(
    title="AcousticSpace",
    version="1.0.0",
    description="Backend API of AcousticSpace Project."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)