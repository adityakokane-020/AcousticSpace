import pandas as pd
import librosa
import numpy as np

# Load dataset
df = pd.read_csv("ml/dataset.csv")

features = []

print("Processing Audio Files...")

for index, row in df.iterrows():

    try:
        audio, sr = librosa.load(row["audio_path"], sr=16000)

        # MFCC
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        mfcc_mean = np.mean(mfcc, axis=1)

        # Zero Crossing Rate
        zcr = librosa.feature.zero_crossing_rate(audio)
        zcr_mean = np.mean(zcr)

        # Spectral Centroid
        centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)
        centroid_mean = np.mean(centroid)

        # Chroma
        chroma = librosa.feature.chroma_stft(y=audio, sr=sr)
        chroma_mean = np.mean(chroma)

        row_data = list(mfcc_mean)
        row_data.append(zcr_mean)
        row_data.append(centroid_mean)
        row_data.append(chroma_mean)
        row_data.append(row["label"])

        features.append(row_data)

        if (index + 1) % 100 == 0:
            print(f"{index+1} files processed...")

    except Exception as e:
        print("Skipped:", row["audio_path"])

columns = [f"mfcc_{i+1}" for i in range(13)]
columns += [
    "zcr",
    "spectral_centroid",
    "chroma",
    "label"
]

feature_df = pd.DataFrame(features, columns=columns)

feature_df.to_csv("ml/features.csv", index=False)

print("\n===================================")
print("Feature Extraction Completed!")
print("Total Samples :", len(feature_df))
print("Saved : ml/features.csv")
print("===================================")