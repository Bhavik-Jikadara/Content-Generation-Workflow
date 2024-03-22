"""
Initiate the process with your enhanced crew ready. Observe as your agents collaborate, leveraging their new capabilities for a successful project outcome. You can also pass the inputs that will be interpolated into the agents and tasks.
"""
from src.components.process import researcher_crew, writer_crew, SEO_analyst_crew, visual_content_creator_crew, content_curator_crew, content_personalization_specialist_crew, all_crew
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

selected_box = st.selectbox(
    "Choose agent",
    ('Researcher', 'Writer', 'SEO Analyst', 'Visual Content Creator', 'Content Curator', 'Content Personalization Specialist', 'All tasks together')
)

def generate_content(topic, crew):
    result = crew.kickoff({"topic":topic})
    st.image(generate_image(topic).resize((800, 400)), caption=topic)
    return result

if st.button("Generate Article"):
    if selected_box == "Researcher":
        st.write(generate_content(topic=topic, crew=researcher_crew))

    if selected_box == "Writer":
        st.write(generate_content(topic=topic, crew=writer_crew))

    if selected_box == "Content Curator":
        st.write(generate_content(topic=topic, crew=content_curator_crew))

    if selected_box == "Visual Content Creator":
        st.write(generate_content(topic=topic, crew=visual_content_creator_crew))

    if selected_box == "Content Personalization Specialist":
        st.write(generate_content(topic=topic, crew=content_personalization_specialist_crew))

    if selected_box == "SEO Analyst":
        st.write(generate_content(topic=topic, crew=SEO_analyst_crew))

    if selected_box == "All tasks together":
        st.write(generate_content(topic=topic, crew=all_crew))