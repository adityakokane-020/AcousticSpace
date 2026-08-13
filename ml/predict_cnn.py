import os
import torch
from PIL import Image
from torchvision import transforms

from model import AcousticCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

model = AcousticCNN()

model.load_state_dict(
    torch.load(
        "ml/model/cnn_best_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()


def predict_cnn(image_path):

    if not os.path.exists(image_path):
        return {
            "error": "Image not found."
        }

    image = Image.open(image_path)

    image = transform(image)

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        prediction = torch.argmax(probabilities, dim=1).item()

    confidence = float(probabilities[0][prediction].item() * 100)

    label = "REAL" if prediction == 0 else "FAKE"

    return {

        "prediction": label,

        "confidence": round(confidence, 2)

    }


if __name__ == "__main__":

    image_path = input("Enter Spectrogram Image Path : ")

    result = predict_cnn(image_path)

    print("\n==============================")
    print("CNN Prediction")
    print("==============================")

    print(result)

    print("==============================")