import streamlit as st
from datetime import datetime

def generate_report(query, answer):
    report = f"""
AI MEDICAL ASSISTANT REPORT
----------------------------

Date: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

User Query:
{query}

AI Response:
{answer}

Disclaimer:
This report is for educational purposes only.
Please consult a doctor for professional advice.
"""
    return report

def download_report_button(query, answer):
    report = generate_report(query, answer)

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="medical_report.txt",
        mime="text/plain"
    )