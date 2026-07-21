import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

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

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Searching Best Parameters...")

# Parameter Grid
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [10, 20, None],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

# Grid Search
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

# Prediction
y_pred = best_model.predict(X_test)

print("\n========== BEST PARAMETERS ==========")
print(grid_search.best_params_)

print("\n========== ACCURACY ==========")
print(f"{accuracy_score(y_test, y_pred):.4f}")

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(y_test, y_pred))

# Save Optimized Model
joblib.dump(best_model, "ml/model/deepfake_detector_optimized.pkl")

print("\n✅ Optimized Model Saved Successfully!")