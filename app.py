import streamlit as st
from main import CareerAdvisor

st.set_page_config(page_title="Career Advisor Expert System", layout="wide")
st.title("🎯 Career Advisor Expert System")
st.info("Your career determines your future ...")

# Initialize the advisor
advisor = CareerAdvisor()

# Sidebar
st.sidebar.title("AI Logic")
st.sidebar.info("Reason with the expert to find your career.")
st.sidebar.header("⚙ Reasoning Method")

reasoning_method = st.sidebar.radio(
    "Choose reasoning method:",
    [
        "Forward Chaining (Data Driven)",
        "Backward Chaining (Goal Driven)",
        "Hybrid (Both)"
    ]
)

st.header("👤 Enter your profile")

# User inputs
skills = st.multiselect(
    "Select your skills:",
    [
        "programming", "problem_solving", "statistics",
        "communication", "medical_knowledge",
        "teaching_explaining", "drawing"
    ]
)

traits = st.multiselect(
    "Select your personality traits:",
    [
        "logical", "analytical", "curious",
        "caring", "creative", "detail_oriented",
        "teaching"
    ]
)

interests = st.multiselect(
    "Select your interests:",
    [
        "technology", "data_analysis", "research",
        "design", "networks", "security",
        "teaching", "house_planning", "patient_care"
    ]
)

education = st.selectbox(
    "Select your education level:",
    ["diploma", "bachelors", "masters", "phd"]
)

# Set user profile
advisor.set_user_profile(
    skills=skills,
    traits=traits,
    interests=interests,
    education=education
)

# Reasoning and recommendation
if st.button("🔍 Get Career Recommendation", use_container_width=True):
    try:
        if reasoning_method == "Forward Chaining (Data Driven)":
            recommended = advisor.forward_chaining()
            method_used = "Forward Chaining"

        elif reasoning_method == "Backward Chaining (Goal Driven)":
            st.subheader("🎯 Select a career to verify")
            career_goal = st.selectbox(
                "Career Goal:",
                [
                    "software_engineer",
                    "data_scientist",
                    "teacher",
                    "architect",
                    "nurse",
                    "lawyer"
                ]
            )

            if advisor.backward_chaining(career_goal):
                recommended = [career_goal]
            else:
                recommended = []

            method_used = "Backward Chaining"

        else:  # Hybrid
            recommended = advisor.hybrid_recommendation()
            method_used = "Hybrid Reasoning"

        st.write(f"**Reasoning Method Used:** {method_used}")

        if recommended:
            st.success("✅ Recommended Careers:")
            for career in recommended:
                st.write(f"- {career.replace('_', ' ').title()}")
        else:
            st.warning(
                "⚠ No career fully matches your profile yet. "
                "Try adjusting your skills, traits, or interests."
            )

    except Exception as e:
        st.error(f"❌ Reasoning error: {e}")
        st.stop()
