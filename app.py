import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("sleep_health_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Sleep Health Predictor",
    page_icon="😴",
    layout="centered"
)

# Title
st.title("😴 Sleep Health Predictor")
st.write(
    "Enter your lifestyle and health information "
    "to predict the possible sleep-disorder category."
)

st.divider()

# -----------------------------
# User Inputs
# -----------------------------

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

occupation = st.selectbox(
    "Occupation",
    [
        "Accountant",
        "Doctor",
        "Engineer",
        "Lawyer",
        "Manager",
        "Nurse",
        "Sales Representative",
        "Scientist",
        "Software Engineer",
        "Teacher"
    ]
)

sleep_duration = st.number_input(
    "Sleep Duration (hours)",
    min_value=1.0,
    max_value=15.0,
    value=7.0,
    step=0.1
)

quality_of_sleep = st.slider(
    "Quality of Sleep",
    min_value=1,
    max_value=10,
    value=7
)

physical_activity = st.number_input(
    "Physical Activity Level",
    min_value=0,
    max_value=150,
    value=50
)

stress_level = st.slider(
    "Stress Level",
    min_value=1,
    max_value=10,
    value=5
)

bmi_category = st.selectbox(
    "BMI Category",
    ["Normal", "Overweight", "Obese"]
)

heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=40,
    max_value=150,
    value=70
)

daily_steps = st.number_input(
    "Daily Steps",
    min_value=0,
    max_value=30000,
    value=5000
)

st.subheader("Blood Pressure")

systolic_bp = st.number_input(
    "Systolic Blood Pressure",
    min_value=70,
    max_value=250,
    value=120
)

diastolic_bp = st.number_input(
    "Diastolic Blood Pressure",
    min_value=40,
    max_value=150,
    value=80
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🔍 Predict Sleep Disorder", use_container_width=True):

    input_data = pd.DataFrame({
        "Gender": [gender],
        "Age": [age],
        "Occupation": [occupation],
        "Sleep Duration": [sleep_duration],
        "Quality of Sleep": [quality_of_sleep],
        "Physical Activity Level": [physical_activity],
        "Stress Level": [stress_level],
        "BMI Category": [bmi_category],
        "Heart Rate": [heart_rate],
        "Daily Steps": [daily_steps],
        "Systolic_BP": [systolic_bp],
        "Diastolic_BP": [diastolic_bp]
    })

    prediction = model.predict(input_data)[0]

    # Prediction result
    st.divider()
    st.subheader("Prediction Result")

    if prediction == "None":
        st.success("✅ No Sleep Disorder predicted")

    elif prediction == "Insomnia":
        st.warning("⚠️ Insomnia predicted")

    elif prediction == "Sleep Apnea":
        st.error("⚠️ Sleep Apnea predicted")

    else:
        st.info(f"Prediction: {prediction}")

    # Probability
    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(input_data)[0]

        probability_df = pd.DataFrame({
            "Category": model.classes_,
            "Probability": probabilities
        })

        probability_df["Probability"] = (
            probability_df["Probability"] * 100
        ).round(2)

        st.subheader("Prediction Probability")

        st.bar_chart(
            probability_df.set_index("Category")
        )

        st.dataframe(
            probability_df,
            hide_index=True,
            use_container_width=True
        )

st.divider()

st.caption(
    "⚠️ This application is an educational machine-learning project "
    "and is not a medical diagnostic tool."
)
