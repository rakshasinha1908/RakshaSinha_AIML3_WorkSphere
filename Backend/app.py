# from flask import Flask, request, jsonify, render_template, redirect, url_for
# import numpy as np
# import pickle
# from flask_cors import CORS
# from question_logic import get_morning_questions
# import re  # For email validation

# app = Flask(__name__)
# CORS(app)

# # Load trained model
# with open("D:/WorkSphere/Backend/wellness_model.pkl", "rb") as f:
#     reg_model = pickle.load(f)

# # 🔒 Dummy users - replace with DB later
# users = {
#     "user@example.com": "User123",
#     "rakshasinha1908@gmail.com": "raksha19"
# }

# # ----------------- ROUTES ------------------

# # Email validation function
# def is_valid_email(email):
#     # Regular expression to validate email format
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
#     return re.match(pattern, email)

# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/dashboard', methods=['POST'])
# def dashboard():
#     email = request.form.get("email")

#     # ✅ Regex to validate email format
#     if re.match(r"[^@]+@[^@]+\.[^@]+", email):
#         return render_template('dashboard.html', user=email)
#     else:
#         return "❌ Invalid Email Format. Please go back and try again."

# @app.route('/morning-checkin')
# def morning_questions():
#     # ✅ Get user from query parameter
#     user_email = request.args.get("user")
#     if not user_email:
#         return "User email not provided", 400
    
#     questions = get_morning_questions(user_name=user_email.split("@")[0].capitalize())
#     return render_template('morning_questions.html', questions=questions)

# @app.route('/submit_morning_checkin', methods=['POST'])
# def submit_morning_checkin():
#     user_responses = request.form.to_dict()
#     print("📥 Received Responses:", user_responses)  # For debugging

#     # You can store/analyze/save responses here
#     return "✅ Morning Check-In Submitted! Thank you."

# @app.route('/logout')
# def logout():
#     return render_template('logout.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     print("📥 Received Data:", data)

#     try:
#         workload = float(data.get("Workload"))
#         task_complexity = float(data.get("Task Complexity"))
#         break_duration = float(data.get("Break Duration (mins)", data.get("Break Duration")))
#         overtime = float(data.get("Overtime Hours", data.get("Overtime")))

#         input_data = np.array([[workload, task_complexity, break_duration, overtime]])
#         predicted_score = reg_model.predict(input_data)[0]
#         predicted_score = round(predicted_score, 2)
#         predicted_score = max(min(predicted_score, 100), 0)

#         return jsonify({"Wellness Score": predicted_score})
    
#     except Exception as e:
#         print("❌ Error in prediction:", str(e))
#         return jsonify({"error": str(e)}), 500

# # ----------------- RUN ------------------

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)


# from flask import Flask, request, jsonify, render_template, redirect, url_for
# import numpy as np
# import pickle
# from flask_cors import CORS
# from question_logic import get_morning_questions
# import re  # For email validation

# app = Flask(__name__)
# CORS(app)

# # Load trained workload-wellness model
# with open("D:/WorkSphere/Backend/wellness_model.pkl", "rb") as f:
#     reg_model = pickle.load(f)

# # 🔒 Dummy users - replace with DB later
# users = {
#     "user@example.com": "User123",
#     "rakshasinha1908@gmail.com": "raksha19"
# }

# # ----------------- ROUTES ------------------

# # Email validation function
# def is_valid_email(email):
#     # Regular expression to validate email format
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
#     return re.match(pattern, email)

# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/dashboard', methods=['POST'])
# def dashboard():
#     email = request.form.get("email")

#     # ✅ Regex to validate email format
#     if re.match(r"[^@]+@[^@]+\.[^@]+", email):
#         return render_template('dashboard.html', user=email)
#     else:
#         return "❌ Invalid Email Format. Please go back and try again."

# @app.route('/morning-checkin')
# def morning_questions():
#     # ✅ Get user from query parameter
#     user_email = request.args.get("user")
#     if not user_email:
#         return "User email not provided", 400

#     questions = get_morning_questions(user_name=user_email.split("@")[0].capitalize())
#     return render_template('morning_questions.html', questions=questions)

