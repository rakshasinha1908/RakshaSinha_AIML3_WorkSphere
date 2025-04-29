from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import numpy as np
import pickle
import json
import os
from flask_cors import CORS
from question_logic import get_morning_questions, MORNING_QUESTIONS
import re  # For email validation

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions
CORS(app)

# Load trained wellness model
with open("D:/work/WorkSphere/Backend/wellness_model.pkl", "rb") as f:
    reg_model = pickle.load(f)

# Users file path
USERS_FILE = 'users.json'

# ----------------- FUNCTIONS ------------------

# Email validation function
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email)

# Load users from JSON
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save users to JSON
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# ----------------- ROUTES ------------------

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        users = load_users()

        # ✅ Check if email exists and password matches
        if email in users and users[email]["password"] == password:
            session['user_email'] = email  # Store email in session
            return redirect(url_for('dashboard'))
        else:
            return "❌ Invalid Credentials. Please try again or <a href='/register'>Register here</a>."
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # ✅ Validate email format
        if not is_valid_email(email):
            return "❌ Invalid Email Format. <a href='/register'>Try again</a>."

        users = load_users()

        if email in users:
            return "❌ User already exists. <a href='/login'>Login here</a>."
        
        # ✅ Save new user with name and password
        users[email] = {"name": name, "password": password}
        save_users(users)
        return render_template('login.html')

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        return redirect(url_for('login'))  # Redirect to login if no user is logged in

    user_email = session['user_email']  # Get email from session
    users = load_users()
    user_info = users.get(user_email)

    if user_info:
        name = user_info.get("name", user_email.split("@")[0].capitalize())
        return render_template('dashboard.html', user=name)
    return redirect(url_for('login'))  # If user not found, go to login

@app.route('/morning-checkin')
def morning_questions():
    user_email = request.args.get("user")
    if not user_email:
        return "User email not provided", 400

    questions = get_morning_questions(user_name=user_email.split("@")[0].capitalize())
    return render_template('morning_questions.html', questions=questions, user_email=user_email)

@app.route('/submit_morning_checkin', methods=['POST'])
def submit_morning_checkin():
    user_responses = request.form.to_dict()
    print("📥 Received Responses:", user_responses)

    try:
        from data_preprocessing import preprocess_answers

        all_ids = [q["id"] for q in MORNING_QUESTIONS]
        default_values = {
            "slider": 5,
            "dropdown": "No"
        }

        full_response = {}
        for q in MORNING_QUESTIONS:
            qid = q["id"]
            if qid in user_responses:
                full_response[qid] = user_responses[qid]
            else:
                if q["type"] == "slider":
                    full_response[qid] = default_values["slider"]
                elif q["type"] == "dropdown":
                    full_response[qid] = q["options"][0]

        print("🧾 Full Responses (with defaults):", full_response)

        # Load the model and predict emotional wellness score
        with open("D:/work/WorkSphere/Backend/wellbeing_model.pkl", "rb") as f:
            model = pickle.load(f)

        features = preprocess_answers(full_response)
        input_data = np.array(features).reshape(1, -1)
        predicted_score = model.predict(input_data)[0]
        predicted_score = round(predicted_score)
        predicted_score = max(min(predicted_score, 100), 0)

        # Save this predicted score somewhere. You can store it in a global variable, database, or file.
        user_email = request.form.get("email")  # Make sure user email is passed along.
        
        # You can save the score to a file or database here
        with open("emotional_wellness_scores.json", "a") as f:
            json.dump({"email": user_email, "emotional_wellness_score": predicted_score}, f)
            f.write("\n")

        return f"✅ Morning Check-In Submitted! Your Emotional Wellbeing Score is: {predicted_score}"

    except Exception as e:
        print("❌ Prediction Error:", str(e))
        return f"❌ Error while predicting wellbeing score: {str(e)}"
    
# Form to fill out wellness data (workload, task complexity, etc.)
@app.route('/wellness-checkin')
def wellness_checkin():
    # Render a wellness check-in form template
    return render_template('wellness_form.html')

# Handle the form submission and prediction
@app.route('/submit_wellness_checkin', methods=['POST'])
def submit_wellness_checkin():
    try:
        # Get form data
        workload = float(request.form['workload'])
        task_complexity = float(request.form['task_complexity'])
        break_duration = float(request.form['break_duration'])
        overtime = float(request.form['overtime'])

        # Create input array for prediction
        input_data = np.array([[workload, task_complexity, break_duration, overtime]])

        # Load your trained model (use the path provided)
        with open("D:/work/WorkSphere/Backend/wellbeing_model.pkl", "rb") as f:
            wellbeing_model = pickle.load(f)

        # Predict wellness score using the loaded model
        predicted_score = wellbeing_model.predict(input_data)[0]
        predicted_score = round(predicted_score, 2)
        predicted_score = max(min(predicted_score, 100), 0)

        # Optionally save the score or do further actions here

        # Return a success message with the predicted score
        return jsonify({"Wellness Score": predicted_score})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/predict', methods=['POST'])
def predict():
    try:
        workload = float(request.form['workload'])
        task_complexity = float(request.form['task_complexity'])
        break_duration = float(request.form['break_duration'])
        overtime = float(request.form['overtime'])

        input_data = np.array([[workload, task_complexity, break_duration, overtime]])
        predicted_score = reg_model.predict(input_data)[0]
        predicted_score = round(predicted_score, 2)
        predicted_score = max(min(predicted_score, 100), 0)

        return jsonify({"Wellness Score": predicted_score})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/logout')
def logout():
    session.pop('user_email', None)  # Remove user email from session
    return redirect(url_for('login'))  # Redirect to login page after logout

# ----------------- RUN ------------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)
