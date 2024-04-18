"""
Initiate the process with your enhanced crew ready. Observe as your agents collaborate, leveraging their new capabilities for a successful project outcome. You can also pass the inputs that will be interpolated into the agents and tasks.
"""
from src.components.process import all_crew
import streamlit as st
from src.components.image_generate import generate_image

st.set_page_config(
    page_title="Article Generate",
    page_icon="📝"
)

st.header("Content Generation Workflow using CrewAI")
st.markdown("This workflow should autonomously process input topics, conduct research, plan content, generate images, optimize for SEO, and perform final editorial checks.")

topic = st.text_area(
    label="Enter the topic: ",
    placeholder="Enter the name of the topic to generate the article",
    height=200
)
st.write(f'You wrote {len(topic.split())} words.')


def generate_content(topic, crew):
    result = crew.kickoff({"topic": topic})
    st.image(generate_image(topic).resize((800, 400)), caption=topic)
    return result


if st.button("Generate Article"):
    st.write(generate_content(topic=topic, crew=all_crew))
