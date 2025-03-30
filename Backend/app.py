# import sys
# sys.stdout.reconfigure(encoding='utf-8')
# import pandas as pd
# import scipy.stats as stats
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# from flask import Flask, request, jsonify
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
# from sklearn.metrics import accuracy_score, classification_report

# # ✅ CSV file load
# file_path = r"D:\WorkSphere\dataset\data.csv"
# df = pd.read_csv(file_path)

# # ✅ Missing values handling
# df.fillna(df.mean(numeric_only=True), inplace=True)

# # ✅ Correlation matrix plot
# plt.figure(figsize=(12,6))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Feature Correlation Heatmap")
# plt.show()

# # ✅ Hypothesis Testing (Overtime vs Mental Health)
# t_stat_overtime, p_value_overtime = stats.ttest_ind(
#     df[df["Overtime Hours"] > df["Overtime Hours"].median()]["Mental Health Status"],
#     df[df["Overtime Hours"] <= df["Overtime Hours"].median()]["Mental Health Status"]
# )
# print(f"T-Statistic (Overtime vs Mental Health): {t_stat_overtime}")
# print(f"P-Value: {p_value_overtime}")

# # ✅ Scatter Plot (Workload vs Mental Health)
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x=df["Workload"], y=df["Mental Health Status"])
# plt.title("Workload vs Mental Health Trend")
# plt.xlabel("Workload")
# plt.ylabel("Mental Health Status")
# plt.show()

# # ✅ Train RandomForestClassifier
# X = df[["Workload", "Task Complexity", "Break Duration (mins)", "Overtime Hours"]]
# y = df["Mental Health Status"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("🔵 Classification Report:")
# print(classification_report(y_test, y_pred))
# print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")

# # ✅ Feature Importance
# feature_importances = pd.Series(model.feature_importances_, index=X.columns)
# feature_importances.plot(kind="barh")
# plt.title("Feature Importance")
# plt.show()

# # ✅ Modified Wellness Score Generation (based on Mental Health Status)
# def get_wellness_score(status):
#     if status == 1:
#         return np.random.randint(80, 101)
#     elif status == 2:
#         return np.random.randint(40, 80)
#     else:
#         return np.random.randint(0, 40)

# # ✅ Apply the logic
# df["Wellness Score"] = df["Mental Health Status"].apply(get_wellness_score)

# # ✅ Regression Model
# reg_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
# reg_model.fit(X, df["Wellness Score"])

# # ✅ Flask API
# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     input_data = np.array([[data["Workload"], data["Task Complexity"], 
#                             data["Break Duration"], data["Overtime"]]])
#     predicted_score = reg_model.predict(input_data)[0]
#     return jsonify({"Wellness Score": round(predicted_score, 2)})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001, debug=False)

# # ✅ Plot Feature Importances Again
# importances = model.feature_importances_
# features = X.columns

# plt.figure(figsize=(8,5))
# sns.barplot(x=importances, y=features)
# plt.xlabel("Feature Importance Score")
# plt.ylabel("Features")
# plt.title("Feature Importance for Prediction")
# plt.show()


# import sys
# sys.stdout.reconfigure(encoding='utf-8')
# import pandas as pd
# import scipy.stats as stats
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# from flask import Flask, request, jsonify
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
# from sklearn.metrics import accuracy_score, classification_report

# # ✅ Load data
# file_path = r"D:\WorkSphere\dataset\data.csv"
# df = pd.read_csv(file_path)
# df.fillna(df.mean(numeric_only=True), inplace=True)

# # ✅ Visualizations
# plt.figure(figsize=(12,6))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Feature Correlation Heatmap")
# plt.show()

# # ✅ Hypothesis Testing (Overtime vs Mental Health)
# t_stat_overtime, p_value_overtime = stats.ttest_ind(
#     df[df["Overtime Hours"] > df["Overtime Hours"].median()]["Mental Health Status"],
#     df[df["Overtime Hours"] <= df["Overtime Hours"].median()]["Mental Health Status"]
# )
# print(f"T-Statistic (Overtime vs Mental Health): {t_stat_overtime}")
# print(f"P-Value: {p_value_overtime}")

