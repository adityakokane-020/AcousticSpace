import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay

# Load Features
df = pd.read_csv("ml/features.csv")

# Convert labels
df["label"] = df["label"].map({
    "bonafide": 0,
    "spoof": 1
})

# Features & Labels
X = df.drop("label", axis=1)
y = df["label"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Load Model
model = joblib.load("ml/model/deepfake_detector.pkl")

# Plot Confusion Matrix
ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test,
    display_labels=["Real", "Fake"],
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.tight_layout()

plt.savefig("ml/confusion_matrix.png", dpi=300)

plt.show()

print("✅ Confusion Matrix Saved Successfully!")