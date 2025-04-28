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
        # Send data to Flask's /predict endpoint
        response = requests.post("http://127.0.0.1:5001/predict", json=data)

        # Show error message if something went wrong
        if response.status_code != 200:
            st.error(f"❌ Error {response.status_code}: {response.text}")
        else:
            # Get the wellness score from the response
            result = response.json()
            wellness_score = result["Wellness Score"]
            st.success(f"✅ Your predicted Wellness Score is: **{wellness_score}/100**")

            # Now, send the wellness score as the mental score to Flask's /submit_mental_score endpoint
            mental_score_data = {"mental_score": wellness_score}

            # Send the mental score to Flask
            mental_score_response = requests.post("http://127.0.0.1:5001/submit_mental_score", json=mental_score_data)

            # Check if the mental score was successfully recorded
            if mental_score_response.status_code == 200:
                st.success("✅ Your mental score has been successfully recorded.")
            else:
                st.error(f"❌ Error in submitting mental score: {mental_score_response.text}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Failed to connect to backend: {e}")
