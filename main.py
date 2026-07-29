import joblib
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

# Load pre-trained model artifacts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Extract input values sent from index.html
    age = float(data.get("age", 0))
    sbp = float(data.get("sbp", 0))
    dbp = float(data.get("dbp", 0))
    bs = float(data.get("bs", 0))
    temp = float(data.get("temp", 0))
    hr = float(data.get("hr", 0))

    if age < 18:
        return jsonify({"error": "Age must be 18 or older."}), 400

    # Format input into Pandas DataFrame matching model features
    user_data = pd.DataFrame([{
        "Age": age,
        "SystolicBP": sbp,
        "DiastolicBP": dbp,
        "BS": bs,
        "BodyTemp": temp,
        "HeartRate": hr
    }])

    # Scale inputs and predict risk level
    scaled_data = scaler.transform(user_data)
    prediction = model.predict(scaled_data)
    risk_label = encoder.inverse_transform(prediction)[0]

    return jsonify({"risk": risk_label})

if __name__ == "__main__":
    app.run(debug=True)
