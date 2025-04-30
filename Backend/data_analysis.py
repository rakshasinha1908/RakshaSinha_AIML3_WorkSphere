

import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# CSV file load karo
file_path = "D:\WorkSphere\dataset\data.csv"  
df = pd.read_csv(file_path)

# Pehle kuch rows check karo
print("First 5 rows of data:")
print(df.head())

# Missing values check karo aur fill karo
print("\nMissing values before handling:")
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
print("\nMissing values after handling:")
print(df.isnull().sum())

# Datatypes check karo
print("\nData Types:")
print(df.dtypes)

# Correlation matrix plot karo
plt.figure(figsize=(12,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# 🟢 Hypothesis 1: Overtime vs Mental Health
t_stat_overtime, p_value_overtime = stats.ttest_ind(
    df[df["Overtime Hours"] > df["Overtime Hours"].median()]["Mental Health Status"],
    df[df["Overtime Hours"] <= df["Overtime Hours"].median()]["Mental Health Status"]
)
print(f"T-Statistic (Overtime vs Mental Health): {t_stat_overtime}")
print(f"P-Value: {p_value_overtime}")
if p_value_overtime < 0.05:
    print("Reject Null Hypothesis: Overtime mental health ko affect karta hai.")
else:
    print("Fail to Reject Null Hypothesis: Overtime ka direct impact nahi hai.")

# 🟢 Hypothesis 2: Break Duration vs Mental Health
t_stat_break, p_value_break = stats.ttest_ind(
    df[df["Break Duration (mins)"] > df["Break Duration (mins)"].median()]["Mental Health Status"],
    df[df["Break Duration (mins)"] <= df["Break Duration (mins)"].median()]["Mental Health Status"]
)
print(f"T-Statistic (Break Duration vs Mental Health): {t_stat_break}")
print(f"P-Value: {p_value_break}")
if p_value_break < 0.05:
    print("Reject Null Hypothesis: Break duration mental health pe effect dalta hai.")
else:
    print("Fail to Reject Null Hypothesis: Break duration ka direct impact nahi hai.")

# 🔵 Scatter Plot (Workload vs Mental Health)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Workload"], y=df["Mental Health Status"])
plt.title("Workload vs Mental Health Trend")
plt.xlabel("Workload")
plt.ylabel("Mental Health Status")
plt.show()

# 🔵 Regression Line
sns.regplot(x=df["Workload"], y=df["Mental Health Status"])
plt.title("Regression: Workload vs Mental Health")
plt.show()

# 🔴 Classification Model (Predict Mental Health from Workload & Others)
X = df[["Workload", "Task Complexity", "Break Duration (mins)", "Overtime Hours"]]
y = df["Mental Health Status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("🔵 Classification Report:")
print(classification_report(y_test, y_pred))

print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")

# 🔴 Feature Importance (Task Complexity, Break Duration, Overtime ka impact)
feature_importances = pd.Series(model.feature_importances_, index=X.columns)
feature_importances.plot(kind="barh")
plt.title("Feature Importance")
plt.show()


from sklearn.preprocessing import MinMaxScaler

# Mental Health Status ko normalize karo
scaler = MinMaxScaler()
df["Wellness Score"] = scaler.fit_transform(df[["Mental Health Status"]]) * 100

# Model ko regression problem par train karo
X = df[["Workload", "Task Complexity", "Break Duration (mins)", "Overtime Hours"]]
y = df["Wellness Score"]

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
model.fit(X, y)

# Test prediction
example = [[10, 7, 40, 120]]  # 10 tasks, complexity 7, 40 min break, 2 hr overtime
predicted_score = model.predict(example)
print(f"Predicted Wellness Score: {predicted_score[0]:.2f}")




