import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression


MODEL_FILE = "model.pkl"
SCALER_FILE = "scaler.pkl"
ENCODER_FILE = "encoder.pkl"

if os.path.exists(MODEL_FILE) and os.path.exists(SCALER_FILE) and os.path.exists(ENCODER_FILE):
    print("Loading pre-trained model, scaler, and encoder...")
    model = joblib.load(MODEL_FILE)
    scaler = joblib.load(SCALER_FILE)
    encoder = joblib.load(ENCODER_FILE)
else:
    print("Training new model on dataset.csv...")
    df = pd.read_csv("dataset.csv")
    X = df.drop("RiskLevel", axis=1)
    y = df["RiskLevel"]

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)
    joblib.dump(encoder, ENCODER_FILE)

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        age = float(data.get("age", 0))
        sbp = float(data.get("sbp", 0))
        dbp = float(data.get("dbp", 0))
        bs = float(data.get("bs", 0))
        temp = float(data.get("temp", 0))
        hr = float(data.get("hr", 0))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid numeric input"}), 400

    if age < 18:
        return jsonify({"error": "Age must be 18 or older."}), 400

    newdata = pd.DataFrame({
        "Age": [age],
        "SystolicBP": [sbp],
        "DiastolicBP": [dbp],
        "BS": [bs],
        "BodyTemp": [temp],
        "HeartRate": [hr]
    })

    scaled_data = scaler.transform(newdata)
    prediction = model.predict(scaled_data)
    probabilities = model.predict_proba(scaled_data)[0]
    confidence = float(max(probabilities))

    risk = encoder.inverse_transform(prediction)[0]

    return jsonify({
        "risk": risk,
        "confidence": confidence
    })

if __name__ == "__main__":
    print("Starting SafeMother server at http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
