import torch


def collate_fn(batch):

    input_values = torch.stack(
        [item["input_values"] for item in batch]
    )

    labels = torch.stack(
        [item["labels"] for item in batch]
    )

    return {
        "input_values": input_values,
        "labels": labels
    }