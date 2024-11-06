import streamlit as st
st.set_page_config(
    page_title="MindCare",
    page_icon="🧠",
    initial_sidebar_state="collapsed"
)

from student_predict_page import show_predict_page

show_predict_page()