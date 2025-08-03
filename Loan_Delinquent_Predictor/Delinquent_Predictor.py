import pickle
import pandas as pd


import streamlit as st
from streamlit_option_menu import option_menu


def initialize_model():
     global Loan_deli_model, feature_names
    # Open the pickle file for model
     Loan_deli_model = pickle.load(open('Loan_Delinquent_model.pkl', 'rb'))
    # Define correct feature names
     feature_names  = ["term_60 months", "gender_Male", "purpose_House", "purpose_Medical", "purpose_Other",
                                  "purpose_Personal", "purpose_Wedding", "home_ownership_Own", "home_ownership_Rent",
                                  "age_>25", "FICO_>500"]


     st.title("Loan Delinquent Prediction using ML")
     st.markdown("<h3><B>Type:</B> Type: </B> Classification </h3>", unsafe_allow_html=True)
     st.markdown("<h3><B>Model used:</B> Type: </B><I> Random Forest</I> </h3>", unsafe_allow_html=True)
     st.markdown('<BR>', unsafe_allow_html=True)


def get_and_prepare_input():
    # Check box to select Loan term
    term_option = st.checkbox("Loan Term - 60 months")
    # Radio button to select Gender
    gender_option = st.radio("Gender", ["Male", "Female"])
    # Drop down to select purpose
    purpose_selection = st.selectbox("Loan Purpose:", ["House", "Medical", "Other", "Personal", "Wedding"])
    # Drop down to select home ownership
    ownership_selection = st.selectbox("Home Ownership:", ["Own", "Rent"])
    # Checkbox to select age range
    age_option = st.checkbox("Age Above 25 years")
    # Checkbox to select FICO score
    FICO_option = st.checkbox("FICO Score >= 500")

    if term_option:
        term_60_months = 1
    else:
        term_60_months = 0


    if gender_option == "Male":
        gender_male = 1
    else:
        gender_male = 0


    purpose_House = purpose_Medical = purpose_Other = purpose_Personal = purpose_Wedding = 0
    match purpose_selection:
        case "House":
            purpose_House = 1
        case "Medical":
            purpose_Medical = 1
        case "Other":
            purpose_Other = 1
        case "Personal":
            purpose_Personal = 1
        case "Wedding":
            purpose_Wedding = 1


    home_ownership_Own = home_ownership_Rent = 0
    match ownership_selection:
        case "Own":
            home_ownership_Own = 1
        case "Rent":
            home_ownership_Rent = 1


    if age_option:
        age_25plus = 1
    else:
        age_25plus = 0


    if FICO_option:
        fico_500plus = 1
    else:
        fico_500plus = 0

    input_data = pd.DataFrame([[term_60_months, gender_male, purpose_House, purpose_Medical, purpose_Other,
                                purpose_Personal, purpose_Wedding, home_ownership_Own, home_ownership_Rent,
                                age_25plus, fico_500plus]], columns=feature_names)
    return input_data

def predict_outcome(input_pd):
    # Creating a button for prediction
    prediction_text = ""
    if st.button("Predict the output!!"):
          Loan_deli_prediction = Loan_deli_model.predict(input_pd)
          if Loan_deli_prediction[0] == 1:
            prediction_text = " This person will be Delinquent"
          else:
            prediction_text = " This person will NOT be Delinquent"

    st.success(prediction_text)

def run():
    initialize_model()
    input_features = get_and_prepare_input()
    st.markdown('<BR>', unsafe_allow_html=True)
    predict_outcome(input_features)