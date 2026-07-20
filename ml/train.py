import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Load Features
df = pd.read_csv("ml/features.csv")

# Convert labels
df["label"] = df["label"].map({
    "bonafide": 0,
    "spoof": 1
})

# Features and Labels
X = df.drop("label", axis=1)
y = df["label"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("\nAccuracy :", accuracy_score(y_test, prediction))

print("\nClassification Report\n")
print(classification_report(y_test, prediction))

# Create model folder if needed
os.makedirs("ml/model", exist_ok=True)

joblib.dump(model, "ml/model/deepfake_detector.pkl")

print("\n✅ Model Saved Successfully!")