import librosa

def load_audio(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)

    return{
        "sample rate": sample_rate,
        "duration": round(librosa.get_duration(y=audio, sr= sample_rate),2),
        "totaL_samples": len(audio)
    }