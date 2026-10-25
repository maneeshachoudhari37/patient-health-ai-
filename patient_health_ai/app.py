import streamlit as st
import pickle

# Load trained model
with open("patient_risk_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏥 Patient Health Early Warning System")

st.write("Enter the patient's health information below.")

# Patient details
patient_id = st.text_input("Patient ID")
age = st.number_input("Age", min_value=1, max_value=120, value=30)

heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=30,
    max_value=200,
    value=75
)

spo2 = st.number_input(
    "SpO₂ (%)",
    min_value=50,
    max_value=100,
    value=98
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=30.0,
    max_value=45.0,
    value=36.5
)

systolic_bp = st.number_input(
    "Systolic BP",
    min_value=60,
    max_value=250,
    value=120
)

diastolic_bp = st.number_input(
    "Diastolic BP",
    min_value=40,
    max_value=150,
    value=80
)

# Analyze button
if st.button("🔍 Analyze Patient"):

    input_data = [[
        age,
        heart_rate,
        spo2,
        temperature,
        systolic_bp,
        diastolic_bp
    ]]

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == "Low":
        st.success("🟢 LOW RISK")

    elif prediction == "Medium":
        st.warning("🟡 MEDIUM RISK")

    else:
        st.error("🔴 HIGH RISK")
        st.error("⚠️ Early Warning: Patient requires attention.")

    st.info(f"Patient ID: {patient_id}")
    