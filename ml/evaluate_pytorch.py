import torch
from torchvision import transforms
from torch.utils.data import DataLoader, random_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from dataset import SpectrogramDataset
from model import AcousticCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

dataset = SpectrogramDataset(
    root_dir="ml/dataset",
    transform=transform
)

train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size

_, test_dataset = random_split(dataset, [train_size, test_size])

test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

model = AcousticCNN().to(device)
model.load_state_dict(torch.load("ml/model/best_model.pth", map_location=device))
model.eval()

y_true = []
y_pred = []

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        y_true.extend(labels.numpy())
        y_pred.extend(predicted.cpu().numpy())

print("\nAccuracy :", accuracy_score(y_true, y_pred))
print("\nConfusion Matrix")
print(confusion_matrix(y_true, y_pred))

print("\nClassification Report")
print(classification_report(y_true, y_pred))