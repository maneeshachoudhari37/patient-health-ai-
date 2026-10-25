import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load patient data
data = pd.read_csv("patient_data.csv")

# Input features
X = data[
    [
        "Age",
        "Heart_Rate",
        "SpO2",
        "Temperature",
        "Systolic_BP",
        "Diastolic_BP"
    ]
]

# Target
y = data["Risk_Level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)

print("Model trained successfully!")
print("Accuracy:", accuracy)

# Save model
with open("patient_risk_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")

