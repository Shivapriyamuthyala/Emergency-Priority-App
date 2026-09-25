🚑 Emergency Patient Priority System

An AI-assisted emergency triage and patient prioritization system built using Python and Streamlit. The application predicts the priority level of an emergency case based on the patient's age and severity level and organizes patients in a treatment queue.

📌 Overview

The Emergency Patient Priority System is designed to support emergency patient prioritization.

The application accepts:

- Patient Name
- Patient Age
- Severity Level (1–10)

Based on the patient's age and severity, the system assigns one of three priority levels:

- 🔴 High Priority
- 🟡 Medium Priority
- 🟢 Low Priority

Patients are then organized in a treatment queue with high-priority cases displayed first.

✨ Features

- Patient information input
- Emergency severity assessment
- Automatic priority prediction
- High, Medium, and Low priority classification
- Heap-based emergency queue
- Treatment queue displaying high-priority patients first
- Admin dashboard
- Priority distribution bar chart
- Interactive Streamlit interface

🧠 Priority Prediction

The current priority logic is:

| Condition | Priority |
|---|---|
| Severity ≥ 8 OR Age ≥ 70 | 🔴 High |
| Severity ≥ 4 | 🟡 Medium |
| Severity < 4 | 🟢 Low |

🔄 Application Workflow

```text
Patient Information
        ↓
Age + Severity Level
        ↓
Priority Prediction
        ↓
High / Medium / Low
        ↓
Emergency Queue
        ↓
Treatment Queue
        ↓
Admin Dashboard

The application includes an admin dashboard that displays the number of:

- Low-priority patients
- Medium-priority patients
- High-priority patients

The priority distribution is visualized using a bar chart.

🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/Shivapriyamuthyala/Emergency-Priority-App.git


```markdown
2. Navigate to the project directory

```bash
cd Emergency-Priority-App

3. Install the required dependencies

```bash
pip install -r requirements.txt

▶️ Run the Application

Run the following command:

```bash
streamlit run app.py

The application will open in your web browser.

📁 Main Files

`app.py`

Contains the Streamlit user interface, patient input form, priority result, treatment queue, and admin dashboard.

`model.py`

Contains the priority prediction logic based on patient age and severity.

`dsa.py`

Implements the emergency queue using a heap-based data structure.

`requirements.txt`

Contains the Python dependencies required to run the application.

🎯 Project Objectives

- Develop an interactive emergency patient prioritization system.
- Apply Data Structures and Algorithms to emergency queue management.
- Provide an automated priority classification mechanism.
- Visualize the distribution of emergency priorities.
- Demonstrate the use of Python and Streamlit in a healthcare-oriented application.

⚠️ Disclaimer

This project is developed for educational and demonstration purposes. The priority classification should not be used as a substitute for professional medical judgment or clinical triage.

👩‍💻 Author

**Muthyala Shiva Priya**

GitHub: https://github.com/Shivapriyamuthyala