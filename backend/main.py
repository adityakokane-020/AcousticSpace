from fastapi import FastAPI
from app.routes import router


app = FastAPI(
    title = "AcousticSpace",
    version = "1.0.0",
    description = "Backend API of AcousticSpace Project."
)

app.include_router(router)


