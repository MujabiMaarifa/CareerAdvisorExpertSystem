import streamlit as st
from main import CareerAdvisor

st.set_page_config(page_title="Career Advisor Expert System", layout="centered")
st.title("🎯 Career Advisor Expert System")
st.info("Your career determines your future ...")

#initialize the advisor 
advisor = CareerAdvisor()

#sidebar contents -> displays the FOL reasoning
st.sidebar.header("⚙ Reasoning Method")
reasoning_method = st.sidebar.radio(
        "Choose reasoning method:",
        ["Forward Chaining", "Backward Chaining", "Hybrid(both)"]
        )

st.header("👤 Enter your profile")

#user input -> from given options
skills = st.multiselect(
        "Select your skills:",
        ["programming", "problem_solving", "statistics", "communication", "medical_knowldege", "teaching_explaining", "drawing"]
        )

traits = st.multiselect(
        "Select your personality traits:",
        ["logical", "analytical", "curious", "caring", "creative", "detailed_oriented"]
        )

interests = st.multiselect(
        "Select your interests:",
        ["technology", "data_analysis", "research", "design", "networks", "security", "teaching", "house_planning", "patient_care"]
        )

education = st.selectbox(
        "Select your education level:",
        ["diploma", "bachelors", "masters", "phd"]
        )

#set user profile based on the selected user's input
advisor.clear_user_facts()
advisor.set_user_profile(
    skills=skills,
    traits=traits,
    interests=interests,
    education=education
)

#implement the expert system to reason and recommend career to user
if st.button("🔍 Get Career Recommendation"):
    if reasoning_method == "Forward Chaining":
        recommended = advisor.forward_chaining()
        method_used = "Forward Chaining"

    elif reasoning_method == "Backward Chaining":
        #backward chaining-> goal driven -> get goal from the user and reason with it
        st.subheader("Select career to check:")
        career_goal = st.selectbox("Career Goal:", ["software_engineer", "data_scientist", "teacher", "architect", "nurse", "lawyer"])
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
        st.success("Recommended Careers:")
        for c in recommended:
            st.write(f"- {c.replace('_', ' ').title()}")
    else:
        st.warning("No career fully matches your profile. We are updating the system soon. Thank you for your patience.")

