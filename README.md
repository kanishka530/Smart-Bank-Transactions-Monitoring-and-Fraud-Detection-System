# 🛡️ Financial Fraud Detection: A Multivariate Statistical Approach

### 🎓 Academic Context
This project was developed during my final semester of **B.Sc. Mathematics** to demonstrate the practical application of Stochastic Modeling and Ensemble Learning in Financial Technology (FinTech).

### 🚀 Executive Summary
The goal was to engineer a robust classification system capable of identifying fraudulent credit card transactions within a highly imbalanced dataset (0.17% fraud rate). By prioritizing **Recall** over simple Accuracy, the model ensures maximum security while minimizing customer friction.

### 📊 Statistical Results & Optimization
- **92.8% Recall:** Successfully identified 91 out of 98 fraud cases in the hold-out test set.
- **13% Precision Optimization:** Transitioned from a Linear Baseline (Logistic Regression) to a **Random Forest Ensemble** (100 Decision Trees). This reduced False Positives by nearly 300 cases, directly improving the "False Alarm" rate for customers.
- **Data Resampling:** Implemented **Random Under-Sampling** to address class imbalance, creating a balanced 50/50 training distribution to prevent model bias toward the majority class.

### 🛠️ Tech Stack & Methodology
- **Languages:** Python (Pandas for data manipulation, NumPy for vectorization)
- **Machine Learning:** Scikit-Learn (RandomForestClassifier, LogisticRegression)
- **Evaluation Metrics:** Confusion Matrix analysis, Precision-Recall curves, and F1-Score.
- **Deployment:** **Streamlit** (Real-time inference dashboard for risk monitoring).

### 📂 Repository Structure
- `/data`: Source CSV and processed datasets.
- `/notebooks`: Exploratory Data Analysis (EDA) and Model Training pipeline.
- `/dashboard`: Production-ready `app.py` and the serialized `fraud_model.pkl`.
- `requirements.txt`: Environment configuration for reproducibility.

### 🧪 Execution Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Launch the UI: `cd dashboard && streamlit run app.py`

### 📂 Data Source
The dataset used in this project is the **Credit Card Fraud Detection** dataset from Kaggle. 
- **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Scale:** 284,807 transactions with 30 numerical features ($V1-V28$, Time, and Amount).

---

