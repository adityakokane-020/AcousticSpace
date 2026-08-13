import torch
from torch.utils.data import DataLoader

from transformers import ASTForAudioClassification

from ast_dataset import ASTDataset
from collate import collate_fn

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ---------------- DATASET ----------------

dataset = ASTDataset(
    protocol_file="ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt",
    audio_folder="ml/asvspoof/ASVspoof2019_LA_train/flac"
)

# Quick testing
dataset.samples = dataset.samples[:200]

loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=False,
    collate_fn=collate_fn
)

# ---------------- MODEL ----------------

device = torch.device("cpu")

model = ASTForAudioClassification.from_pretrained(
    "MIT/ast-finetuned-audioset-10-10-0.4593",
    num_labels=2,
    ignore_mismatched_sizes=True
)

model.load_state_dict(
    torch.load(
        "ml/model/ast_best_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()

# ---------------- EVALUATION ----------------

all_labels = []
all_predictions = []

with torch.no_grad():

    for batch in loader:

        input_values = batch["input_values"].to(device)
        labels = batch["labels"].to(device)

        outputs = model(input_values=input_values)

        predictions = torch.argmax(outputs.logits, dim=1)

        all_labels.extend(labels.cpu().numpy())
        all_predictions.extend(predictions.cpu().numpy())

# ---------------- RESULTS ----------------

print("\n========== Evaluation ==========\n")

print("Accuracy :", accuracy_score(all_labels, all_predictions))

print("Precision :", precision_score(all_labels, all_predictions))

print("Recall :", recall_score(all_labels, all_predictions))

print("F1 Score :", f1_score(all_labels, all_predictions))

print("\nConfusion Matrix\n")

print(
    confusion_matrix(
        all_labels,
        all_predictions,
        labels=[0, 1]
    )
)

print("\nClassification Report\n")

print(
    classification_report(
        all_labels,
        all_predictions,
        labels=[0, 1],
        target_names=["Real", "Fake"],
        zero_division=0
    )
)