"""
Initiate the process with your enhanced crew ready. Observe as your agents collaborate, leveraging their new capabilities for a successful project outcome. You can also pass the inputs that will be interpolated into the agents and tasks.
"""
from src.components.process import all_crew
import streamlit as st
from src.components.image_geneerate import generate_image

st.header("Article Generate using CrewAI")

topic = st.text_area(
    label="Enter the topic: ",
    placeholder="Enter the name of the topic to generate the article"
)
st.write(f'You wrote {len(topic.split())} words.')

def generate_content(topic):
    result = all_crew.kickoff({"topic":topic})
    st.image(generate_image(topic).resize((800, 400)), caption=topic)
    return result

if st.button("Generate Article"):
    st.write(generate_content(topic=topic))