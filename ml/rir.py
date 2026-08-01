import librosa
import numpy as np


def extract_rir(audio_path):

    y, sr = librosa.load(audio_path, sr=16000)

    # Short-Time Fourier Transform
    stft = librosa.stft(y)

    magnitude = np.abs(stft)

    # Estimate reverberation energy
    rir_energy = np.mean(magnitude, axis=1)

    # Normalize
    rir_energy = rir_energy / np.max(rir_energy)

    return rir_energy