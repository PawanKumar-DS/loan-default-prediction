# \# 🏦 Loan Default Prediction

# 

# A Machine Learning project that predicts the probability of a customer defaulting on a loan using a Random Forest Classifier.

# 

# \## 📌 Project Overview

# 

# Loan default prediction helps financial institutions identify customers who may have a higher risk of defaulting on their loans.

# 

# In this project, customer financial and personal information is analyzed and a Machine Learning model is trained to predict loan default.

# 

# \## 🎯 Objective

# 

# The main objective of this project is to:

# 

# \- Analyze loan customer data

# \- Perform data preprocessing and exploratory data analysis

# \- Train multiple Machine Learning classification models

# \- Compare model performance

# \- Select the best-performing model

# \- Build a Streamlit application for real-time prediction

# 

# \## 🛠️ Technologies Used

# 

# \- Python

# \- Pandas

# \- NumPy

# \- Matplotlib

# \- Seaborn

# \- Scikit-learn

# \- XGBoost

# \- Joblib

# \- Streamlit

# \- Jupyter Notebook

# 

# \## 🤖 Machine Learning Models

# 

# The following models were evaluated:

# 

# \- Logistic Regression

# \- Decision Tree Classifier

# \- Random Forest Classifier

# \- XGBoost Classifier

# 

# The \*\*Random Forest Classifier\*\* was selected as the final model based on the F1 Score among the evaluated models.

# 

# \## 📊 Model Performance

# 

# | Metric | Score |

# |---|---:|

# | Accuracy | 77.54% |

# | Precision | 26.99% |

# | Recall | 54.76% |

# | F1 Score | 36.16% |

# 

# \## 📂 Project Structure

# 

# ```text

# loan-default-prediction/

# │

# ├── App/

# │   └── app.py

# │

# ├── Data/

# │   └── archive/

# │       └── Loan\_default.csv

# │

# ├── Models/

# │   ├── feature\_columns.pkl

# │   ├── random\_forest\_model.pkl

# │   └── scaler.pkl

# │

# ├── Notebook/

# │   └── loan\_Default\_prediction.ipynb

# │

# ├── .gitignore

# ├── README.md

# └── requirements.txt



# 🚀 Streamlit Application

# 

# The project includes a Streamlit web application where users can enter customer information and get a loan default prediction.

# 

# The application provides:

# 

# Customer information input

# Default probability

# Risk level

# Prediction result

# Downloadable prediction report

# Risk Levels

# 🟢 Low Risk — Below 30%

# 🟡 Medium Risk — 30% to 60%

# 🔴 High Risk — Above 60%













# ▶️ How to Run the Project





# 1️⃣ Clone the repository

# git clone https://github.com/PawanKumar-DS/loan-default-prediction.git







# 2️⃣ Go to the project directory

# cd loan-default-prediction





# 3️⃣ Install dependencies

# pip install -r requirements.txt





# 4️⃣ Run the Streamlit application

# streamlit run App/app.py







# 📓 Notebook

# 

# The complete data analysis, preprocessing, exploratory data analysis, model training, evaluation and model saving steps are available in:

# 

# Notebook/loan\_Default\_prediction.ipynb

# 

# 

