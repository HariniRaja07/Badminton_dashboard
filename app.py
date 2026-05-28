
import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(
    page_title="ALLIANCE GALLERIA",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

body{
    background-color:#f4f7fe;
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1e3a8a;
    margin-bottom:20px;
}

.hero{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    margin-bottom:30px;
}

.metric-card{
    background:white;
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
}

.metric-title{
    color:#64748b;
    font-size:18px;
}

.metric-value{
    color:#2563eb;
    font-size:32px;
    font-weight:bold;
}

.feedback-box{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown(
    "<div class='main-title'>🏸 ALLIANCE GALLERIA</div>",
    unsafe_allow_html=True
)

# ---------------- HERO SECTION ---------------- #

col1, col2 = st.columns([1,2])

with col1:

    st.image("coach.jpg", width=230)

with col2:

    st.markdown("## BHARATHRAJ PILLAI")

    st.write("""
Professional badminton coach with 15+ years of coaching excellence.

### Expertise
- Match Strategy
- Footwork Training
- Tournament Preparation
- Fitness Development
- Technical Skill Coaching
- Advanced Player Analytics
""")

    st.info(
        "Dedicated to building discipline, confidence, stamina, leadership and tournament-level performance."
    )

# ---------------- LOAD EXCEL ---------------- #

df = pd.read_excel("badminton.xlsx")

students = list(df.columns[1:])

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🏸 Navigation")

selected_student = st.sidebar.selectbox(
    "Select Student",
    students
)

st.sidebar.success(
    f"Selected: {selected_student}"
)

# ---------------- FILTER DATA ---------------- #

criteria = df.iloc[:,0]

scores = df[selected_student]

student_df = pd.DataFrame({
    "Criteria": criteria,
    "Score": scores
})

student_df = student_df.dropna()

student_df["Score"] = pd.to_numeric(
    student_df["Score"],
    errors="coerce"
)

student_df = student_df.dropna()

# ---------------- KPI CALCULATIONS ---------------- #

average = round(student_df["Score"].mean(),1)

strong = len(
    student_df[
        student_df["Score"] >= 8
    ]
)

weak = len(
    student_df[
        student_df["Score"] <= 4
    ]
)

if average >= 8:
    level = "Excellent"

elif average >= 6:
    level = "Good"

else:
    level = "Developing"

# ---------------- STUDENT HEADER ---------------- #

st.markdown("---")

st.subheader(f"🏸 {selected_student} Performance Dashboard")

# ---------------- KPI SECTION ---------------- #

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            Overall Score
        </div>

        <div class="metric-value">
            {average}/10
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            Strong Skills
        </div>

        <div class="metric-value">
            {strong}
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            Improvement Areas
        </div>

        <div class="metric-value">
            {weak}
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            Performance
        </div>

        <div class="metric-value">
            {level}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- CHARTS ---------------- #

tab1, tab2, tab3, tab4 = st.tabs([
    "Movement Analytics",
    "Technical Skills",
    "Fitness Analysis",
    "Overall Distribution"
])

with tab1:

    fig1 = px.bar(
        student_df,
        x="Criteria",
        y="Score",
        color="Score",
        title="Movement Skills Analytics"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with tab2:

    fig2 = px.line(
        student_df,
        x="Criteria",
        y="Score",
        markers=True,
        title="Technical Skills Analysis"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

with tab3:

    fig3 = px.area(
        student_df,
        x="Criteria",
        y="Score",
        title="Fitness & Court Coverage"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with tab4:

    fig4 = px.pie(
        student_df,
        names="Criteria",
        values="Score",
        title="Overall Skill Distribution"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ---------------- RADAR CHART ---------------- #

st.subheader("🏸 Advanced Performance Metrics")

fig5 = px.line_polar(
    student_df,
    r="Score",
    theta="Criteria",
    line_close=True
)

fig5.update_traces(fill='toself')

st.plotly_chart(
    fig5,
    use_container_width=True
)

# ---------------- AI FEEDBACK ---------------- #

strengths = student_df[
    student_df["Score"] >= 8
]["Criteria"].tolist()

improvements = student_df[
    student_df["Score"] <= 4
]["Criteria"].tolist()

positive_lines = [

    "shows excellent court awareness.",
    "demonstrates strong match confidence.",
    "has excellent badminton potential.",
    "maintains strong discipline during practice.",
    "shows impressive tactical understanding."
]

improvement_lines = [

    "needs more movement stability.",
    "requires additional focused practice.",
    "can improve with advanced training.",
    "needs stronger rally consistency.",
    "requires better defensive recovery."
]

future_lines = [

    "Has strong future tournament potential.",
    "Can become a high-level competitive player.",
    "Shows excellent long-term growth potential.",
    "Can perform strongly in advanced competitions."
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
        "Areas requiring improvement include "
        + ", ".join(improvements[:3])
        + ". "
        + random.choice(improvement_lines)
        + " "
    )

feedback += random.choice(future_lines)

st.markdown("""
<div class="feedback-box">
<h3>🏸 Intelligent Coach Feedback</h3>
</div>
""", unsafe_allow_html=True)

st.success(feedback)

# ---------------- PARENT FEEDBACK ---------------- #

st.subheader("👨‍👩‍👧 Parent Feedback")

parent_name = st.text_input(
    "Enter Parent Name"
)

parent_feedback = st.text_area(
    "Enter Feedback"
)

if st.button("Submit Feedback"):

    st.success(
        "Feedback Submitted Successfully ✅"
    )

# ---------------- DOWNLOAD ---------------- #

csv = student_df.to_csv(index=False)

st.download_button(
    label="📄 Download Personalized Report",
    data=csv,
    file_name=f"{selected_student}_report.csv",
    mime="text/csv"
)

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown("""
<center>
© 2026 ALLIANCE GALLERIA |
Professional Badminton Performance Analytics
</center>
""", unsafe_allow_html=True)

