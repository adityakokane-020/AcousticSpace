import librosa
import numpy as np

def load_audio(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)
    return{
        "sample rate": sample_rate,
        "duration": round(librosa.get_duration(y=audio, sr= sample_rate),2),
        "totaL_samples": len(audio)
    }

def extract_spectrogram(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)
    stft = librosa.stft(audio)
    spectrogram = librosa.amplitude_to_db(np.abs(stft), ref = np.max)
    return {
        "spectrogram_shape": spectrogram.shape
    }