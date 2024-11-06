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
features_list = data.get("features_list")

# st.write("Feature list: " , features_list)

# # Create a label encoder for categorical features
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

    /* Subheader styling */
    h2 {
        text-align: center;
        color: #004d40;
        font-size: 3rem;
    }

    /* Result styling */
    .result {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #d32f2f;
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
        # encoded_features = [
        #     job_satisfaction,
        #     work_pressure,
        #     label_encoders['financial_stress'].fit_transform([financial_stress])[0],
        #     work_hours
        # ]

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
        }

        input_df = pd.DataFrame([user_data])

        # Encode categorical variables consistently
        input_df['Financial Stress'] = label_encoders['financial_stress'].fit_transform(input_df['Financial Stress'])
        input_df['Dietary Habits'] = label_encoders['dietary_habits'].fit_transform(input_df['Dietary Habits'])
        input_df['Suicidal Thoughts'] = label_encoders['suicidal_thoughts'].fit_transform(input_df['Suicidal Thoughts'])
        input_df['Family History'] = label_encoders['family_history'].fit_transform(input_df['Family History'])

    # Drop the original columns
        input_df = input_df.drop(['Financial Stress', 'Dietary Habits', 'Suicidal Thoughts', 'Family History'], axis=1)

        # Create dummy variables for categorical columns
        categorical_cols = ['Gender', 'City', 'Profession', 'Degree']
        input_df = pd.get_dummies(input_df, columns=categorical_cols)

        # st.write("Original input_df columns:", input_df.columns.tolist())
        # st.write("Features required by the model:", features_list)

        missing_columns = set(features_list) - set(input_df.columns)
        extra_columns = set(input_df.columns) - set(features_list)

        # st.write("Missing columns:", list(missing_columns))
        # st.write("Extra columns:", list(extra_columns))

        # Instead of setting missing columns to 0, we'll only add columns that are categorical
        for col in missing_columns:
            if col.startswith(tuple(categorical_cols)):
                input_df[col] = 0

        # Remove any extra columns not needed by the model
        input_df = input_df[input_df.columns.intersection(features_list)]

        # Check if any required columns are still missing
        still_missing = set(features_list) - set(input_df.columns)
        if still_missing:
            st.error(f"Error: The following required features are missing: {still_missing}")
            return

        # st.write("Final input_df columns:", input_df.columns.tolist())
        # st.write("Input df:", input_df)

        # Ensure the order of columns matches the order expected by the model
        input_df = input_df[features_list]

        # st.write("Final input_df (ordered):", input_df)

        # features = np.array([encoded_features])
        prediction = model.predict(input_df)
        # st.write(type(prediction))
        st.write("predictions: " , str(prediction))

        # Scale and display prediction result
        scaled_prediction = round(prediction[0] * 10, 1)
        st.markdown(f"<div class='result'>Depression Likelihood Score: {scaled_prediction}</div>", unsafe_allow_html=True)     