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

image_path = input("Enter Spectrogram Image Path: ")

image = Image.open(image_path)
image = transform(image)
image = image.unsqueeze(0).to(device)

with torch.no_grad():

    outputs = model(image)

    probabilities = torch.softmax(outputs, dim=1)

    prediction = torch.argmax(probabilities, dim=1).item()

confidence = probabilities[0][prediction].item() * 100

print("\n==============================")

if prediction == 0:
    print("Prediction : REAL")
else:
    print("Prediction : FAKE")

print(f"Confidence : {confidence:.2f}%")

print("==============================")