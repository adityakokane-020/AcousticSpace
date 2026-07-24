import os
import torch
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from torchvision import transforms
from ml.model import AcousticCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AcousticCNN().to(device)
model.load_state_dict(torch.load("ml/model/best_model.pth", map_location=device))
model.eval()


def predict_audio(audio_file):

    os.makedirs("ml/temp", exist_ok=True)

    y, sr = librosa.load(audio_file, sr=16000)

    mel = librosa.feature.melspectrogram(
        y=y,
        sr=sr,
        n_mels=128
    )

    mel_db = librosa.power_to_db(mel, ref=np.max)

    image_path = "ml/temp/test.png"

    plt.figure(figsize=(4, 4))
    librosa.display.specshow(mel_db, sr=sr)
    plt.axis("off")
    plt.savefig(image_path, bbox_inches="tight", pad_inches=0)
    plt.close()

    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])

    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(output, dim=1)

        confidence = torch.max(probabilities).item() * 100

        prediction = torch.argmax(probabilities, dim=1).item()

    if prediction == 0:
        result = "FAKE AUDIO"
    else:
        result = "REAL AUDIO"

    return {
        "prediction": result,
        "confidence": round(confidence, 2)
    }