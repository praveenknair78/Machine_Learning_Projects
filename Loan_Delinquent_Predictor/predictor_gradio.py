import pickle
import gradio as gr
import pandas as pd

Loan_deli_model = pickle.load(open('Loan_Delinquent_model.pkl', 'rb'))

# Define correct feature names
feature_names = ["term_60 months", "gender_Male", "purpose_House", "purpose_Medical","purpose_Other","purpose_Personal"
                 ,"purpose_Wedding","home_ownership_Own","home_ownership_Rent","age_>25", "FICO_>500"]

#define predict function
def predict(term_option,gender_option,purpose_selection,ownership_selection, age_option,FICO_option):

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

    input_data = pd.DataFrame([[term_60_months, gender_male, purpose_House,purpose_Medical, purpose_Other,
                                purpose_Personal,purpose_Wedding, home_ownership_Own, home_ownership_Rent,
                                age_25plus, fico_500plus]], columns=feature_names)

    Loan_deli_prediction = Loan_deli_model.predict(input_data)
    if Loan_deli_prediction[0] == 1:
        prediction_text = " This person will be Delinquent"
    else:
        prediction_text = " This person will NOT be Delinquent"

    return prediction_text


with gr.Blocks() as app:
    gr.Markdown("# 🚀 Loan Delinquent Prediction")  # Main Header
    gr.Markdown("### Using ML classification model.")  # Sub-header

    term_option =  gr.Checkbox(label="Loan Term - 60 months")
    gender_option = gr.Radio(["Male", "Female"], label="Gender")
    purpose_selection = gr.Dropdown(["House", "Medical", "Other", "Personal", "Wedding"], label="Loan Purpose")
    ownership_selection =gr.Dropdown(["Own", "Rent"], label="Home Ownership")
    age_option = gr.Checkbox(label="Age Above 25 years")
    FICO_option = gr.Checkbox(label="FICO Score>500")

    submit_btn = gr.Button("Predict the outcome!!")
    output = gr.Textbox(label="Output")
    submit_btn.click(fn=predict, inputs=[term_option , gender_option,purpose_selection,ownership_selection,
                                         age_option,FICO_option], outputs=output)

app.launch()

