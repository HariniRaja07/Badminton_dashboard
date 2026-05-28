import streamlit as st
import pandas as pd
import plotly.express as px
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="ALLIANCE GALLERIA",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#eef2ff,#f8fafc);
}

/* TITLE */

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#1e3a8a;
    margin-bottom:20px;
}

/* HERO SECTION */

.hero-box{
    background:white;
    padding:35px;
    border-radius:22px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom:30px;
}

/* KPI CARDS */

.metric-card{
    background:linear-gradient(135deg,#2563eb,#1d4ed8);
    padding:25px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
    margin-bottom:15px;
}

.metric-title{
    font-size:18px;
    font-weight:500;
}

.metric-value{
    font-size:34px;
    font-weight:bold;
}

/* CHART BOX */

.chart-box{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

/* FEEDBACK */

.feedback-box{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.markdown(
    "<div class='main-title'>🏸 ALLIANCE GALLERIA</div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

with st.container():

    col1, col2 = st.columns([1,2])

    with col1:

        st.image("coach.jpg", width=240)

    with col2:

        st.markdown("## BHARATHRAJ PILLAI")

        st.write("""
Professional badminton coach with 15+ years of coaching excellence.

### Coaching Expertise
- Match Strategy Development
- Tournament Preparation
- Fitness & Endurance Training
- Technical Skill Development
- Footwork & Court Coverage
- Player Performance Analytics

Dedicated to developing discipline, confidence, leadership,
mental strength, and advanced badminton performance.
""")

# ---------------------------------------------------
# LOAD EXCEL
# ---------------------------------------------------

df = pd.read_excel("badminton.xlsx")

students = list(df.columns[1:])

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🏸 Student Dashboard")

selected_student = st.sidebar.selectbox(
    "Select Student",
    students
)

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------

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

# ---------------------------------------------------
# SPLIT DATA FOR DIFFERENT CHARTS
# ---------------------------------------------------

movement_df = student_df.iloc[0:5]

technical_df = student_df.iloc[5:10]

fitness_df = student_df.iloc[10:15]

mental_df = student_df.iloc[15:20]

advanced_df = student_df.iloc[20:25]

# ---------------------------------------------------
# KPI CALCULATIONS
# ---------------------------------------------------

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

# ---------------------------------------------------
# STUDENT HEADER
# ---------------------------------------------------

st.markdown("---")

st.subheader(
    f"🏸 {selected_student} Performance Dashboard"
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

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

# ---------------------------------------------------
# CHARTS
# ---------------------------------------------------

st.write("")

col1, col2 = st.columns(2)

with col1:

    fig1 = px.bar(
        movement_df,
        x="Criteria",
        y="Score",
        color="Score",
        title="Movement Skills Analytics"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = px.line(
        technical_df,
        x="Criteria",
        y="Score",
        markers=True,
        title="Technical Skills Analysis"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ---------------------------------------------------

col3, col4 = st.columns(2)

with col3:

    fig3 = px.area(
        fitness_df,
        x="Criteria",
        y="Score",
        title="Fitness & Court Coverage"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col4:

    fig4 = px.pie(
        mental_df,
        names="Criteria",
        values="Score",
        title="Mental Strength & Discipline"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ---------------------------------------------------
# RADAR CHART
# ---------------------------------------------------

st.subheader("🏸 Advanced Performance Metrics")

fig5 = px.line_polar(
    advanced_df,
    r="Score",
    theta="Criteria",
    line_close=True
)

fig5.update_traces(fill='toself')

st.plotly_chart(
    fig5,
    use_container_width=True
)

# ---------------------------------------------------
# DETAILED AI FEEDBACK
# ---------------------------------------------------

strengths = student_df[
    student_df["Score"] >= 8
]["Criteria"].tolist()

improvements = student_df[
    student_df["Score"] <= 5
]["Criteria"].tolist()

overall_lines = [

    "shows strong dedication towards badminton development and maintains impressive consistency during training sessions.",

    "demonstrates excellent discipline and positive learning attitude during badminton coaching activities.",

    "has shown stable performance improvement across multiple badminton performance indicators.",

    "maintains strong interest and active involvement during advanced badminton practice sessions."
]

strength_lines = [

    "The student performs strongly in {} and demonstrates excellent tactical awareness during rallies.",

    "Strong performance has been observed in {}, indicating excellent technical understanding and confidence.",

    "The student consistently performs well in {}, reflecting advanced badminton potential.",

    "Excellent performance is visible in {}, showing strong focus and skill execution."
]

improvement_lines = [

    "Additional improvement is recommended in {} to strengthen overall tournament consistency.",

    "Focused training sessions in {} can improve advanced competitive performance.",

    "The student can further improve overall gameplay by strengthening {} through regular practice.",

    "Further technical refinement in {} can help improve defensive recovery and match stability."
]

future_lines = [

    "With continuous coaching and regular training, the student has strong district-level tournament potential.",

    "The student demonstrates excellent long-term badminton growth opportunities and competitive capability.",

    "Current performance trends indicate strong future possibilities in advanced badminton competitions.",

    "Regular advanced training and structured coaching can help the student achieve higher performance levels."
]

overall_feedback = random.choice(overall_lines)

strength_feedback = random.choice(
    strength_lines
).format(
    ", ".join(strengths[:4])
)

improvement_feedback = random.choice(
    improvement_lines
).format(
    ", ".join(improvements[:4])
)

future_feedback = random.choice(future_lines)

# ---------------------------------------------------
# FEEDBACK DISPLAY
# ---------------------------------------------------

st.markdown("---")

st.subheader(
    "🏸 Intelligent AI Performance Report"
)

st.info(overall_feedback)

st.success(strength_feedback)

st.warning(improvement_feedback)

st.success(future_feedback)

# ---------------------------------------------------
# PARENT FEEDBACK
# ---------------------------------------------------

st.markdown("---")

st.subheader("👨‍👩‍👧 Parent Feedback")

parent_name = st.text_input(
    "Enter Parent Name"
)

parent_feedback = st.text_area(
    "Enter Parent Feedback"
)

if st.button("Submit Feedback"):

    st.success(
        "Feedback Submitted Successfully ✅"
    )

# ---------------------------------------------------
# DOWNLOAD REPORT
# ---------------------------------------------------

csv = student_df.to_csv(index=False)

st.download_button(
    label="📄 Download Personalized Report",
    data=csv,
    file_name=f"{selected_student}_report.csv",
    mime="text/csv"
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown("""
<center>

© 2026 ALLIANCE GALLERIA

Professional Badminton Performance Analytics System

</center>
""", unsafe_allow_html=True)
