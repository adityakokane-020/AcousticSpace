from ast_dataset import ASTDataset
from torch.utils.data import DataLoader


dataset = ASTDataset(
    "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt",
    "ml/asvspoof/ASVspoof2019_LA_train/flac"
)


print("Total Samples:", len(dataset))


loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)


batch = next(iter(loader))


print("Input Shape:", batch["input_values"].shape)
print("Labels:", batch["labels"])