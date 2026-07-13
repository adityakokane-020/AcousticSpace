import librosa

def load_audio(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)

    return{
        "sample rate": sample_rate,
        "duration": librosa.get_duration(y=audio, sr= sample_rate)
    }