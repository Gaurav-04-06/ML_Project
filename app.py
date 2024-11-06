import streamlit as st
st.set_page_config(
    page_title="MindCare",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from PIL import Image
import base64

# Custom CSS for layout styling
st.markdown(
    """
    <style>
    /* Background color */
    .main {
        background-color: #f0f4f8; /* Light blue-grey color */
    }
    
    /* Container for the image and text */
    .flex-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        margin: 20px 0;
    }

    /* Styling for the image */
    .flex-container img {
        max-width: 45%; /* Adjust to fit half of the container */
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Styling for the text */
    .flex-container .text-content {
        max-width: 50%; /* Adjust width as needed */
        margin-left: 20px;
        font-size: 18px; /* Increased font size */
        line-height: 1.8;
    }

    /* Center align for titles */
    h1 {
        text-align: center;
        font-weight: bold;
        color: #FFFFFF;
        font-size: 5rem;
    }

    h2 {
        text-align: center;
        font-weight: bold;
        color: #FFFFFF;
        font-size: 40px;
    }

    h3 {
        text-align: center;
        font-weight: bold;
        color: #FFFFFF;
        font-size: 32px;
    }

    /* Styling for section text */
    .section-header {
        font-size: 30px; /* Increased size for section headers */
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
    }

    .section-text {
        font-size: 30px; /* Increased size for regular text */
        color: #FFFFFF;
    }

    .text-content p{
        font-size: 25px; /* Increased size for regular text */
        color: #FFFFFF;
    }
    

    </style>
    """,
    unsafe_allow_html=True
)

# Display the title and a welcome message
st.title("MindCare")
st.subheader("Mental Health Prediction Platform")

# Function to load and encode image in base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load and display the styled image alongside text
image_path = "mental_health_image.jpg"
image_base64 = get_image_base64(image_path)
st.markdown(
    f"""
    <div class="flex-container">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Mental Health Image"/>
        <div class="text-content">
            <p>Welcome to MindCare. This tool is designed to 
            help identify potential signs of mental health challenges among professionals and students.
            By providing personalized assessments, we aim to promote mental health awareness and encourage 
            proactive support.</p>
        </div>
        <br/><br/>
    </div>
    
    """,
    unsafe_allow_html=True
)

# Sections Overview
st.markdown('<div class="section-header"><br/> Navigate to Different Sections: <br/><br/></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-text">
    -Professionals' Mental Health Prediction: Analyze how work-related factors such as job satisfaction, work pressure, and financial stress contribute to mental health status.<br/>
    -Students' Mental Health Prediction: Examine the influence of academic pressure, CGPA, and study satisfaction on mental health.<br/>
    -Insights and Resources: Access articles, tips, and resources for maintaining mental well-being.<br/>
    </div>
    <br/><br/>
    """,
    unsafe_allow_html=True
)

# Call to Action
st.markdown('<div class="section-header">How to Use This Platform:</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-text">
    1. Navigate to the Professionals or Students page using the sidebar.<br>
    2. Enter the required information for analysis.<br>
    3. View the prediction and gain insights into your mental health status.
    <br/><br/>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-text">Your well-being matters! Stay informed and take steps toward a healthier mind.</div>', unsafe_allow_html=True)

# Contact Information
st.write("---")
st.markdown(
    '<div class="section-text">For any assistance or further information, contact us at: <a href="mailto:support@mentalhealthplatform.com">support@mentalhealthplatform.com</a></div>',
    unsafe_allow_html=True
)