import torch

from torch.utils.data import DataLoader
from ast_dataset import ASTDataset
from collate import collate_fn


print("Loading Dataset...")

dataset = ASTDataset(
    protocol_file="ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt",
    audio_folder="ml/asvspoof/ASVspoof2019_LA_train/flac"
)

print("Dataset Loaded")
print("Total Samples:", len(dataset))

loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True,
    collate_fn=collate_fn
)

print("DataLoader Ready")

sample = next(iter(loader))

print("\nInput Shape")
print(sample["input_values"].shape)

print("\nLabels")
print(sample["labels"])