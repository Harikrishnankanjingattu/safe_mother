# 🤰 Safe Mother - Maternal Health Risk Prediction

A Machine Learning project that predicts the maternal health risk level of pregnant women using health parameters such as blood pressure, blood sugar, body temperature, heart rate, and age.

---

## 📌 Project Overview

Safe Mother is a machine learning-based healthcare application that helps identify the maternal risk level of pregnant women.

The model predicts one of the following risk levels:

- 🟢 Low Risk
- 🟡 Mid Risk
- 🔴 High Risk

The project is built using **Python** and **Scikit-learn** with a Logistic Regression classifier.

---

## 🚀 Features

- Predict maternal health risk
- User-friendly console input
- Data preprocessing using StandardScaler
- Label encoding for categorical output
- Model evaluation using accuracy
- Save trained model using Joblib (.pkl)

---

## 📂 Dataset Features

| Feature | Description |
|----------|-------------|
| Age | Mother's Age |
| SystolicBP | Systolic Blood Pressure |
| DiastolicBP | Diastolic Blood Pressure |
| BS | Blood Sugar |
| BodyTemp | Body Temperature |
| HeartRate | Heart Rate |
| RiskLevel | Target Variable |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📊 Machine Learning Pipeline

1. Load Dataset
2. Data Preprocessing
3. Label Encoding
4. Train-Test Split
5. Feature Scaling
6. Logistic Regression Training
7. Model Evaluation
8. Risk Prediction
9. Save Model

---

## 📈 Model Performance

Algorithm:
- Logistic Regression

Accuracy:

*68.5%**

> Update this value if you retrain the model and obtain a different measured accuracy.

---

## 📁 Project Structure

```
safe_mother/
│
├── dataset.csv
├── main.py
├── maternal_risk_model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── README.md
└── requirements.txt
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/safe_mother.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 💻 Example Input

```
Age: 30
Systolic Blood Pressure: 130
Diastolic Blood Pressure: 80
Blood Sugar: 7.2
Body Temperature: 98.6
Heart Rate: 72
```

Example Output

```
Predicted Risk Level:
LOW RISK
```

---

## 🔮 Future Improvements

- Flask/FastAPI REST API
- React Frontend
- User Authentication
- Risk History
- PDF Report Generation
- Cloud Deployment
- Improved model using Random Forest or XGBoost

---

## 👨‍💻 Author

Harikrishnan K

Machine Learning | Backend Development | AI Enthusiast

---

## 📜 License

This project is licensed under the MIT License.