# # ✅ Workload vs Mental Health
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x=df["Workload"], y=df["Mental Health Status"])
# plt.title("Workload vs Mental Health Trend")
# plt.xlabel("Workload")
# plt.ylabel("Mental Health Status")
# plt.show()

# # ✅ Classification Model
# X = df[["Workload", "Task Complexity", "Break Duration (mins)", "Overtime Hours"]]
# y = df["Mental Health Status"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("🔵 Classification Report:")
# print(classification_report(y_test, y_pred))
# print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")

# # ✅ Feature Importance
# feature_importances = pd.Series(model.feature_importances_, index=X.columns)
# feature_importances.plot(kind="barh")
# plt.title("Feature Importance")
# plt.show()

# # ✅ 🎯 SMART Wellness Score Generation
# def calculate_wellness(row):
#     score = 100
#     score -= row["Workload"] * 4
#     score -= row["Task Complexity"] * 3

#     if row["Break Duration (mins)"] >= 90:
#         score += 5
#     elif row["Break Duration (mins)"] < 30:
#         score -= 5

#     if row["Overtime Hours"] > 2:
#         score -= 10
#     elif row["Overtime Hours"] > 0:
#         score -= 5

#     return min(max(score, 0), 100)


# df["Wellness Score"] = df.apply(calculate_wellness, axis=1)
# print(df["Wellness Score"].describe())
# print(df["Wellness Score"].head(10))


# # ✅ Regression Model
# reg_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
# reg_model.fit(X, df["Wellness Score"])

# # ✅ Flask API
# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     input_data = np.array([[data["Workload"], data["Task Complexity"], 
#                             data["Break Duration"], data["Overtime"]]])
#     predicted_score = reg_model.predict(input_data)[0]
#     return jsonify({"Wellness Score": round(predicted_score, 2)})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001, debug=False)

# # ✅ Feature Importance Re-Plot
# importances = model.feature_importances_
# features = X.columns

# plt.figure(figsize=(8,5))
# sns.barplot(x=importances, y=features)
# plt.xlabel("Feature Importance Score")
# plt.ylabel("Features")
# plt.title("Feature Importance for Prediction")
# plt.show()


# import sys
# sys.stdout.reconfigure(encoding='utf-8')

# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from flask import Flask, request, jsonify
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
# from sklearn.metrics import accuracy_score, classification_report
# import scipy.stats as stats

# # ✅ Load Data
# file_path = r"D:\WorkSphere\dataset\data.csv"
# df = pd.read_csv(file_path)
# df.fillna(df.mean(numeric_only=True), inplace=True)

# # ✅ Visualizations
# plt.figure(figsize=(12,6))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Feature Correlation Heatmap")
# plt.show()

# # ✅ T-Test (Optional)
# t_stat_overtime, p_value_overtime = stats.ttest_ind(
#     df[df["Overtime Hours"] > df["Overtime Hours"].median()]["Mental Health Status"],
#     df[df["Overtime Hours"] <= df["Overtime Hours"].median()]["Mental Health Status"]
# )
# print(f"T-Statistic (Overtime vs Mental Health): {t_stat_overtime}")
# print(f"P-Value: {p_value_overtime}")

# # ✅ Scatter Plot
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x=df["Workload"], y=df["Mental Health Status"])
# plt.title("Workload vs Mental Health Trend")
# plt.xlabel("Workload")
# plt.ylabel("Mental Health Status")
# plt.show()

# # ✅ Classification Model
# X = df[["Workload", "Task Complexity", "Break Duration (mins)", "Overtime Hours"]]
# y = df["Mental Health Status"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# clf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# clf_model.fit(X_train, y_train)

# y_pred = clf_model.predict(X_test)
# print("🔵 Classification Report:")
# print(classification_report(y_test, y_pred))
# print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")

# # ✅ Updated Wellness Score Logic (SMART)
# def calculate_wellness(row):
#     score = 100
#     score -= row["Workload"] * 2
#     score -= row["Task Complexity"] * 2

#     if row["Break Duration (mins)"] >= 90:
#         score += 10
#     elif row["Break Duration (mins)"] >= 60:
#         score += 5
#     elif row["Break Duration (mins)"] < 30:
#         score -= 5

#     if row["Overtime Hours"] > 2:
#         score -= 10
#     elif row["Overtime Hours"] > 0:
#         score -= 3

