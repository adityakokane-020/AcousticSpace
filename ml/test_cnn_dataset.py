from cnn_dataset import CNNDataset
from torch.utils.data import DataLoader

dataset = CNNDataset("ml/spectrograms")

loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)

images, labels = next(iter(loader))

print("Total Samples :", len(dataset))
print("Image Shape :", images.shape)
print("Labels :", labels)