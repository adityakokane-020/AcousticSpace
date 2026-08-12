import torch    
from ml.model import AcousticCNN
from backend.app.config import MODEL_PATH

model = AcousticCNN()
model.load_state_dict(
    torch.load( MODEL_PATH, map_location= torch.device("cpu") )
)
model.eval()
def predict_audio(features):
    with torch.no_grad():
        output = model(features)

        probabilities = torch.softmax(output,dim=1)

        confidence, predicted = torch.max(probabilities, dim=1)

    labels = ["Fake","Real"]

    return{
        "prediction": labels[predicted.item()],
        "confidence": round(confidence.item(), 4)

    }