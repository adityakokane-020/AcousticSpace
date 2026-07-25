import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc

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

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Load Model
model = joblib.load("ml/model/deepfake_detector.pkl")

# Probability Prediction
y_prob = model.predict_proba(X_test)[:, 1]

# ROC
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# Plot
plt.figure(figsize=(7,6))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.4f}")
plt.plot([0,1], [0,1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()

plt.tight_layout()

plt.savefig("ml/roc_curve.png", dpi=300)

plt.show()

print(f"\nAUC Score : {roc_auc:.4f}")
print("✅ ROC Curve Saved Successfully!")