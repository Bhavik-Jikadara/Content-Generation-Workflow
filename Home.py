import streamlit as st
from src.components.process import all_crew
from dotenv import load_dotenv
load_dotenv()


class ContentGenerationUI:

    def generate_content(self, topic):
        inputs = {
            "topic": topic
        }
        result = all_crew.kickoff(inputs=inputs)
        return result

    def content_generation(self):
        if st.session_state.generating:
            st.session_state.content_generator = self.generate_content(
                st.session_state.topic)

        if st.session_state.content_generator and st.session_state.content_generator != "":
            with st.container():
                st.write("Content generated successfully!")
                st.download_button(
                    label="Download Markdown file",
                    data=st.session_state.content_generator,
                    file_name="content_generate.md",
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
                st.session_state.generating = True

    def render(self):
        st.set_page_config(page_title="Content Generation", page_icon="📃")
        tab1, tab2 = st.tabs(["Output", "About Project"])

        # This is sidebar section
        self.sidebar()

        with tab2:
            st.markdown("# About project")
            st.write(
                """
                ### Project Description
                Implementing a scalable content team using AI involves creating a framework that blends the strengths of AI technologies with the creative and supervisory capabilities of human team members. This strategy aims to enhance efficiency, creativity, and content output quality.

                This code is a high-level conceptualization and would require adaptation to fit the actual CrewAI framework and toolset specifics. It illustrates how different AI agents, equipped with specialized roles and tools, can collaborate within a content creation process. Each agent focuses on a key area—research, writing, and SEO—streamlining the content development workflow and enhancing output quality through specialized AI-driven tasks.
                
                ### Objective
                Implement a content generation workflow using the Crew AI framework. This workflow should autonomously process input topics, conduct research, plan content, generate images, optimize for SEO, and perform final editorial checks.
                
                ### Tools and Frameworks:
                * Crew AI framework
                * Streamlit - User Interface(UI)
                * Python for scripting
                * AI models or APIs (e.g., `gemini-pro` for content, `stable-diffusion-xl-base` for images)

                ### Prerequisites
                To complete this project, you should understand Python programming, data manipulation, visualization libraries such as Pandas and Matplotlib, and machine learning libraries such as Scikit-Learn. Additionally, some background knowledge of natural language processing (NLP) techniques and generate text to image and image to text methods would be helpful.

                ### Resources
                - Live demo link: [Content Generate - WebApp]()
                - Check out  [CrewAI](https://docs.crewai.com/)
                - Project code [GitHub](https://github.com/Bhavik-Jikadara/Content-Generation-Workflow)
                """
            )

        with tab1:
            # Initialize the app session state
            if "topic" not in st.session_state:
                st.session_state.topic = ""

            if "content_generator" not in st.session_state:
                st.session_state.content_generator = ""

            if "generating" not in st.session_state:
                st.session_state.generating = False

            self.content_generation()


if __name__ == "__main__":
    ContentGenerationUI().render()
