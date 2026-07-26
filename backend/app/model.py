import torch
from ml.model import AcousticCNN

MODEL_PATH = "ml/model/best_model.pth"

model = AcousticCNN()
model.state_dict(
    torch.load( MODEL_PATH, map_location= torch.device("cpu") )
)
model.eval()
def predict_audio(features):
    with torch.no_grad():
        output = model(features)

        probabilities = torch.softmax(output,dim=1)

        confidence, predicted = torch.max(probabilities, dim=1)

    labels = ["Real","Fake"]

    return{
        "prediction": labels[predicted.item()],
        "confidence": labels[confidence.item(), 4]

    }