<p align="center">
  <img src="https://raw.githubusercontent.com/Harikrishnankanjingattu/safe_mother/main/safe.png" alt="Safe Mother Banner" width="100%">
</p>

<h1 align="center">🤰 Safe Mother</h1>

<p align="center">
  <strong>AI-Powered Maternal Health Risk Prediction System</strong>
</p>

<p align="center">
  Predict • Prevent • Protect
</p>

<p align="center">
  <a href="https://safe-mother-gray.vercel.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Visit_Website-blue?style=for-the-badge" />
  </a>
  &nbsp;
  <a href="https://github.com/Harikrishnankanjingattu/safe_mother">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB?logo=react">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Vercel-Deployed-black?logo=vercel">
  <img src="https://img.shields.io/badge/License-MIT-success">
</p>

---

# 📖 About

**Safe Mother** is an AI-powered Maternal Health Risk Prediction System that predicts pregnancy risk levels using Machine Learning.

The application analyzes maternal health parameters and classifies the patient into one of three categories:

- 🟢 Low Risk
- 🟡 Mid Risk
- 🔴 High Risk

The primary objective of this project is to assist in early detection of pregnancy-related health risks, enabling timely medical intervention.

---

# 🌐 Live Demo

### 🚀 https://safe-mother-gray.vercel.app/

---

# ✨ Features

- 🤖 AI-powered maternal risk prediction
- 📊 Logistic Regression Machine Learning model
- ⚡ Real-time prediction
- 📈 Data preprocessing & feature scaling
- 💾 Saved ML model using Joblib (.pkl)
- 🌐 Responsive React frontend
- 🚀 Deployed on Vercel
- 📱 Clean and modern UI

---

# 🧠 Machine Learning Workflow

```
Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Label Encoding
    │
    ▼
Train Test Split
    │
    ▼
Feature Scaling
    │
    ▼
Logistic Regression
    │
    ▼
Model Evaluation
    │
    ▼
Risk Prediction
```

---

# 📊 Dataset Features

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

# 🎯 Prediction Classes

| Risk Level | Meaning |
|------------|---------|
| 🟢 Low Risk | Healthy Pregnancy |
| 🟡 Mid Risk | Requires Regular Monitoring |
| 🔴 High Risk | Immediate Medical Attention Recommended |

---

# 🛠️ Tech Stack

## Frontend

- React.js
- HTML5
- CSS3
- JavaScript

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

## Deployment

- Vercel
- GitHub

---

# 📈 Model Information

| Item | Value |
|------|-------|
| Algorithm | Logistic Regression |
| Problem Type | Multi-Class Classification |
| Prediction | Low / Mid / High Risk |
| Feature Scaling | StandardScaler |
| Label Encoding | LabelEncoder |

---

# 📂 Project Structure

```
safe_mother
│
├── frontend
├── backend
├── model
│
├── dataset.csv
├── main.py
├── maternal_risk_model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── requirements.txt
├── safe.png
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Harikrishnankanjingattu/safe_mother.git
```

## Move to Project

```bash
cd safe_mother
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
python main.py
```

---

# 💻 Sample Input

```
Age : 30

Systolic Blood Pressure : 130

Diastolic Blood Pressure : 80

Blood Sugar : 7.2

Body Temperature : 98.6

Heart Rate : 72
```

---

# 📋 Sample Output

```
Predicted Risk Level

LOW RISK
```

---

# 🚀 Future Improvements

- Random Forest Model
- XGBoost Integration
- Explainable AI (SHAP)
- Doctor Dashboard
- Patient History
- Authentication
- PDF Medical Report
- Email Notifications
- Cloud Database
- Mobile Application

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 👨‍💻 Author

## Harikrishnan K

Backend Developer • Machine Learning Enthusiast • AI Developer

### GitHub

https://github.com/Harikrishnankanjingattu

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the **MIT License**.

---

<p align="center">
Made with ❤️ using Python, React and Machine Learning
</p>
