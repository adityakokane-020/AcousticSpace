import torch
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    
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

    labels = ["Real","Fake"]

    return{
        "prediction": labels[predicted.item()],
        "confidence": round(confidence.item(), 4)

    }