import torch


def get_device():

    if torch.cuda.is_available():

        return torch.device("cuda")

    return torch.device("cpu")


def count_parameters(model):

    return sum(

        p.numel()

        for p in model.parameters()

        if p.requires_grad

    )