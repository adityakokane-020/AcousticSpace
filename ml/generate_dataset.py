import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve

# Paths
protocol_file = "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"
audio_folder = "ml/asvspoof/ASVspoof2019_LA_train/flac"

real_folder = "ml/dataset/real"
fake_folder = "ml/dataset/fake"

os.makedirs(real_folder, exist_ok=True)
os.makedirs(fake_folder, exist_ok=True)

count = 0

with open(protocol_file, "r") as file:

    for line in file:

        parts = line.strip().split()

        audio_id = parts[1]
        label = parts[-1]

        print(parts)
        print("Label:", label)

        # Print label for checking
        print(audio_id, "->", label)

        audio_path = os.path.join(audio_folder, audio_id + ".flac")

        if not os.path.exists(audio_path):
            continue

        y, sr = librosa.load(audio_path, sr=16000)

        rir = np.zeros(4000)
        rir[0] = 1.0

        for i in range(1, len(rir)):
            rir[i] = 0.9 ** i
            
        # Apply RIR to the audio
        y = convolve(y, rir, mode="full")
        # Keep the original audio length
        y = y[:len(y)]

        mel = librosa.feature.melspectrogram(
            y=y,
            sr=sr,
            n_mels=128
        )

        mel_db = librosa.power_to_db(mel, ref=np.max)

        if label == "bonafide":
            save_path = os.path.join(real_folder, audio_id + ".png")
        else:
            save_path = os.path.join(fake_folder, audio_id + ".png")

        plt.figure(figsize=(4, 4))
        librosa.display.specshow(mel_db, sr=sr)
        plt.axis("off")
        plt.savefig(save_path, bbox_inches="tight", pad_inches=0)
        plt.close()

        count += 1

        # Test only first 20 files
        #if count == 20:
         #   break

print("\nDone!")