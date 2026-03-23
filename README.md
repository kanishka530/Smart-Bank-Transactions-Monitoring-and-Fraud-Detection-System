# 🏦 Smart Bank Transaction Monitoring System
**Status: 🟡 Development Phase (Data Preprocessing)**

A Python-based fraud detection system designed to identify suspicious financial activities and patterns of money laundering (AML) using the ULB Credit Card Fraud dataset.

## 🚀 Project Overview
This project focuses on identifying fraudulent transactions from a highly imbalanced dataset. It involves Exploratory Data Analysis (EDA), handling class imbalance via undersampling, and implementing machine learning models to ensure transaction integrity.

## 📁 Dataset Information
Due to GitHub's **100MB file size limit**, the raw `creditcard.csv` (143.84 MB) is excluded from this repository via `.gitignore`. 

**To run this project, please download the dataset from Kaggle:**
🔗 [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

* **Total Transactions:** 284,807
* **Fraudulent Cases:** 492 (0.172% of total)
* **Features:** PCA-transformed numerical features (V1-V28), Time, and Amount.

## 🛠️ Roadmap & Milestones
- [x] **Project Setup:** Repository architecture and Git configuration.
- [x] **Data Audit:** Initial EDA and class distribution analysis.
- [x] **Data Splitting:** 80/20 Train-Test split.
- [ ] **Class Balancing:** Implementing Undersampling to handle 0.17% fraud ratio.
- [ ] **Model Building:** Training and evaluating Logistic Regression.
- [ ] **Dashboard:** Visualizing fraud triggers and threshold reports.

## ⚙️ Setup Instructions
1. Clone this repository.
2. Download `creditcard.csv` from the link above and place it in the `/data` folder.
3. Open `notebook/fraud_analysis.ipynb` to view the analysis.