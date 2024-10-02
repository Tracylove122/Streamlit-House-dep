#streamlit web file
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="Predicting House Price"
)
with st.sidebar:
    selected=option_menu(
        menu_title=None,
        options=["Home","Prediction","Dashbord"],
        icons=["house","Unsplash",""],
        menu_icon="cast",
        default_index=0
    )