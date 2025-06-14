import streamlit as st
import joblib
import pandas as pd

# Load model pipeline (with preprocessing + model)
model = joblib.load('model/loan_model_pipeline.pkl')

# Add logo/image at the top
st.image('https://raw.githubusercontent.com/yourusername/yourrepo/main/logo.png', width=150)  # Replace URL or local path

st.title("🏦 Loan Approval Prediction App")

# Brief project description
st.write("""
Welcome to the Loan Approval Prediction App!  
This app uses machine learning to predict whether a loan application will be approved based on applicant details.  
Enter the relevant information in the sidebar and click **Predict** to get the result.
""")

# Sidebar inputs
st.sidebar.header("Applicant Details")

gender = st.sidebar.selectbox("Gender", ['Male', 'Female'])
married = st.sidebar.selectbox("Married", ['Yes', 'No'])
dependents = st.sidebar.selectbox("Dependents", ['0', '1', '2', '3+'])
education = st.sidebar.selectbox("Education", ['Graduate', 'Not Graduate'])
self_employed = st.sidebar.selectbox("Self Employed", ['Yes', 'No'])
applicant_income = st.sidebar.number_input("Applicant Income", min_value=0)
coapplicant_income = st.sidebar.number_input("Coapplicant Income", min_value=0)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0)
loan_term = st.sidebar.number_input("Loan Term (in days)", min_value=0)
credit_history = st.sidebar.selectbox("Credit History", [1.0, 0.0])
property_area = st.sidebar.selectbox("Property Area", ['Urban', 'Rural', 'Semiurban'])

if st.sidebar.button("Predict"):
    input_dict = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]

    if prediction == 'Y':
        st.success("✅ Congratulations! Loan Approved")
    else:
        st.error("❌ Sorry, Loan Not Approved")

    # Optional: Show prediction probability
    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba(input_df)[0]
        st.write(f"Approval Probability: {proba[1]*100:.2f}%")
