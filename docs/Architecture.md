# System Architecture

## Overview
The AcousticSpace project is divided into three main modules:

- Frontend (React + Vite)
- Backend (FastAPI)
- Machine Learning (PyTorch)

The frontend sends audio files to the backend.
The backend processes the request and forwards it to the ML model.
The ML model predicts whether the audio is Real or Deepfake and returns the result.