#     return min(max(score, 0), 100)

# # ✅ Apply new score logic to all rows
# df["Wellness Score"] = df.apply(calculate_wellness, axis=1)

# # ✅ Retrain Regression Model on new values
# reg_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
# reg_model.fit(X, df["Wellness Score"])

# # ✅ Feature Importance
# feature_importances = pd.Series(clf_model.feature_importances_, index=X.columns)
# feature_importances.plot(kind="barh")
# plt.title("Feature Importance")
# plt.show()

# # ✅ Flask API
# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     input_data = np.array([[data["Workload"], data["Task Complexity"],
#                             data["Break Duration"], data["Overtime"]]])
#     predicted_score = reg_model.predict(input_data)[0]
#     predicted_score = round(predicted_score, 2)
#     predicted_score = max(min(predicted_score, 100), 0)  # Clamp between 0-100
#     return jsonify({"Wellness Score": predicted_score})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001, debug=False)

# sample = pd.DataFrame([{
#     "Workload": 10,
#     "Task Complexity": 4,
#     "Break Duration (mins)": 62,
#     "Overtime Hours": 1.5
# }])

# print("Manual Score:", calculate_wellness(sample.iloc[0]))  # This should be ~74
# print("Model Prediction:", reg_model.predict(sample)[0])    # This should match


# from flask import Flask, request, jsonify
# import numpy as np
# import pickle
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Allow CORS for Streamlit access

# # Load trained model
# with open("D:/WorkSphere/Backend/wellness_model.pkl", "rb") as f:
#     reg_model = pickle.load(f)

# @app.route('/')
# def home():
#     return "Welcome to the Wellness Score Prediction API!"

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     print("📥 Received Data:", data)  # Debug print

#     try:
#         # Extract input values
#         workload = float(data.get("Workload"))
#         task_complexity = float(data.get("Task Complexity"))
#         break_duration = float(data.get("Break Duration (mins)", data.get("Break Duration")))
#         overtime = float(data.get("Overtime Hours", data.get("Overtime")))

#         # Prepare input for model
#         input_data = np.array([[workload, task_complexity, break_duration, overtime]])

#         # Predict score
#         predicted_score = reg_model.predict(input_data)[0]
#         predicted_score = round(predicted_score, 2)
#         predicted_score = max(min(predicted_score, 100), 0)  # Clamp between 0 and 100

#         return jsonify({"Wellness Score": predicted_score})
    
#     except Exception as e:
#         print("❌ Error in prediction:", str(e))
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)


from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pickle
from flask_cors import CORS
import os
print("Current Working Directory:", os.getcwd())
print("Templates Folder Exists:", os.path.exists("templates"))
print("login.html Exists:", os.path.exists("templates/login.html"))


app = Flask(__name__)
CORS(app)


# Load trained model
with open("D:/WorkSphere/Backend/wellness_model.pkl", "rb") as f:
    reg_model = pickle.load(f)

# 🔒 Dummy users - replace with DB later
users = {
    "user@example.com": "User123",
    "rakshasinha1908@gmail.com": "raksha19"
    }


# ----------------- ROUTES ------------------

@app.route('/')
def home():
    return redirect(url_for('login'))  # Redirecting to login page

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    email = request.form.get("email")

    if email in users:  # Very basic check
        return render_template('dashboard.html', user=email)
    else:
        return "❌ Invalid User. Go Back and try again."
    
@app.route('/morning-checkin')
def morning_questions():
    return render_template('morning_questions.html')  


@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print("📥 Received Data:", data)  # Debug print

    try:
        workload = float(data.get("Workload"))
        task_complexity = float(data.get("Task Complexity"))
        break_duration = float(data.get("Break Duration (mins)", data.get("Break Duration")))
        overtime = float(data.get("Overtime Hours", data.get("Overtime")))

        input_data = np.array([[workload, task_complexity, break_duration, overtime]])

        predicted_score = reg_model.predict(input_data)[0]
        predicted_score = round(predicted_score, 2)
        predicted_score = max(min(predicted_score, 100), 0)

        return jsonify({"Wellness Score": predicted_score})
    
    except Exception as e:
        print("❌ Error in prediction:", str(e))
        return jsonify({"error": str(e)}), 500

# ----------------- RUN ------------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)
