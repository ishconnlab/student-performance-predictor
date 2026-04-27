from flask import Flask, render_template, request # pyright: ignore[reportMissingImports]
import joblib # pyright: ignore[reportMissingImports]
import pandas as pd # pyright: ignore[reportMissingModuleSource]

app = Flask(__name__)

# Load trained model
model = joblib.load("student_model.pkl")

#  Updated feature order (NOW includes G1, G2)
FEATURE_ORDER = [
    "age", "absences", "failures", "studytime",
    "goout", "health", "freetime",
    "traveltime", "Walc", "Fedu",
    "G1", "G2"
]

# Helper function for safe input
def get_float(form, name):
    value = form.get(name)
    if value is None or value.strip() == "":
        raise ValueError(f"{name} is required")
    return float(value)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        #  Collect inputs (NOW includes G1, G2)
        data = {
            "age": get_float(request.form, "age"),
            "absences": get_float(request.form, "absences"),
            "failures": get_float(request.form, "failures"),
            "studytime": get_float(request.form, "studytime"),
            "goout": get_float(request.form, "goout"),
            "health": get_float(request.form, "health"),
            "freetime": get_float(request.form, "freetime"),
            "traveltime": get_float(request.form, "traveltime"),
            "Walc": get_float(request.form, "Walc"),
            "Fedu": get_float(request.form, "Fedu"),
            "G1": get_float(request.form, "G1"),
            "G2": get_float(request.form, "G2"),
        }

        #  Debug logs (optional)
        print("INPUT:", data)

        # Convert to DataFrame
        df = pd.DataFrame([data])[FEATURE_ORDER]

        print("DF:\n", df)

        # Predict
        prediction = model.predict(df)[0]

        print("RAW PREDICTION:", prediction)

        # Clamp result (0–20)
        prediction = max(0, min(20, prediction))

        #  Status classification
        if prediction >= 15:
            status = "Excellent 🎉"
        elif prediction >= 10:
            status = "Average 👍"
        else:
            status = "Needs Improvement ⚠️"

        #  Smarter tips (based on both behavior + grades)
        tips = []

        if data["G1"] < 10 or data["G2"] < 10:
            tips.append("Improve your earlier test scores (G1, G2).")

        if data["failures"] > 0:
            tips.append("Avoid failures—they strongly affect final grade.")

        if data["studytime"] < 3:
            tips.append("Increase your study time.")

        if data["absences"] > 5:
            tips.append("Reduce absences.")

        if data["goout"] > 3 or data["Walc"] > 3:
            tips.append("Reduce social and alcohol activities.")

        if not tips:
            tips.append("Great performance! Keep maintaining your habits.")

        tip_text = " ".join(tips)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Grade: {round(prediction, 2)} ({status})",
            tip_text=tip_text
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)
