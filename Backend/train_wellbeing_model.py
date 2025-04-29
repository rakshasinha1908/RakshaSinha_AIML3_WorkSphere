import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle
 
# Load the dataset
df = pd.read_csv("D:\work\WorkSphere\dataset\sample_wellbeing_data.csv")

X = df.drop(columns=["wellbeing_score"])
y = df["wellbeing_score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"✅ Model trained successfully!")
print(f"📉 Mean Squared Error: {mse:.2f}")
print(f"📈 R2 Score: {r2:.2f}")

# Save the model
with open("wellbeing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("💾 Model saved as wellbeing_model.pkl")
