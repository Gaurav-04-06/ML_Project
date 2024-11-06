 # Prepare data for saving
        import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load model function
def load_model():
    with open('prof_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load the model
data = load_model()
model = data["model"]
features_list = data.get("features_list" , None)

# Create a label encoder for categorical features
label_encoders = {
    'financial_stress': LabelEncoder(),
    'dietary_habits': LabelEncoder(),
    'suicidal_thoughts': LabelEncoder(),
    'family_history': LabelEncoder()
}

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Background color */
    .main {
        background-color: #FFFFF; 
    }
    
    /* Title styling */
    h1 {
        text-align: center;
        color: #FFFFFF;
        font-size: 3rem;
    }

    /* Result styling */
    .result {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def show_professional_predict_page():
    st.title("MindCare - Mental Health Prediction")
    st.write("Please fill in the following details:")

    # Collecting User Information
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.slider("Age", 18, 80, 30)
    city = st.text_input("City")
    
    # Professional and Lifestyle Information
    profession = st.text_input("Profession")
    work_pressure = st.slider("Work Pressure (1-10)", 1, 10, 5)
    job_satisfaction = st.slider("Job Satisfaction (1-10)", 1, 10, 5)
    sleep_hours = st.slider("Sleep Hours", 1, 12, 7)
    dietary_habits = st.selectbox("Dietary Habits", ["Healthy", "Moderate", "Unhealthy"])
    
    # Additional Information
    degree = st.text_input("Degree")  
    suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])
    work_hours = st.slider("Work Hours per Day", 1, 16, 8)
    financial_stress = st.selectbox("Financial Stress", ["High", "Moderate", "Low"])
    family_history = st.selectbox("Family History of Depression", ["Yes", "No"])

    # When the user clicks the 'Predict' button, show results
    if st.button("Predict"):
        # Encode categorical variables
        encoded_features = [
            job_satisfaction,
            work_pressure,
            label_encoders['financial_stress'].fit_transform([financial_stress])[0],
            work_hours
        ]
        
        features = np.array([encoded_features])
        prediction = model.predict(features)

        # Scale and display prediction result
        scaled_prediction = round(prediction[0] * 10, 1)
        
        # Conditional formatting based on prediction score
        if scaled_prediction > 8:
            color = "red"
        elif scaled_prediction > 5:
            color = "orange"
        else:
            color = "green"

        # Display the result with the corresponding color
        st.markdown(f"<div class='result' style='color: {color};'>Depression Likelihood Score: {scaled_prediction}</div>", unsafe_allow_html=True)

        # Prepare data for saving
        user_data = {
            "Name": name,
            "Gender": gender,
            "Age": age,
            "City": city,
            "Profession": profession,
            "Work Pressure": work_pressure,
            "Job Satisfaction": job_satisfaction,
            "Sleep Hours": sleep_hours,
            "Dietary Habits": dietary_habits,
            "Degree": degree,
            "Suicidal Thoughts": suicidal_thoughts,
            "Work Hours": work_hours,
            "Financial Stress": financial_stress,
            "Family History": family_history,
            "Prediction Score": scaled_prediction
        }

        # # Convert to DataFrame and save to CSV
        # df = pd.DataFrame([user_data])  # Create DataFrame from the user data
        # df.to_csv('user_data.csv', mode='a', header=False, index=False)  # Append data to CSV

        # st.success("User data saved to 'user_data.csv'.")
        