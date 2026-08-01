import os
from PIL import Image

import torch
from torch.utils.data import Dataset

from torchvision import transforms


class CNNDataset(Dataset):

    def __init__(self, root_folder):

        self.samples = []

        self.transform = transforms.Compose([
            transforms.Grayscale(num_output_channels=1),
            transforms.Resize((128, 128)),
            transforms.ToTensor()
        ])

        real_folder = os.path.join(root_folder, "real")
        fake_folder = os.path.join(root_folder, "fake")

        # Real Images
        for image in os.listdir(real_folder):

            if image.endswith(".png"):

                self.samples.append(
                    (
                        os.path.join(real_folder, image),
                        0
                    )
                )

        # Fake Images
        for image in os.listdir(fake_folder):

            if image.endswith(".png"):

                self.samples.append(
                    (
                        os.path.join(fake_folder, image),
                        1
                    )
                )

    def __len__(self):

        return len(self.samples)

    def __getitem__(self, index):

        image_path, label = self.samples[index]

        image = Image.open(image_path)

        image = self.transform(image)

        return image, torch.tensor(label, dtype=torch.long)