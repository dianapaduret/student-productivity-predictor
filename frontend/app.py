import streamlit as st
import requests

st.set_page_config(page_title="Student Productivity Predictor", page_icon="🎓")

st.title("🎓 Student Productivity Predictor")
st.write("Enter your daily habits and get your predicted productivity score.")

sleep_hours = st.slider("Sleep hours", 0.0, 12.0, 7.0, 0.5)
phone_usage_hours = st.slider("Phone usage hours", 0.0, 15.0, 4.0, 0.5)
study_hours_per_day = st.slider("Study hours per day", 0.0, 12.0, 5.0, 0.5)

if st.button("Predict productivity"):
    payload = {
        "sleep_hours": sleep_hours,
        "phone_usage_hours": phone_usage_hours,
        "study_hours_per_day": study_hours_per_day
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            prediction = result["predicted_productivity"]
            st.success(f"Predicted productivity score: {prediction}")
        else:
            st.error("API request failed.")

    except:
        st.error("Backend not running.")