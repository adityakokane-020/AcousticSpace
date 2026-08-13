import os
import pandas as pd

# Paths
TRAIN_AUDIO_FOLDER = "ml/asvspoof/ASVspoof2019_LA_train/flac"
PROTOCOL_FILE = "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"

dataset = []

with open(PROTOCOL_FILE, "r") as file:
    for line in file:
        parts = line.strip().split()

        speaker_id = parts[0]
        file_name = parts[1]
        system_id = parts[3]
        label = parts[4]

        audio_path = os.path.join(TRAIN_AUDIO_FOLDER, file_name + ".flac")

        if os.path.exists(audio_path):
            dataset.append({
                "audio_path": audio_path,
                "speaker_id": speaker_id,
                "system_id": system_id,
                "label": label
            })

df = pd.DataFrame(dataset)

df.to_csv("ml/dataset.csv", index=False)

print("===================================")
print("Dataset Created Successfully")
print("===================================")
print(df.head())
print("\nTotal Audio Files :", len(df))