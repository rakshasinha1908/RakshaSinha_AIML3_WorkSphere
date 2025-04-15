from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pickle
from flask_cors import CORS
from question_logic import get_morning_questions

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
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    email = request.form.get("email")

    if email in users:
        # ✅ Pass user email to dashboard page
        return render_template('dashboard.html', user=email)
    else:
        return "❌ Invalid User. Go Back and try again."

@app.route('/morning-checkin')
def morning_questions():
    # ✅ Get user from query parameter
    user_email = request.args.get("user")
    if not user_email:
        return "User email not provided", 400
    
    questions = get_morning_questions(user_name=user_email.split("@")[0].capitalize())
    return render_template('morning_questions.html', questions=questions)

@app.route('/submit_morning_checkin', methods=['POST'])
def submit_morning_checkin():
    user_responses = request.form.to_dict()
    print("📥 Received Responses:", user_responses)  # For debugging

    # You can store/analyze/save responses here
    return "✅ Morning Check-In Submitted! Thank you."

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print("📥 Received Data:", data)

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
