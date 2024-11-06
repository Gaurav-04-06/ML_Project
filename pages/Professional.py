import streamlit as st
st.set_page_config(
    page_title="MindCare",
    page_icon="🧠",
    initial_sidebar_state="collapsed"
)
import pandas as pd
from professional_predict_page import show_professional_predict_page

show_professional_predict_page()