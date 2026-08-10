import os
import torch
import librosa

from transformers import (
    ASTFeatureExtractor,
    ASTForAudioClassification
)

device = torch.device("cpu")

feature_extractor = ASTFeatureExtractor.from_pretrained(
    "MIT/ast-finetuned-audioset-10-10-0.4593"
)

model = ASTForAudioClassification.from_pretrained(
    "MIT/ast-finetuned-audioset-10-10-0.4593",
    num_labels=2,
    ignore_mismatched_sizes=True
)

model.load_state_dict(
    torch.load(
        "ml/model/ast_best_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()


def predict_ast(audio_path):

    if not os.path.exists(audio_path):
        return {
            "error": "Audio file not found."
        }

    audio, sr = librosa.load(audio_path, sr=16000)

    inputs = feature_extractor(
        audio,
        sampling_rate=16000,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model(
            input_values=inputs["input_values"].to(device)
        )

        probabilities = torch.softmax(outputs.logits, dim=1)

        prediction = torch.argmax(probabilities, dim=1).item()

    confidence = float(probabilities[0][prediction].item() * 100)

    label = "REAL" if prediction == 0 else "FAKE"

    return {

        "prediction": label,

        "confidence": round(confidence, 2)

    }


if __name__ == "__main__":

    audio_path = input("Enter Audio Path : ")

    result = predict_ast(audio_path)

    print("\n==============================")
    print("AST Prediction")
    print("==============================")

    print(result)

    print("==============================")