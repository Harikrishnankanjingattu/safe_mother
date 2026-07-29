import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

# 1. Load dataset
df = pd.read_csv("dataset.csv")

X = df.drop("RiskLevel", axis=1)
y = df["RiskLevel"]

# 2. Encode target labels (low risk, mid risk, high risk)
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# 3. Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 4. Scale feature values
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 5. Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 6. Save model, scaler, and encoder to disk
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoder, "encoder.pkl")

print("Model, scaler, and encoder saved successfully!")
