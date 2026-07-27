import os
import librosa
import torch

from torch.utils.data import Dataset
from transformers import ASTFeatureExtractor


class ASTDataset(Dataset):

    def __init__(self, protocol_file, audio_folder):

        self.feature_extractor = ASTFeatureExtractor.from_pretrained(
            "MIT/ast-finetuned-audioset-10-10-0.4593"
        )

        self.samples = []

        with open(protocol_file, "r") as file:

            for line in file:

                parts = line.strip().split()

                audio_name = parts[1]

                label = 0 if parts[-1] == "bonafide" else 1

                audio_path = os.path.join(
                    audio_folder,
                    audio_name + ".flac"
                )

                if os.path.exists(audio_path):

                    self.samples.append((audio_path, label))

    def __len__(self):

        return len(self.samples)

    def __getitem__(self, index):

        audio_path, label = self.samples[index]

        audio, sr = librosa.load(audio_path, sr=16000)

        inputs = self.feature_extractor(
            audio,
            sampling_rate=16000,
            return_tensors="pt"
        )

        return {
            "input_values": inputs["input_values"].squeeze(0),
            "label": torch.tensor(label)
        }