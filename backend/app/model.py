import torch
from ml.model import AcousticCNN

MODEL_PATH = "ml/model/best_model.pth"

model = AcousticCNN()
model.state_dict(
    model.load( MODEL_PATH, map_location= torch.device("cpu") )
)
model.eval()
def predict_audio(features):
    #ml model details
    return{
        "prediction": "model loaded successfully",
        "confidence": None

    }