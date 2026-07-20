import librosa
import librosa.display
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Audio file path
audio_path = "ml/audio/Recording.wav"

try:
    # Load audio
    audio, sample_rate = librosa.load(audio_path, sr=None)

    print("✅ Audio Loaded Successfully!")
    print(f"Sample Rate : {sample_rate}")
    print(f"Duration : {len(audio) / sample_rate:.2f} seconds")

    # Plot Waveform
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(audio, sr=sample_rate)

    plt.title("Audio Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("❌ Error: Audio file not found.")
except Exception as e:
    print("❌ Error:", e)

# -----------------------------
# Spectrogram
# -----------------------------

# Short-Time Fourier Transform (STFT)
stft = librosa.stft(audio)

# Convert amplitude to decibel scale
spectrogram = librosa.amplitude_to_db(abs(stft), ref=np.max)
plt.figure(figsize=(14,5))

librosa.display.specshow(
    spectrogram,
    sr=sample_rate,
    x_axis='time',
    y_axis='log'
)

plt.colorbar(format='%+2.0f dB')

plt.title("Audio Spectrogram")

plt.tight_layout()

plt.show()

# -----------------------------
# MFCC Feature Extraction
# -----------------------------

mfcc = librosa.feature.mfcc(
    y=audio,
    sr=sample_rate,
    n_mfcc=13
)

print("\n========== MFCC ==========")
print("MFCC Shape :", mfcc.shape)

plt.figure(figsize=(14,5))

librosa.display.specshow(
    mfcc,
    x_axis="time",
    sr=sample_rate
)

plt.colorbar()
plt.title("MFCC Features")

plt.tight_layout()
plt.show()

# -----------------------------
# Zero Crossing Rate
# -----------------------------

zcr = librosa.feature.zero_crossing_rate(audio)

print("\n========== Zero Crossing Rate ==========")
print("ZCR Shape :", zcr.shape)
print("Average ZCR :", zcr.mean())

plt.figure(figsize=(14,3))

plt.plot(zcr[0])

plt.title("Zero Crossing Rate")
plt.xlabel("Frame")
plt.ylabel("ZCR")

plt.tight_layout()
plt.show()

# -----------------------------
# Spectral Centroid
# -----------------------------

centroid = librosa.feature.spectral_centroid(
    y=audio,
    sr=sample_rate
)

print("\n========== Spectral Centroid ==========")
print("Shape :", centroid.shape)
print("Average :", centroid.mean())

plt.figure(figsize=(14,3))

plt.plot(centroid[0])

plt.title("Spectral Centroid")
plt.xlabel("Frame")
plt.ylabel("Hz")

plt.tight_layout()
plt.show()

# -----------------------------
# Chroma Features
# -----------------------------

chroma = librosa.feature.chroma_stft(
    y=audio,
    sr=sample_rate
)

print("\n========== Chroma ==========")
print("Shape :", chroma.shape)

plt.figure(figsize=(14,4))

librosa.display.specshow(
    chroma,
    x_axis='time',
    y_axis='chroma'
)

plt.colorbar()

plt.title("Chroma Features")

plt.tight_layout()

plt.show()

# -----------------------------
# Feature Vector
# -----------------------------

feature_vector = {
    "MFCC Mean": mfcc.mean(),
    "Zero Crossing Rate": zcr.mean(),
    "Spectral Centroid": centroid.mean(),
    "Chroma Mean": chroma.mean()
}

print("\n========== Feature Vector ==========")

for key, value in feature_vector.items():
    print(f"{key} : {value:.4f}")

# -----------------------------
# Save Features to CSV
# -----------------------------

df = pd.DataFrame([feature_vector])

df.to_csv("ml/features.csv", index=False)

print("\n✅ Features saved successfully!")
print("Location : ml/features.csv")