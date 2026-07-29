import joblib
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory

<<<<<<< HEAD
=======

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

>>>>>>> 4b9fee29f06bb0bb80544f6c041b0c7f102330bb
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
