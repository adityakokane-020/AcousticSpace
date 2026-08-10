import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Protocol File
protocol_file = "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"

# Audio Folder
audio_folder = "ml/asvspoof/ASVspoof2019_LA_train/flac"

# Output Folders
real_folder = "ml/spectrograms/real"
fake_folder = "ml/spectrograms/fake"

os.makedirs(real_folder, exist_ok=True)
os.makedirs(fake_folder, exist_ok=True)

count = 0

with open(protocol_file, "r") as file:

    for line in file:

        parts = line.strip().split()

        audio_name = parts[1]
        label = parts[-1]

        audio_path = os.path.join(
            audio_folder,
            audio_name + ".flac"
        )

        if not os.path.exists(audio_path):
            continue

        # Load Audio
        audio, sr = librosa.load(audio_path, sr=16000)

        # Create Mel Spectrogram
        mel = librosa.feature.melspectrogram(
            y=audio,
            sr=sr,
            n_mels=128
        )

        mel_db = librosa.power_to_db(
            mel,
            ref=np.max
        )

        # Save Path
        if label == "bonafide":
            save_path = os.path.join(
                real_folder,
                audio_name + ".png"
            )
        else:
            save_path = os.path.join(
                fake_folder,
                audio_name + ".png"
            )

        # Plot
        plt.figure(figsize=(3, 3))

        librosa.display.specshow(
            mel_db,
            sr=sr,
            cmap="viridis"
        )

        plt.axis("off")

        plt.savefig(
            save_path,
            bbox_inches="tight",
            pad_inches=0
        )

        plt.close()

        count += 1

        if count % 100 == 0:
            print(f"{count} Spectrograms Created")

        
print("\n==============================")
print("Generation Completed")
print("Total Spectrograms :", count)
print("==============================")