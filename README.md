# 🏦 Loan Approval Prediction App

A Machine Learning-powered web app that predicts whether a bank loan will be approved based on applicant details. Built using Python, Scikit-learn, and Streamlit, and deployed on Streamlit Cloud.

---

🌐 Live Demo
👉 https://loan-prediction-app-laa.streamlit.app/



## 🚀 Features

- 🔍 User-friendly Streamlit web interface
- 📊 Real-time predictions using a trained ML pipeline
- ✅ Clean pre-processing with ColumnTransformer + Pipeline
- 📁 Modular code structure with joblib model loading
- ☁️ One-click deployment on Streamlit Cloud

---

## 🧠 Model Details

- **Training Dataset**: Loan Prediction from Analytics Vidhya
- **Features Used**:
  - Gender, Marital Status, Dependents
  - Education, Self-Employment
  - Income, Loan Amount, Loan Term
  - Credit History, Property Area
- **Models Tested**:
  - Logistic Regression ✅ (best performance)
  - Random Forest
  - Decision Tree

---

## 🖼️ App UI Screenshot

![Loan Approval App UI](images/screenshot.png)

---

## 📦 How to Run Locally

### 🔧 Prerequisites
- Python 3.8 or higher
- Git

### 🛠️ Installation Steps

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/loan-prediction-app.git
cd loan-prediction-app

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py


