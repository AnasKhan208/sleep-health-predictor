import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Sleep Health Predictor",
    page_icon="😴",
    layout="centered"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("sleep_health_model.pkl")


model = load_model()


# =========================================================
# TITLE
# =========================================================

st.title("😴 Sleep Health Predictor")

st.write(
    "Enter your lifestyle and health information "
    "to predict the possible sleep-disorder category."
)

st.caption(
    "Machine Learning Based Sleep Health Classification"
)

st.divider()


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.subheader("📊 Model Performance")

# ---------------------------------------------------------
# IMPORTANT:
# Replace these values with your ACTUAL Colab results.
# ---------------------------------------------------------

accuracy = 0.9467
precision = 0.9491
recall = 0.9467
f1_score_value = 0.9463


# Metric cards

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{accuracy * 100:.2f}%"
)

col2.metric(
    "Precision",
    f"{precision * 100:.2f}%"
)

col3.metric(
    "Recall",
    f"{recall * 100:.2f}%"
)

col4.metric(
    "F1 Score",
    f"{f1_score_value * 100:.2f}%"
)


# Performance chart

metrics = {
    "Accuracy": accuracy,
    "Precision": precision,
    "Recall": recall,
    "F1 Score": f1_score_value
}

fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.bar(
    metrics.keys(),
    metrics.values()
)

ax.set_ylim(0, 1.05)
ax.set_ylabel("Score")
ax.set_title("Final Model Performance")

for bar, value in zip(bars, metrics.values()):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.02,
        f"{value * 100:.1f}%",
        ha="center",
        fontsize=10
    )

st.pyplot(fig)

st.caption(
    "Performance metrics are calculated using the held-out test dataset."
)

st.divider()


# =========================================================
# USER INPUT
# =========================================================

st.subheader("🧑 Enter Your Information")


# Gender

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


# Age

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30,
    step=1
)


# Occupation

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


# Sleep Duration

sleep_duration = st.number_input(
    "Sleep Duration (hours)",
    min_value=1.0,
    max_value=15.0,
    value=7.0,
    step=0.1
)


# Quality of Sleep

quality_of_sleep = st.slider(
    "Quality of Sleep",
    min_value=1,
    max_value=10,
    value=7
)


# Physical Activity

physical_activity = st.number_input(
    "Physical Activity Level",
    min_value=0,
    max_value=150,
    value=50,
    step=1
)


# Stress Level

stress_level = st.slider(
    "Stress Level",
    min_value=1,
    max_value=10,
    value=5
)


# BMI

bmi_category = st.selectbox(
    "BMI Category",
    [
        "Normal",
        "Overweight",
        "Obese"
    ]
)


# Heart Rate

heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=40,
    max_value=150,
    value=70,
    step=1
)


# Daily Steps

daily_steps = st.number_input(
    "Daily Steps",
    min_value=0,
    max_value=30000,
    value=5000,
    step=100
)


# =========================================================
# BLOOD PRESSURE
# =========================================================

st.subheader("🩺 Blood Pressure")

col1, col2 = st.columns(2)

with col1:

    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=70,
        max_value=250,
        value=120,
        step=1
    )

with col2:

    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=40,
        max_value=150,
        value=80,
        step=1
    )


st.divider()


# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button(
    "🔍 Predict Sleep Disorder",
    use_container_width=True
):

    # -----------------------------------------------------
    # Create input dataframe
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # Prediction
    # -----------------------------------------------------

    prediction = model.predict(input_data)[0]


    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    st.divider()

    st.subheader("🔮 Prediction Result")


    if prediction == "None":

        st.success(
            "✅ No Sleep Disorder predicted"
        )

    elif prediction == "Insomnia":

        st.warning(
            "⚠️ Insomnia predicted"
        )

    elif prediction == "Sleep Apnea":

        st.error(
            "⚠️ Sleep Apnea predicted"
        )

    else:

        st.info(
            f"Prediction: {prediction}"
        )


    # -----------------------------------------------------
    # PREDICTION PROBABILITY
    # -----------------------------------------------------

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]


        probability_df = pd.DataFrame({

            "Category": model.classes_,

            "Probability": probabilities

        })


        probability_df["Probability (%)"] = (
            probability_df["Probability"] * 100
        ).round(2)


        st.subheader(
            "📈 Prediction Probability"
        )


        # Bar chart

        chart_data = probability_df[
            ["Category", "Probability"]
        ].set_index("Category")


        st.bar_chart(
            chart_data
        )


        # Table

        st.dataframe(
            probability_df[
                ["Category", "Probability (%)"]
            ],
            hide_index=True,
            use_container_width=True
        )


# =========================================================
# DISCLAIMER
# =========================================================

st.divider()

st.info(
    "⚠️ This application is an educational machine-learning "
    "project and is not a medical diagnostic tool."
)

st.caption(
    "Sleep Health & Lifestyle Classification Project"
)
