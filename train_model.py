import pandas as pd # pyright: ignore[reportMissingModuleSource]
from sklearn.model_selection import train_test_split # pyright: ignore[reportMissingModuleSource]
from sklearn.ensemble import RandomForestRegressor # pyright: ignore[reportMissingModuleSource]
import joblib # pyright: ignore[reportMissingImports]

# Load data
df = pd.read_csv("student_data.csv")

# ✅ Updated Features (NOW includes G1, G2)
X = df[[
    "age", "absences", "failures", "studytime",
    "goout", "health", "freetime",
    "traveltime", "Walc", "Fedu",
    "G1", "G2"
]]

# Target
y = df["G3"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔥 Stronger model
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f"Model R² Score: {score:.2f}")

# Save
joblib.dump(model, "student_model.pkl")

print("✅ Model trained and saved!")
