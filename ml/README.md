# Machine Learning Module

## Overview

The Machine Learning module detects deepfake audio using a PyTorch-based Convolutional Neural Network (CNN). It converts uploaded audio into Mel Spectrogram images and classifies them as Real or Fake.

---

## Dataset

- Dataset: ASVspoof2019 Logical Access (LA)
- Total Samples:
  - Real (Bonafide): 2,580
  - Fake (Spoof): 22,800

---

## Model

- Framework: PyTorch
- Model: Convolutional Neural Network (CNN)
- Input: Mel Spectrogram Images
- Output:
  - REAL AUDIO
  - FAKE AUDIO

---

## Training Results

- Test Accuracy: **99.92%**

---

## Folder Structure

ml/
├── asvspoof/
├── audio/
├── dataset/
│   ├── real/
│   └── fake/
├── model/
│   └── best_model.pth
├── train_pytorch.py
├── evaluate_pytorch.py
├── predict.py
├── inference.py
├── dataset.py
├── generate_spectrogram.py
└── api.py

---

## API Endpoint

POST /predict

Upload a WAV audio file.

Example Response

{
    "prediction": "FAKE AUDIO",
    "confidence": 100
}

---

## Technologies Used

- Python
- PyTorch
- FastAPI
- Librosa
- TorchVision
- NumPy
- Matplotlib

---

## Current Status

- Dataset Preparation ✅
- Spectrogram Generation ✅
- CNN Model Training ✅
- Model Evaluation ✅
- Prediction Pipeline ✅
- FastAPI Integration ✅
- Backend Integration (In Progress)
- RIR Feature Extraction (Planned)


## RIR Feature Extraction

Room Impulse Response (RIR) features are extracted from the uploaded audio using Librosa.

Files:
- rir.py
- test_rir.py
- visualize_rir.py

Output:
- Normalized RIR feature vector
- RIR visualization (rir_plot.png)