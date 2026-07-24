import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Input audio
audio_file = "ml/audio/Recording.wav"

# Output folder
output_folder = "ml/spectrograms"
os.makedirs(output_folder, exist_ok=True)

# Load audio
y, sr = librosa.load(audio_file, sr=16000)

# Create Mel Spectrogram
mel = librosa.feature.melspectrogram(
    y=y,
    sr=sr,
    n_mels=128
)

mel_db = librosa.power_to_db(mel, ref=np.max)

# Save Image
plt.figure(figsize=(6, 6))
librosa.display.specshow(mel_db, sr=sr, x_axis="time", y_axis="mel")
plt.colorbar(format="%+2.0f dB")

save_path = os.path.join(output_folder, "Recording.png")
plt.savefig(save_path)
plt.close()

print("Spectrogram Saved:", save_path)