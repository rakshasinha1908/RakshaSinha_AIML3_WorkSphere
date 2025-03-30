# import streamlit as st
# import requests

# st.title("Employee Wellness Score Predictor")

# workload = st.slider("Workload (Tasks Completed)", 1, 20, 10)
# task_complexity = st.slider("Task Complexity (1-10)", 1, 10, 5)
# break_duration = st.slider("Total Break Duration (mins)", 0, 120, 30)
# overtime = st.slider("Overtime (mins)", 0, 180, 60)

# if st.button("Predict Wellness Score"):
#     data = {
#         "Workload": workload,
#         "Task Complexity": task_complexity,
#         "Break Duration (mins)": break_duration,  # ✅ FIXED
#         "Overtime Hours": overtime                 # ✅ FIXED
#     }
    
#     response = requests.post("http://127.0.0.1:5001/predict", json=data)
#     score = response.json()["Wellness Score"]
    
#     st.write(f"Predicted Wellness Score: {score}/100")


import streamlit as st
import requests

st.set_page_config(page_title="Wellness Score Predictor", layout="centered")

st.title("🧠 Wellness Score Predictor")
st.write("Fill in the details below to predict your wellness score.")

# Input fields
workload = st.slider("Workload (1 to 10)", 1, 10, 5)
task_complexity = st.slider("Task Complexity (1 to 5)", 1, 5, 3)
break_duration = st.number_input("Break Duration (in minutes)", min_value=0, max_value=240, value=30)
overtime = st.number_input("Overtime Hours", min_value=0.0, max_value=10.0, value=0.0)

# Predict button
if st.button("🔮 Predict Wellness Score"):
    data = {
        "Workload": workload,
        "Task Complexity": task_complexity,
        "Break Duration (mins)": break_duration,
        "Overtime Hours": overtime
    }

    try:
        response = requests.post("http://127.0.0.1:5001/predict", json=data)

        # Show raw error if any
        if response.status_code != 200:
            st.error(f"❌ Error {response.status_code}: {response.text}")
        else:
            result = response.json()
            score = result["Wellness Score"]
            st.success(f"✅ Your predicted Wellness Score is: **{score}/100**")
    
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Failed to connect to backend: {e}")

