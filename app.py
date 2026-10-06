import streamlit as st
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #f5f7fa;
        text-align: center;
        margin-bottom: 10px;
    }

    .suggestion {
        padding: 15px;
        border-radius: 10px;
        background-color: #f5f7fa;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    '<div class="main-title">🎓 Student Performance Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze academic performance using Python</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# SIDEBAR - STUDENT INPUT
# --------------------------------------------------
st.sidebar.header("📝 Student Information")

name = st.sidebar.text_input(
    "Student Name",
    placeholder="Enter student name"
)

math = st.sidebar.number_input(
    "Mathematics Marks",
    min_value=0,
    max_value=100,
    value=50
)

science = st.sidebar.number_input(
    "Science Marks",
    min_value=0,
    max_value=100,
    value=50
)

english = st.sidebar.number_input(
    "English Marks",
    min_value=0,
    max_value=100,
    value=50
)

attendance = st.sidebar.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

study_hours = st.sidebar.slider(
    "Study Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=2.0,
    step=0.5
)

analyze = st.sidebar.button(
    "🔍 Analyze Performance",
    use_container_width=True
)

# --------------------------------------------------
# DEFAULT MESSAGE
# --------------------------------------------------
if not analyze:
    st.info(
        "👈 Enter the student's information from the sidebar "
        "and click **Analyze Performance**."
    )

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------
if analyze:

    if name.strip() == "":
        st.error("⚠️ Please enter the student's name.")
        st.stop()

    # Calculations
    total = math + science + english
    average = total / 3

    # Grade
    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    # Result
    if average >= 40:
        result = "PASS ✅"
    else:
        result = "FAIL ❌"

    # Performance level
    if average >= 80:
        performance = "Excellent 🌟"
    elif average >= 60:
        performance = "Good 👍"
    elif average >= 40:
        performance = "Average 📚"
    else:
        performance = "Needs Improvement 💪"

    # --------------------------------------------------
    # STUDENT NAME
    # --------------------------------------------------
    st.subheader(f"👤 Performance Report: {name}")

    # --------------------------------------------------
    # METRICS
    # --------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Marks", f"{total}/300")
    col2.metric("Average", f"{average:.2f}%")
    col3.metric("Grade", grade)
    col4.metric("Attendance", f"{attendance}%")

    st.divider()

    # --------------------------------------------------
    # RESULT INFORMATION
    # --------------------------------------------------
    left, right = st.columns(2)

    with left:
        st.subheader("📋 Student Summary")

        st.write(f"**Student Name:** {name}")
        st.write(f"**Mathematics:** {math}/100")
        st.write(f"**Science:** {science}/100")
        st.write(f"**English:** {english}/100")
        st.write(f"**Study Hours:** {study_hours} hours/day")
        st.write(f"**Result:** {result}")
        st.write(f"**Performance:** {performance}")

    # --------------------------------------------------
    # PERFORMANCE CHART
    # --------------------------------------------------
    with right:
        st.subheader("📊 Subject Performance")

        subjects = ["Mathematics", "Science", "English"]
        marks = [math, science, english]

        fig, ax = plt.subplots(figsize=(7, 4))

        ax.bar(subjects, marks)

        ax.set_ylim(0, 100)
        ax.set_ylabel("Marks")
        ax.set_xlabel("Subjects")
        ax.set_title("Subject-wise Marks")

        st.pyplot(fig)

    st.divider()

    # --------------------------------------------------
    # PERFORMANCE PROGRESS
    # --------------------------------------------------
    st.subheader("📈 Overall Performance")

    st.progress(
        min(int(average), 100)
    )

    st.write(f"Overall Score: **{average:.2f}%**")

    # --------------------------------------------------
    # SUGGESTIONS
    # --------------------------------------------------
    st.subheader("💡 Personalized Suggestions")

    if average >= 80:
        st.success(
            "🌟 Excellent performance! Keep maintaining your current "
            "study routine and continue practicing."
        )

    elif average >= 60:
        st.info(
            "👍 Good performance! Focus more on difficult topics "
            "to improve your overall score."
        )

    elif average >= 40:
        st.warning(
            "📚 Your performance is average. Increase study time "
            "and practice regularly."
        )

    else:
        st.error(
            "💪 More improvement is needed. Focus on basic concepts, "
            "practice daily, and ask teachers for help when needed."
        )

    # Attendance suggestion
    if attendance < 75:
        st.warning(
            "⚠️ Attendance is below 75%. Try to attend classes more regularly."
        )
    elif attendance >= 90:
        st.success(
            "✅ Excellent attendance!"
        )

    # Study-hour suggestion
    if study_hours < 2:
        st.info(
            "📖 Consider increasing your study time gradually "
            "and maintaining a consistent routine."
        )

    # --------------------------------------------------
    # STRONGEST & WEAKEST SUBJECT
    # --------------------------------------------------
    marks_dict = {
        "Mathematics": math,
        "Science": science,
        "English": english
    }

    strongest = max(marks_dict, key=marks_dict.get)
    weakest = min(marks_dict, key=marks_dict.get)

    col1, col2 = st.columns(2)

    with col1:
        st.success(
            f"🏆 Strongest Subject: **{strongest}** ({marks_dict[strongest]}/100)"
        )

    with col2:
        st.warning(
            f"📌 Subject to Improve: **{weakest}** ({marks_dict[weakest]}/100)"
        )

    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------
    st.divider()

    st.caption(
        "Student Performance Analysis Project | "
        "Python + Pandas + Streamlit + Matplotlib"
    )
