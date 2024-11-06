# import streamlit as st
# import pickle

# # Load model function
# def load_model():
#     with open('stud_model.pkl', 'rb') as file:
#         data = pickle.load(file)
#     return data

# data = load_model()
# model = data["model"]


# # Load the model
# data = load_model()
# model = data["model"]

# # Custom CSS for styling
# st.markdown("""
#     <style>
#         /* Background color */
#         .main {
#             background-color: #FFFFF; 
#         }
        
#         /* Title styling */
#         h1 {
#             text-align: center;
#             color: #FFFFFF;
#             font-size: 3rem;
#         }

#         /* Subheader styling */
#         .sub-title {
#             text-align: center;
#             color: #FFFFFF;
#             font-size: 1.5rem; /* Ensuring subtitle size is consistent */
#             margin-top: 20px; /* Add spacing above subtitles */
#         }

#         /* Form field styling */
#         .stTextInput, .stSlider, .stSelectbox {
#             padding: 8px;
#         }

#         /* Button styling */
#         .stButton-button {
#             background-color: #00838f;
#             color: white;
#             border-radius: 8px;
#             padding: 10px 20px;
#             font-size: 18px;
#         }

#         /* Result display styling */
#         .result {
#             text-align: center;
#             font-size: 3rem; /* Matching the font size of other results */
#             font-weight: bold;
#             color: #d32f2f;
#             margin-top: 20px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# def show_predict_page():
#     # Display main title with consistent font size using HTML
#     st.markdown("<h1>MindCare - Mental Health Prediction</h1>", unsafe_allow_html=True)
#     st.write("Please fill in the following details:")

#     # Personal Information Section with subtitle styling
#     name = st.text_input("Name")
#     gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#     age = st.slider("Age", 10, 80, 18)
#     city = st.text_input("City")

#     # Academic and Lifestyle Information Section
#     academic_pressure = st.slider("Academic Pressure", 1, 10, 5)
#     cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1, value=7.0)
#     study_satisfaction = st.slider("Study Satisfaction", 1, 10, 5)
#     sleep_duration = st.slider("Sleep Duration (hours)", 1, 12, 7)
#     dietary_habits = st.selectbox("Dietary Habits", ["Healthy", "Moderate", "Unhealthy"])

#     # Additional Information Section
#     degree = st.text_input("Degree")
#     suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])
#     study_hours = st.slider("Study Hours per Day", 1, 12, 4)
#     financial_stress = st.selectbox("Financial Stress", ["High", "Moderate", "Low"])
#     family_history = st.selectbox("Family History of Depression", ["Yes", "No"])

#     # Prediction Button
#     if st.button("Predict"):
#         # Prepare data for prediction
#         features = [[cgpa, academic_pressure, study_satisfaction, study_hours]]
#         prediction = model.predict(features)

#         # Scale and display prediction result
#         scaled_prediction = round(prediction[0] * 10, 1)
        
#         # Conditional formatting based on prediction score
#         if scaled_prediction > 8:
#             color = "red"
#         elif scaled_prediction > 5:
#             color = "orange"
#         else:
#             color = "green"
#          # Display the result with the corresponding color
#         st.markdown(f"<div class='result' style='color: {color};'>Depression Likelihood Score: {scaled_prediction}</div>", unsafe_allow_html=True)   