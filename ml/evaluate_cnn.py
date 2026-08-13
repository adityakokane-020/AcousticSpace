import torch

from torch.utils.data import DataLoader
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from cnn_dataset import CNNDataset
from model import AcousticCNN

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Dataset
dataset = CNNDataset("ml/spectrograms")

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=False
)

# Model
model = AcousticCNN()

model.load_state_dict(
    torch.load(
        "ml/model/cnn_best_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()

true_labels = []
predicted_labels = []

with torch.no_grad():

    for images, labels in loader:

        images = images.to(device)

        outputs = model(images)

        predictions = torch.argmax(outputs, dim=1).cpu()

        predicted_labels.extend(
            predictions.numpy()
        )

        true_labels.extend(
            labels.numpy()
        )

print("\n========== CNN Evaluation ==========\n")

print(
    "Accuracy :",
    accuracy_score(
        true_labels,
        predicted_labels
    )
)

print(
    "Precision :",
    precision_score(
        true_labels,
        predicted_labels,
        zero_division=0
    )
)

print(
    "Recall :",
    recall_score(
        true_labels,
        predicted_labels,
        zero_division=0
    )
)

print(
    "F1 Score :",
    f1_score(
        true_labels,
        predicted_labels,
        zero_division=0
    )
)

print("\nConfusion Matrix\n")

print(
    confusion_matrix(
        true_labels,
        predicted_labels
    )
)

print("\nClassification Report\n")

print(
    classification_report(
        true_labels,
        predicted_labels,
        target_names=["Real", "Fake"],
        zero_division=0
    )
)