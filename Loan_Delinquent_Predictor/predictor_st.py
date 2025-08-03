import pandas as pd
import Delinquent_Predictor as dp


import streamlit as st
from streamlit_option_menu import option_menu

#Setup Window Title and Page title
st.set_page_config(page_title="ML Models Demo")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")


# Setup Sidebar menu and style it
with st.sidebar:
    selected = option_menu(menu_title="ML Models Menu",menu_icon="None",default_index=0,
                           options=['Loan Delinquent Prediction'],icons=['award-fill'],
                           styles={ "container": {"padding": "0!important", "background-color": "#ffffe6"},
                                    "icon": {"color": "orange", "font-size": "15px"},
                                    "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0px",
                                                 "--hover-color": "#eee", },
                                    "nav-link-selected": {"background-color": "green"},}
                           )

# Get the selection and route it to right functions
if selected == 'Loan Delinquent Prediction':
    dp.run()