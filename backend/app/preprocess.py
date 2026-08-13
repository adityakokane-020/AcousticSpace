import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import torch
from PIL import Image
from torchvision import transforms
from scipy.signal import convolve

def load_audio(audio, sample_rate):
    # audio, sample_rate = librosa.load(file_path, sr=None)
    return{
        "sample rate": sample_rate,
        "duration": round(librosa.get_duration(y=audio, sr= sample_rate),2),
        "total_samples": len(audio)
    }

def extract_spectrogram(audio, sample_rate):
    # audio, sample_rate = librosa.load(file_path, sr=16000)

    rir = np.zeros(4000)
    rir[0] = 1.0

    for i in range(1, len(rir)):
        rir[i] = 0.9 ** i

    audio = convolve(audio, rir, mode="full")
    audio = audio[:len(audio)]

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate,
        n_mels=128,
    )

    mel_db = librosa.power_to_db(mel, ref = np.max)

    temp_path ="uploads/temp.png"
    plt.figure(figsize = (4,4))
    librosa.display.specshow(mel_db, sr=sample_rate)
    plt.axis("off")
    plt.savefig(temp_path, bbox_inches ="tight", pad_inches= 0)
    plt.close()

    image = Image.open(temp_path).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((128,128)),
        transforms.ToTensor()
    ])

    tensor = transform(image)

    tensor = tensor.unsqueeze(0)

    return tensor