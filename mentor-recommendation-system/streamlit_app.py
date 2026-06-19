import streamlit as st
import pandas as pd

from app.recommendation import recommend_mentors


st.set_page_config(
    page_title="Mentor Recommendation System",
    layout="wide"
)

st.title(":rainbow[🎓 AI Mentor Recommendation System]")

students = pd.read_csv("data/students.csv")

st.markdown("### :red[👨‍🎓 Choose Student]")
student_id = st.selectbox(
    "",
    students["student_id"]
)

student = students[
    students["student_id"] == student_id
].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.markdown("### :green[📋 Student Details]")
    st.write(f"**Name:** {student['student_name']}")
    st.write(f"**Skills:** {student['skills']}")
    st.write(f"**Interests:** {student['interests']}")

with col2:
    st.markdown("### :orange[📍 Location]")
    st.write(f"Latitude: {student['latitude']}")
    st.write(f"Longitude: {student['longitude']}")

if st.button("🔍 Find Mentors"):

    result = recommend_mentors(student_id)

    st.markdown("## :violet[🏆 Top Recommended Mentors]")

    st.dataframe(
        result,
        use_container_width=True
    )

    st.balloons()