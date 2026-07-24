# AcousticSpace

## Project Title
AcousticSpace: Deepfake Audio Detection using Room Impulse Response (RIR)

## Problem Statement
Current deepfake audio detectors mainly focus on voice characteristics. This project detects deepfake audio using Room Impulse Response (RIR), making detection more reliable.

## Team Members
- Aditya Kokane (Team Leader)
- Backend Developer
- Frontend Developer
- ML Developer

## Tech Stack

### Backend
- Python
- FastAPI

### Frontend
- React + Vite
- TypeScript

### Machine Learning
- PyTorch
- Librosa
- NumPy

## Folder Structure

backend/
frontend/
ml/
docs/
assets/

## Setup Instructions

Coming Soon...

## Current Status

Project Initialization Completed.

## Future Scope

- Improve Detection Accuracy
- Real-time Audio Detection
- Cloud Deployment

- ## Project Architecture

![AcousticSpace Architecture](assets/architecture.png)

# AcousticSpace ML Module

## Model
- Random Forest Classifier

## Dataset
- ASVspoof2019 LA

## Extracted Features
- MFCC
- Zero Crossing Rate
- Spectral Centroid
- Chroma

## Evaluation
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- Feature Importance

## Saved Model
deepfake_detector_optimized.pkl

# Machine Learning Module

## Overview
This module is responsible for detecting deepfake audio using Room Impulse Response (RIR) features.

## Current Progress
- Dataset collection completed (ASVspoof)
- Dataset preprocessing completed
- Audio feature extraction implemented
- Initial model training pipeline created

## Files
- create_dataset.py
- extract_features.py
- extract_dataset_features.py
- train.py

## Next Tasks
- Train the deep learning model
- Save trained model
- Build prediction pipeline
- Integrate with FastAPI backend
