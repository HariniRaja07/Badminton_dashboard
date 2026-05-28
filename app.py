
import streamlit as st
import pandas as pd
import plotly.express as px
import random

# PAGE CONFIG

st.set_page_config(
    page_title="ALLIANCE GALLERIA",
    layout="wide"
)

# CUSTOM CSS

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1e3a8a;
}

.profile-box{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.1);
}

.metric-box{
    background:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 5px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# TITLE

st.markdown(
    "<div class='main-title'>🏸 ALLIANCE GALLERIA</div>",
    unsafe_allow_html=True
)

st.write("")

# COACH SECTION

col1, col2 = st.columns([1,2])

with col1:
    st.image("coach.jpg", width=220)

with col2:

    st.markdown("## BHARATHRAJ PILLAI")

    st.write("""
Professional Badminton Coach with 15+ years of coaching experience.

Specialized in:
- Match Strategy
- Fitness Training
- Footwork Improvement
- Player Development
- Tournament Coaching
""")

# LOAD EXCEL

df = pd.read_excel("badminton.xlsx")

students = list(df.columns[1:])

st.write("")
st.subheader("🏸 Student Performance Dashboard")

selected_student = st.selectbox(
    "Select Student",
    students
)

# FILTER DATA

criteria = df.iloc[:,0]
scores = df[selected_student]

student_df = pd.DataFrame({
    "Criteria": criteria,
    "Score": scores
})

student_df = student_df.dropna()

# KPI

average = round(student_df["Score"].mean(),1)

strong = len(student_df[student_df["Score"] >= 8])

weak = len(student_df[student_df["Score"] <= 4])

if average >= 8:
    level = "Excellent"

elif average >= 6:
    level = "Good"

else:
    level = "Developing"

# KPI DISPLAY

c1, c2, c3, c4 = st.columns(4)

c1.metric("Overall Score", f"{average}/10")
c2.metric("Strong Skills", strong)
c3.metric("Weak Skills", weak)
c4.metric("Performance", level)

st.write("")

# CHARTS

chart1 = px.bar(
    student_df,
    x="Criteria",
    y="Score",
    title="Performance Analysis"
)

st.plotly_chart(
    chart1,
    use_container_width=True
)

chart2 = px.line(
    student_df,
    x="Criteria",
    y="Score",
    markers=True,
    title="Skill Progress"
)

st.plotly_chart(
    chart2,
    use_container_width=True
)

chart3 = px.pie(
    student_df,
    names="Criteria",
    values="Score",
    title="Skill Distribution"
)

st.plotly_chart(
    chart3,
    use_container_width=True
)

chart4 = px.radar(
    student_df,
    r="Score",
    theta="Criteria"
)

# FEEDBACK

strengths = student_df[
    student_df["Score"] >= 8
]["Criteria"].tolist()

improvements = student_df[
    student_df["Score"] <= 4
]["Criteria"].tolist()

positive_lines = [

    "shows excellent match confidence.",
    "has strong court awareness.",
    "demonstrates excellent discipline.",
    "shows high badminton potential."
]

improvement_lines = [

    "needs more focused practice.",
    "can improve with additional training.",
    "requires better consistency.",
    "needs more movement control."
]

feedback = ""

if strengths:

    feedback += (
        selected_student
        + " performs strongly in "
        + ", ".join(strengths[:3])
        + " and "
        + random.choice(positive_lines)
        + " "
    )

if improvements:

    feedback += (
        "Areas to improve include "
        + ", ".join(improvements[:3])
        + ". "
        + random.choice(improvement_lines)
    )

st.subheader("🏸 AI Coach Feedback")

st.success(feedback)

# PARENT FEEDBACK

st.subheader("👨‍👩‍👧 Parent Feedback")

parent_name = st.text_input("Parent Name")

parent_feedback = st.text_area(
    "Enter Feedback"
)

if st.button("Submit Feedback"):

    st.success(
        "Feedback Submitted Successfully ✅"
    )

# DOWNLOAD REPORT

csv = student_df.to_csv(index=False)

st.download_button(
    label="📄 Download Report",
    data=csv,
    file_name=f"{selected_student}_report.csv",
    mime="text/csv"
)
```
