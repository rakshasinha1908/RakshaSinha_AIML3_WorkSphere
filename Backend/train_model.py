import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Dummy dataset (Replace with actual dataset)
data = {
    "Workload": np.random.randint(1, 11, 100),
    "Task Complexity": np.random.randint(1, 6, 100),
    "Break Duration": np.random.randint(5, 60, 100),
    "Overtime Hours": np.random.uniform(0, 10, 100),
    "Wellness Score": np.random.randint(20, 100, 100)  # Target variable
}

df = pd.DataFrame(data)

# Features & Target
X = df.drop(columns=["Wellness Score"])
y = df["Wellness Score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save trained model
with open("wellness_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as 'wellness_model.pkl'")
