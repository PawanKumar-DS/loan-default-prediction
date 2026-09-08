import streamlit as st
import joblib
import os
import pandas as pd


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Loan Default Prediction",
    page_icon="🏦",
    layout="wide"
)


# ==========================================
# Load Model and Feature Columns
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

model_path = os.path.join(
    BASE_DIR,
    "Models",
    "random_forest_model.pkl"
)

feature_path = os.path.join(
    BASE_DIR,
    "Models",
    "feature_columns.pkl"
)

model = joblib.load(model_path)

feature_columns = joblib.load(feature_path)


# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("🏦 Loan Default Prediction")

st.sidebar.write("### About the Project")

st.sidebar.write(
    "This application predicts the likelihood "
    "of a customer defaulting on a loan using "
    "a Machine Learning model."
)

st.sidebar.write("### Model")

st.sidebar.write(
    "Random Forest Classifier"
)

st.sidebar.write("### Risk Levels")

st.sidebar.write(
    "🟢 Low Risk: Below 30%"
)

st.sidebar.write(
    "🟡 Medium Risk: 30% - 60%"
)

st.sidebar.write(
    "🔴 High Risk: Above 60%"
)


# ==========================================
# App Title
# ==========================================

st.title("🏦 Loan Default Prediction")

st.write(
    "Enter customer information to predict "
    "the likelihood of loan default."
)


# ==========================================
# Customer Information
# ==========================================

st.header("👤 Customer Information")

col1, col2 = st.columns(2)


# ==========================================
# Column 1
# ==========================================

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    income = st.number_input(
        "Income",
        min_value=0,
        value=50000
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=100000
    )

    months_employed = st.number_input(
        "Months Employed",
        min_value=0,
        value=60
    )

    num_credit_lines = st.number_input(
        "Number of Credit Lines",
        min_value=0,
        value=3
    )


# ==========================================
# Column 2
# ==========================================

with col2:

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=850,
        value=650
    )

    interest_rate = st.number_input(
        "Interest Rate",
        min_value=0.0,
        max_value=100.0,
        value=10.0
    )

    loan_term = st.number_input(
        "Loan Term (Months)",
        min_value=1,
        value=36
    )

    dti_ratio = st.number_input(
        "DTI Ratio",
        min_value=0.0,
        max_value=100.0,
        value=20.0
    )


# ==========================================
# Additional Information
# ==========================================

st.header("📋 Additional Information")

col3, col4 = st.columns(2)


# ==========================================
# Column 3
# ==========================================

