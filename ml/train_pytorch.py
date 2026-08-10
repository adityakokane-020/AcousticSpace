import os
import torch
import torch.nn as nn
import torch.optim as optim


from torch.utils.data import DataLoader, random_split

from cnn_dataset import CNNDataset
from model import AcousticCNN

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



# Dataset
dataset = CNNDataset(
    "ml/spectrograms"
)

# Split
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size

train_dataset, test_dataset = random_split(
    dataset,
    [train_size, test_size]
)

# DataLoader
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=32,
    shuffle=False
)

# Model
model = AcousticCNN().to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 1

print("Training Started...\n")

for epoch in range(epochs):

    model.train()

    running_loss = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    print(
    f"Epoch {epoch+1}/{epochs}  Loss : {running_loss/len(train_loader):.4f}"
)

os.makedirs("ml/model", exist_ok=True)

torch.save(
    model.state_dict(),
    "ml/model/cnn_best_model.pth"
)

print("\nModel Saved Successfully!")