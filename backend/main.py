from fastapi import FastAPI
from backend.app.routes import router
from fastapi.middleware.cors import CORSMiddleware


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