with col3:

    education = st.selectbox(
        "Education",
        [
            "High School",
            "Bachelor's",
            "Master's",
            "PhD"
        ]
    )

    employment_type = st.selectbox(
        "Employment Type",
        [
            "Full-time",
            "Part-time",
            "Self-employed",
            "Unemployed"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

    has_mortgage = st.selectbox(
        "Has Mortgage?",
        [
            "Yes",
            "No"
        ]
    )


# ==========================================
# Column 4
# ==========================================

with col4:

    has_dependents = st.selectbox(
        "Has Dependents?",
        [
            "Yes",
            "No"
        ]
    )

    loan_purpose = st.selectbox(
        "Loan Purpose",
        [
            "Auto",
            "Business",
            "Education",
            "Home",
            "Other"
        ]
    )

    has_cosigner = st.selectbox(
        "Has Co-Signer?",
        [
            "Yes",
            "No"
        ]
    )


# ==========================================
# Create Input DataFrame
# ==========================================

input_data = pd.DataFrame({

    "Age": [age],

    "Income": [income],

    "LoanAmount": [loan_amount],

    "CreditScore": [credit_score],

    "MonthsEmployed": [months_employed],

    "NumCreditLines": [num_credit_lines],

    "InterestRate": [interest_rate],

    "LoanTerm": [loan_term],

    "DTIRatio": [dti_ratio],

    "Education": [education],

    "EmploymentType": [employment_type],

    "MaritalStatus": [marital_status],

    "HasMortgage": [has_mortgage],

    "HasDependents": [has_dependents],

    "LoanPurpose": [loan_purpose],

    "HasCoSigner": [has_cosigner]

})


# ==========================================
# Buttons
# ==========================================

st.header("🔍 Prediction")

col5, col6 = st.columns(2)


with col5:

    predict_button = st.button(
        "🔍 Predict Loan Default",
        use_container_width=True
    )


with col6:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True
    )


# ==========================================
# Reset Button
# ==========================================

if reset_button:

    st.rerun()


# ==========================================
# Prediction
# ==========================================

if predict_button:

    # --------------------------------------
    # Customer Input Summary
    # --------------------------------------

    st.subheader("📋 Customer Input Summary")

    st.dataframe(
        input_data,
        use_container_width=True
    )


    # --------------------------------------
    # Encode Categorical Variables
    # --------------------------------------

    input_encoded = pd.get_dummies(
        input_data
    )


    # --------------------------------------
    # Match Training Columns
    # --------------------------------------

    input_encoded = input_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )


    # --------------------------------------
    # Make Prediction
    # --------------------------------------

    prediction = model.predict(
        input_encoded
    )[0]


    # --------------------------------------
    # Get Probability
    # --------------------------------------

    probability = model.predict_proba(
        input_encoded
    )[0][1]


    # ======================================
    # Prediction Result
    # ======================================

    st.subheader("🎯 Prediction Result")


    if probability < 0.30:

        risk_level = "Low Risk"

        st.success(
            "🟢 LOW RISK"
        )

        st.write(
            "The customer has a low estimated "
            "probability of loan default."
        )


    elif probability < 0.60:

        risk_level = "Medium Risk"

        st.warning(
            "🟡 MEDIUM RISK"
        )

        st.write(
            "The customer has a moderate estimated "
            "probability of loan default."
        )


    else:

        risk_level = "High Risk"

        st.error(
            "🔴 HIGH RISK"
        )

        st.write(
            "The customer has a high estimated "
            "probability of loan default."
        )


    # ======================================
    # Default Probability
    # ======================================

    st.metric(
        "Default Probability",
        f"{probability:.2%}"
    )

    st.progress(
        probability
    )


    # ======================================
    # Download Prediction Report
    # ======================================

    st.subheader("📥 Prediction Report")


    result_data = pd.DataFrame({

        "Prediction": [
            "Default" if prediction == 1
            else "No Default"
        ],

        "Risk Level": [
            risk_level
        ],

        "Default Probability": [
            f"{probability:.2%}"
        ]

    })


    csv_data = result_data.to_csv(
        index=False
    )


    st.download_button(
        label="📥 Download Prediction Report",

        data=csv_data,

        file_name="loan_prediction_report.csv",

        mime="text/csv"
    )


# ==========================================
# Risk Level Guide
# ==========================================

st.header("📌 Risk Level Guide")

risk_col1, risk_col2, risk_col3 = st.columns(3)


with risk_col1:

    st.success("🟢 LOW RISK")

    st.write(
        "Default Probability: Below 30%"
    )


with risk_col2:

    st.warning("🟡 MEDIUM RISK")

    st.write(
        "Default Probability: 30% - 60%"
    )


with risk_col3:

    st.error("🔴 HIGH RISK")

    st.write(
        "Default Probability: Above 60%"
    )


# ==========================================
# Model Performance
# ==========================================

st.header("📊 Model Performance")

col7, col8, col9, col10 = st.columns(4)


with col7:

    st.metric(
        "Accuracy",
        "77.54%"
    )


with col8:

    st.metric(
        "Precision",
        "26.99%"
    )


with col9:

    st.metric(
        "Recall",
        "54.76%"
    )


with col10:

    st.metric(
        "F1 Score",
        "36.16%"
    )
# ==========================================
# Dataset Information
# ==========================================

st.header("📊 Dataset Information")

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.metric(
        "Total Rows",
        "255,347"
    )

with info_col2:
    st.metric(
        "Total Features",
        "16"
    )


# ==========================================
# Model Information
# ==========================================

st.header("🤖 Model Information")

model_col1, model_col2 = st.columns(2)

with model_col1:
    st.write("**Algorithm:** Random Forest Classifier")

with model_col2:
    st.write("**Task:** Loan Default Classification")

# ==========================================
# Disclaimer
# ==========================================

st.divider()

st.caption(
    "⚠️ Disclaimer: This prediction is generated "
    "by a Machine Learning model for educational "
    "and demonstration purposes only. It should "
    "not be used as the sole basis for financial "
    "or lending decisions."
)