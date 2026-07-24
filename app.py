from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoder
model = joblib.load("decision_tree_mushroom (1).pkl")
encoder = joblib.load("mushroom_encoder (1).pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # MUST match HTML exactly (NOW 22 FEATURES)
        features = [
            "cap-shape",
            "cap-surface",
            "cap-color",
            "bruises",
            "odor",
            "gill-attachment",
            "gill-spacing",
            "gill-size",
            "gill-color",
            "stalk-shape",
            "stalk-root",
            "stalk-surface-above-ring",
            "stalk-surface-below-ring",
            "stalk-color-above-ring",
            "stalk-color-below-ring",
            "veil-type",
            "veil-color",
            "ring-number",
            "ring-type",   # ← YOU MISSED THIS
            "spore-print-color",
            "population",
            "habitat"
        ]

        input_data = [request.form[feat] for feat in features]

        input_array = np.array(input_data, dtype=object).reshape(1, -1)
        input_encoded = encoder.transform(input_array)

        prediction = model.predict(input_encoded)[0]
        result = "Edible 🍄" if prediction == 0 else "Poisonous ☠️"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