# @app.route('/submit_morning_checkin', methods=['POST'])
# def submit_morning_checkin():
#     user_responses = request.form.to_dict()
#     print("📥 Received Responses:", user_responses)  # For debugging

#     try:
#         # 🧠 Preprocess the answers
#         from data_preprocessing import preprocess_answers
#         features = preprocess_answers(user_responses)

#         # 📊 Load emotional wellbeing model
#         with open("D:/WorkSphere/Backend/wellbeing_model.pkl", "rb") as f:
#             model = pickle.load(f)

#         # 🤖 Predict the wellbeing score
#         input_data = np.array(features).reshape(1, -1)
#         predicted_score = model.predict(input_data)[0]
#         predicted_score = round(predicted_score)
#         predicted_score = max(min(predicted_score, 100), 0)

#         # ✅ Return the response with score
#         return f"✅ Morning Check-In Submitted! Thank you. Your Emotional Wellbeing Score is: {predicted_score}"

#     except Exception as e:
#         print("❌ Prediction Error:", str(e))
#         return f"❌ Error while predicting wellbeing score: {str(e)}"

# @app.route('/logout')
# def logout():
#     return render_template('logout.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     print("📥 Received Data:", data)

#     try:
#         workload = float(data.get("Workload"))
#         task_complexity = float(data.get("Task Complexity"))
#         break_duration = float(data.get("Break Duration (mins)", data.get("Break Duration")))
#         overtime = float(data.get("Overtime Hours", data.get("Overtime")))

#         input_data = np.array([[workload, task_complexity, break_duration, overtime]])
#         predicted_score = reg_model.predict(input_data)[0]
#         predicted_score = round(predicted_score, 2)
#         predicted_score = max(min(predicted_score, 100), 0)

#         return jsonify({"Wellness Score": predicted_score})

#     except Exception as e:
#         print("❌ Error in prediction:", str(e))
#         return jsonify({"error": str(e)}), 500

# # ----------------- RUN ------------------

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)


from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pickle
from flask_cors import CORS
from question_logic import get_morning_questions, MORNING_QUESTIONS
import re  # For email validation

app = Flask(__name__)
CORS(app)

# Load trained workload-wellness model
with open("D:/WorkSphere/Backend/wellness_model.pkl", "rb") as f:
    reg_model = pickle.load(f)

# 🔒 Dummy users - replace with DB later
users = {
    "user@example.com": "User123",
    "rakshasinha1908@gmail.com": "raksha19"
}

# ----------------- ROUTES ------------------

# Email validation function
def is_valid_email(email):
    # Regular expression to validate email format
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    email = request.form.get("email")

    # ✅ Regex to validate email format
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return render_template('dashboard.html', user=email)
    else:
        return "❌ Invalid Email Format. Please go back and try again."

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

    try:
        from data_preprocessing import preprocess_answers

        # Step 1: Make sure all 15 question IDs are represented
        all_ids = [q["id"] for q in MORNING_QUESTIONS]
        default_values = {
            "slider": 5,  # Neutral
            "dropdown": "No"  # Default option for missing dropdown
        }

        # Step 2: Fill missing answers
        full_response = {}
        for q in MORNING_QUESTIONS:
            qid = q["id"]
            if qid in user_responses:
                full_response[qid] = user_responses[qid]
            else:
                if q["type"] == "slider":
                    full_response[qid] = default_values["slider"]
                elif q["type"] == "dropdown":
                    full_response[qid] = q["options"][0]  # Default to first option

        print("🧾 Full Responses (with defaults):", full_response)

        # Step 3: Preprocess & Predict
        features = preprocess_answers(full_response)

        with open("D:/WorkSphere/Backend/wellbeing_model.pkl", "rb") as f:
            model = pickle.load(f)

        input_data = np.array(features).reshape(1, -1)
        predicted_score = model.predict(input_data)[0]
        predicted_score = round(predicted_score)
        predicted_score = max(min(predicted_score, 100), 0)

        return f"✅ Morning Check-In Submitted! Your Emotional Wellbeing Score is: {predicted_score}"

    except Exception as e:
        print("❌ Prediction Error:", str(e))
        return f"❌ Error while predicting wellbeing score: {str(e)}"

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
