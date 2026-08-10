import os
import librosa
import numpy as np
import pandas as pd

# Dataset Paths
protocol_file = "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"
audio_folder = "ml/asvspoof/ASVspoof2019_LA_train/flac"

# Output
output_csv = "ml/features_rir.csv"

features = []

print("Generating RIR Features...\n")

with open(protocol_file, "r") as file:

    for line in file:

        parts = line.strip().split()

        audio_id = parts[1]
        label = 0 if parts[-1] == "bonafide" else 1

        audio_path = os.path.join(audio_folder, audio_id + ".flac")

        if not os.path.exists(audio_path):
            continue

        try:

            y, sr = librosa.load(audio_path, sr=16000)

            rir = np.abs(np.fft.ifft(np.log(np.abs(np.fft.fft(y)) + 1e-6)))

            rir = rir[:1024]

            row = rir.tolist()
            row.append(label)

            features.append(row)

            if len(features) % 100 == 0:
                print(f"Processed : {len(features)}")

        except Exception as e:

            print(audio_id, e)

columns = [f"rir_{i}" for i in range(1024)]
columns.append("label")

df = pd.DataFrame(features, columns=columns)

df.to_csv(output_csv, index=False)

print("\n====================")
print("RIR Dataset Created")
print("====================")
print("Total Samples :", len(df))
print("Saved :", output_csv)