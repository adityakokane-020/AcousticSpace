from fastapi import FastAPI

app = FastAPI(
    title = "AcousticSpace",
    version = "1.0.0",
    description = "Backend API of AcousticSpace Project."
)

@app.get("/")
def home():
    return{
        "message": "Welcome to the Backend of AcousticSpace .",
        "status" : "Running"
    }

@app.get("/health")
def health_check_server():
    return{
        "status" : "OK"
    }

@app.get("/about")
def about():
    return {
        "project": "AcousticSpace",
        "theme": "Deepfake Audio Detection",
        "backend": "FastAPI",
        "version": "1.0.0"
    }