import streamlit as st
from datetime import datetime

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🩺",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f9ff;
}
.stButton>button {
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}
.stDownloadButton>button {
    background: linear-gradient(90deg,#00b09b,#96c93d);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🩺 AI Health Assistant")
st.write("### Personal Details + BMI Calculator + Advanced Symptom Checker + Download Report")

# ---------------------------------------------------
# REPORT FUNCTION
# ---------------------------------------------------
def generate_report(name, age, gender, bmi_result, severity_result, disease_result):
    report = f"""
AI HEALTH ASSISTANT REPORT
====================================

Date: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

Patient Name : {name}
Age          : {age}
Gender       : {gender}

------------------------------------
BMI RESULT
------------------------------------
{bmi_result}

------------------------------------
SYMPTOM SEVERITY
------------------------------------
{severity_result}

------------------------------------
POSSIBLE CONDITION
------------------------------------
{disease_result}

------------------------------------
HEALTH TIPS
------------------------------------
• Drink enough water
• Exercise daily
• Eat healthy food
• Sleep 7-8 hours
• Consult doctor if needed

------------------------------------
DISCLAIMER
------------------------------------
Educational purpose only.
Consult doctor for medical advice.
"""
    return report

# ---------------------------------------------------
# PERSONAL DETAILS
# ---------------------------------------------------
st.header("👤 Personal Details")

p1, p2, p3 = st.columns(3)

with p1:
    name = st.text_input("Enter Name")

with p2:
    age = st.number_input("Enter Age", min_value=1, max_value=120, step=1)

with p3:
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])

st.markdown("---")

# ---------------------------------------------------
# DEFAULT VALUES
# ---------------------------------------------------
bmi_result = "Not Calculated"
severity_result = "Not Checked"
disease_result = "Not Checked"

# ---------------------------------------------------
# MAIN 2 COLUMNS
# ---------------------------------------------------
col1, col2 = st.columns(2)

# ===================================================
# BMI CALCULATOR
# ===================================================
with col1:
    st.header("⚖️ BMI Calculator")

    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.5)
    height = st.number_input("Height (cm)", min_value=1.0, step=0.5)

    if st.button("Calculate BMI"):
        h = height / 100
        bmi = weight / (h ** 2)

        if bmi < 18.5:
            bmi_result = f"BMI = {bmi:.2f} (Underweight)"
            st.warning(bmi_result)
            st.info("💡 Eat healthy food, nuts, milk, fruits.")

        elif bmi < 25:
            bmi_result = f"BMI = {bmi:.2f} (Normal)"
            st.success(bmi_result)
            st.info("💡 Keep exercising and maintain diet.")

        elif bmi < 30:
            bmi_result = f"BMI = {bmi:.2f} (Overweight)"
            st.warning(bmi_result)
            st.info("💡 Reduce oily foods and start walking daily.")

        else:
            bmi_result = f"BMI = {bmi:.2f} (Obese)"
            st.error(bmi_result)
            st.info("💡 Consult doctor, exercise regularly.")

# ===================================================
# ADVANCED SYMPTOM CHECKER
# ===================================================
with col2:
    st.header("🤒 Symptom Checker")

    fever = st.selectbox("Fever?", ["No", "Yes"])
    vomiting = st.selectbox("Vomiting?", ["No", "Yes"])
    loose_motion = st.selectbox("Loose Motions?", ["No", "Yes"])
    body_pain = st.selectbox("Body Pain?", ["No", "Yes"])
    watery_eyes = st.selectbox("Watery Eyes?", ["No", "Yes"])
    throat_pain = st.selectbox("Throat Pain?", ["No", "Yes"])
    cough = st.selectbox("Cough?", ["No", "Yes"])
    headache = st.selectbox("Headache?", ["No", "Yes"])
    breathing = st.selectbox("Breathing Problem?", ["No", "Yes"])
    cold = st.selectbox("Cold / Sneezing?", ["No", "Yes"])
    stomach_pain = st.selectbox("Stomach Pain?", ["No", "Yes"])
    tiredness = st.selectbox("Tiredness?", ["No", "Yes"])

    if st.button("Analyze Symptoms"):

        score = 0

        symptoms = [
            fever, vomiting, loose_motion, body_pain,
            watery_eyes, throat_pain, cough,
            headache, cold, stomach_pain, tiredness
        ]

        for s in symptoms:
            if s == "Yes":
                score += 1

        if breathing == "Yes":
            score += 2

        # Severity
        if score <= 3:
            severity_result = "Mild Symptoms 🙂"
            st.success(severity_result)

        elif score <= 6:
            severity_result = "Moderate Symptoms 😷"
            st.warning(severity_result)

        else:
            severity_result = "Severe Symptoms 🚨 Consult Doctor Immediately"
            st.error(severity_result)

        # Disease Detection
        st.subheader("🔍 Possible Condition")

        if fever == "Yes" and body_pain == "Yes" and headache == "Yes":
            disease_result = "Possible Viral Fever / Dengue"
            st.warning(disease_result)

        elif throat_pain == "Yes" and cough == "Yes" and fever == "Yes":
            disease_result = "Possible Cold / Throat Infection"
            st.warning(disease_result)

        elif loose_motion == "Yes" and vomiting == "Yes":
            disease_result = "Possible Food Poisoning"
            st.warning(disease_result)

        elif watery_eyes == "Yes" and cold == "Yes":
            disease_result = "Possible Allergy"
            st.warning(disease_result)

        elif breathing == "Yes" and cough == "Yes":
            disease_result = "Possible Asthma / Respiratory Problem"
            st.error(disease_result)

        elif fever == "Yes" and cough == "Yes":
            disease_result = "Possible Flu / Viral Infection"
            st.warning(disease_result)

        elif stomach_pain == "Yes" and vomiting == "Yes":
            disease_result = "Possible Gastric / Stomach Infection"
            st.warning(disease_result)

        elif tiredness == "Yes" and headache == "Yes":
            disease_result = "Possible Stress / Weakness"
            st.warning(disease_result)

        else:
            disease_result = "No major disease pattern detected."
            st.success(disease_result)

# ---------------------------------------------------
# DOWNLOAD REPORT
# ---------------------------------------------------
st.markdown("---")
st.header("📄 Download Full Report")

report = generate_report(
    name,
    age,
    gender,
    bmi_result,
    severity_result,
    disease_result
)

st.download_button(
    label="⬇️ Download Report",
    data=report,
    file_name="Health_Report.txt",
    mime="text/plain"
)

# ---------------------------------------------------
# HEALTH TIPS
# ---------------------------------------------------
st.markdown("---")
st.header("💡 Daily Health Tips")

tips = [
    "💧 Drink 8 glasses of water daily",
    "🏃 Exercise 30 mins every day",
    "😴 Sleep at least 7 hours",
    "🍎 Eat fruits and vegetables",
    "🧘 Reduce stress with meditation",
    "🧼 Wash hands regularly",
    "🚶 Walk after meals",
    "🚫 Avoid smoking and alcohol"
]

for tip in tips:
    st.success(tip)

# ---------------------------------------------------
# USER SUMMARY
# ---------------------------------------------------
st.markdown("---")

if name:
    st.success(f"👤 Patient Name: {name}")
    st.info(f"Age: {age} | Gender: {gender}")

# ---------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------
st.warning("⚠️ This tool gives basic suggestions only. Please consult a doctor for accurate diagnosis.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.info("Made with ❤️ using Streamlit | AI Health Assistant")