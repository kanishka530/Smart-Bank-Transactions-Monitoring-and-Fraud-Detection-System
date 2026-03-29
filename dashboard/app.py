import streamlit as st
import joblib
import numpy as np

# 1. Load the "Brain" we saved earlier
model = joblib.load('fraud_model.pkl')

# 2. Set the Title of our Website
st.set_page_config(page_title="SmartBank Fraud Detector", layout="centered")
st.title("🛡️ SmartBank: AI Transaction Monitor")
st.write("Enter the transaction details below to check for suspicious activity.")

# 3. Create the Input Boxes (The "Risk Sliders")
# Since we have 30 features, we'll just test a few key ones for now
st.subheader("Transaction Clues")

v17 = st.number_input("V17 (Key Fraud Indicator)", value=0.0)
v14 = st.number_input("V14 (The 'Snitch' Feature)", value=0.0)
amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=10.0)

# 4. The "Check" Button
if st.button("Analyze Transaction"):
    # We create a fake 'row' of data to feed the model
    # (In a real app, we'd provide all 30 features, but let's test with 3)
    # We fill the rest with zeros for this simple test
    features = np.zeros(30) 
    features[17] = v17 # V17
    features[14] = v14 # V14
    features[29] = amount # Amount
    
    prediction = model.predict([features])
    probability = model.predict_proba([features])[0][1]

    # 5. Show the Results
    st.divider()
    if prediction[0] == 1:
        st.error(f"🚨 ALERT: High Risk of Fraud! (Probability: {probability:.2%})")
        st.warning("Recommendation: Freeze account and contact customer.")
    else:
        st.success(f"✅ Transaction Verified. (Fraud Probability: {probability:.2%})")
        st.balloons()