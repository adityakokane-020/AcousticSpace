import os
from PIL import Image
from torch.utils.data import Dataset

class SpectrogramDataset(Dataset):

    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = []
        self.labels = []

        classes = ["fake", "real"]

        for label, folder in enumerate(classes):
            folder_path = os.path.join(root_dir, folder)

            if not os.path.exists(folder_path):
                continue

            for file in os.listdir(folder_path):
                if file.endswith(".png"):
                    self.images.append(os.path.join(folder_path, file))
                    self.labels.append(label)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):

        image = Image.open(self.images[index]).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, self.labels[index]