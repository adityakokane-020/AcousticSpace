import os

protocol = "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"

dataset = []

with open(protocol, "r") as file:

    for line in file:

        parts = line.strip().split()

        audio_name = parts[1]

        label = parts[-1]

        label = 0 if label == "bonafide" else 1

        path = f"ml/asvspoof/ASVspoof2019_LA_train/flac/{audio_name}.flac"

        if os.path.exists(path):

            dataset.append((path, label))

print("Total Samples :", len(dataset))

print()

print("First Sample")

print(dataset[0])

print()

print("Last Sample")

print(dataset[-1])