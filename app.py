import streamlit as st
from model import predict_priority
from dsa import EmergencyQueue
import pandas as pd

# App config
st.set_page_config(
    page_title="Emergency Patient Priority System",
    layout="centered"
)

# Initialize queue (session-safe)
if "queue" not in st.session_state:
    st.session_state.queue = EmergencyQueue()

queue = st.session_state.queue

# ---------- HEADER ----------
st.title("🚑 Emergency Patient Priority System")
st.write("AI-assisted emergency triage and prioritization system")

st.divider()

# ---------- INPUT FORM ----------
with st.form("patient_form"):
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    severity = st.slider("Severity Level (1–10)", 1, 10)

    submitted = st.form_submit_button("Predict Priority")

if submitted:
    priority = predict_priority(age, severity)
    queue.add_patient(name, priority)

    if priority == 2:
        st.error("🔴 HIGH PRIORITY – Immediate care required")
    elif priority == 1:
        st.warning("🟡 MEDIUM PRIORITY – Needs attention soon")
    else:
        st.success("🟢 LOW PRIORITY – Stable condition")

# ---------- QUEUE DISPLAY ----------
st.divider()
st.subheader("🧾 Treatment Queue (High Priority First)")

data = queue.get_all()

if data:
    df = pd.DataFrame(data, columns=["Priority", "Patient Name"])
    df["Priority"] = df["Priority"].map({
    2: "High",
    1: "Medium",
    0: "Low"})
    st.dataframe(df, use_container_width=True)

else:
    st.info("No patients in queue yet")

# ---------- DASHBOARD ----------
st.divider()
st.subheader("📊 Admin Dashboard")

priorities = [p[0] for p in data]

if priorities:
    chart_data = pd.DataFrame({
        "Priority": ["Low", "Medium", "High"],
        "Count": [
            priorities.count(0),
            priorities.count(1),
            priorities.count(2)
        ]
    })
    st.bar_chart(chart_data.set_index("Priority"))
else:
    st.info("No data available for dashboard")
