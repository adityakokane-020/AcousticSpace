import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("ml/model/deepfake_detector.pkl")

# Load feature names
df = pd.read_csv("ml/features.csv")

feature_names = df.drop("label", axis=1).columns

# Feature Importance
importance = model.feature_importances_

# Create DataFrame
feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

# Sort
feature_df = feature_df.sort_values(by="Importance", ascending=False)

print(feature_df)

# Plot
plt.figure(figsize=(12,6))
plt.bar(feature_df["Feature"], feature_df["Importance"])
plt.xticks(rotation=90)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()

plt.savefig("ml/feature_importance.png", dpi=300)

plt.show()

print("\n✅ Feature Importance graph saved!")
print("Location : ml/feature_importance.png")