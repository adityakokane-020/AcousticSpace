import os

# Protocol file
protocol_file = "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"

# Audio folder
audio_folder = "ml/asvspoof/ASVspoof2019_LA_train/flac"

count = 0

with open(protocol_file, "r") as file:
    for line in file:

        parts = line.strip().split()

        audio_id = parts[1]
        label = parts[-1]

        audio_path = os.path.join(audio_folder, audio_id + ".flac")

        if os.path.exists(audio_path):

            print(audio_path, "->", label)

            count += 1

        if count == 10:
            break

print("\nDone!")