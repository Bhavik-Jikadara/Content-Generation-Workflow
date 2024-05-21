import streamlit as st
from src.components.process import all_crew


class ContentGenerationUI:

    def generate_content(self, topic):
        inputs = {
            "topic": topic
        }
        result = all_crew.kickoff(inputs=inputs)
        return result

    def content_generation(self):
        if st.session_state.generating:
            st.session_state.content_generator = self.generate_content(st.session_state.topic)

        if st.session_state.content_generator and st.session_state.content_generator != "":
            with st.container():
                st.write("Content generated successfully!")
                st.download_button(
                    label="Download Markdown file",
                    data=st.session_state.content_generator,
                    file_name = "content_generate.md",
                    mime="text/markdown"
                )   
            st.session_state.generating = False

    def sidebar(self):
        with st.sidebar:
            st.title("Content Generator Tool")
            st.write("This workflow should autonomously process input topics, conduct research, plan content, generate images, optimize for SEO, and perform final editorial checks.")

            topic = st.text_area(
                label="Enter the topic: ",
                placeholder="Enter the name of the topic to generate the article",
                key="topic",
                height=175
            )
            st.write(f'You wrote {len(topic.split())} words.')

            if st.button("Generate Content"):
                st.session_state.generating=True


    def render(self):
        st.set_page_config(page_title="Content Generation", page_icon="📃")

        # Initialize the app session state
        if "topic" not in st.session_state:
            st.session_state.topic = ""

        if "content_generator" not in st.session_state:
            st.session_state.content_generator = ""
        
        if "generating" not in st.session_state:
            st.session_state.generating = False

        # This is sidebar section
        self.sidebar()

        self.content_generation()



if __name__ == "__main__":
    ContentGenerationUI().render()

    
