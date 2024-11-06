# Save this code as app.py and run it with `streamlit run app.py`

import streamlit as st
import pandas as pd
import numpy as np
import joblib  # or use pickle
from sklearn.preprocessing import StandardScaler

# Load pre-trained models
prof_model = joblib.load('prof_model.pkl')  # Path to your trained professional model
stud_model = joblib.load('stud_model.pkl')  # Path to your trained student model

# UI title
st.title("")

# Input fields
name = st.text_input("Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
city = st.text_input("City")
user_type = st.selectbox("Working Professional or Student", ["Working Professional", "Student"])
profession = st.text_input("Profession (if applicable)")

academic_pressure = st.slider("Academic Pressure (1-10)", 1, 10, 5)
work_pressure = st.slider("Work Pressure (1-10)", 1, 10, 5)
cgpa = st.number_input("CGPA (0.0 - 10.0)", min_value=0.0, max_value=10.0, step=0.1)
study_satisfaction = st.slider("Study Satisfaction (1-10)", 1, 10, 5)
job_satisfaction = st.slider("Job Satisfaction (1-10)", 1, 10, 5)
sleep_duration = st.slider("Average Sleep Duration (hours)", 0, 24, 7)
dietary_habits = st.selectbox("Dietary Habits", ["Healthy", "Unhealthy", "Moderate"])
degree = st.selectbox("Degree (Highest Attained)", ["High School", "Bachelor's", "Master's", "PhD", "Other"])
suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])
work_study_hours = st.slider("Work/Study Hours (per day)", 1, 24, 8)
financial_stress = st.slider("Financial Stress (1-10)", 1, 10, 5)
family_history = st.selectbox("Family history of depression?", ["Yes", "No"])

# Map inputs to feature vector
if user_type == "Working Professional":
    input_features = pd.DataFrame({
        'Job Satisfaction': [job_satisfaction],
        'Work Pressure': [work_pressure],
        'Financial Stress': [financial_stress],
        'Work/Study Hours': [work_study_hours]
    })
else:
    input_features = pd.DataFrame({
        'CGPA': [cgpa],
        'Academic Pressure': [academic_pressure],
        'Study Satisfaction': [study_satisfaction],
        'Work/Study Hours': [work_study_hours]
    })

# Prediction
if st.button("Predict"):
    if user_type == "Working Professional":
        prediction = prof_model.predict(input_features)[0]
    else:
        prediction = stud_model.predict(input_features)[0]

    # Display result
    if prediction == 1:
        st.error("Result: Depressed")
    else:
        st.success("Result: Not Depressed")
