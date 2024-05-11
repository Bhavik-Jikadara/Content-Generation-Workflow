from src.exception import CustomException
from crewai import Task
from src.components.agents import researcher_agent, content_creator_agent, visual_content_creator_agent, seo_analyst_agent, editorial_assistant_agent, content_curator_agent
import sys
from src.utils import llm

try:
    researcher_task = Task(
        description="""
        These responsibilities highlight the role of the AI Research Assistant in supporting the content creation process by leveraging AI and machine learning techniques to streamline research, gather relevant data and insights, and facilitate collaboration between AI and human content creators based on the user input {topic}.
        """,
        agent=researcher_agent,
        expected_output="""
        Structuring a content plan that includes headings, subheadings, and key points to cover for the {topic}.

        Exaple output:
        ### Title: The Role of AI in Healthcare

        ### Introduction:
        - Brief overview of ....

        ### 1: AI Applications in Diagnosis and Disease Detection
        * 1.1: Medical Imaging and Radiology
            * Key points:
                - Use of AI algorithms to analyze medical images (X-rays, MRIs, CT scans) for early detection of diseases.
                - Improved accuracy and efficiency in identifying abnormalities and diagnosing conditions such as cancer, fractures, and cardiovascular diseases.
        * 1.2: .......

        ### Conclusion:
        - Summary of the key roles and applications of AI in healthcare, from diagnosis and treatment to personalized medicine and remote monitoring.
        - Discussion of the potential benefits and challenges of AI adoption in healthcare, along with considerations for future developments.
        - Call-to-action encouraging readers to stay informed about advancements in AI healthcare and to engage in discussions about the ethical and regulatory implications.
        - Closing remarks emphasizing the transformative potential of AI in improving patient care and shaping the future of healthcare delivery.

        """,
        llm=llm,
        output_file="outputs/content_creator.md"
    )

    content_creator_task = Task(
        description="""
        The role of generating initial drafts of content requires a blend of creativity, research skills, attention to detail, and adherence to guidelines. By effectively translating research insights into compelling content drafts, content creators lay the groundwork for successful content marketing campaigns that resonate with the target audience and achieve business objectives.
        """,
        agent=content_creator_agent,
        expected_output="""
        - Based on the content plan, generate a draft using an AI text-generation model. This should form the body of your content.
        - Generating creative ideas for content, including headlines, taglines, and calls-to-action.
        """,
        llm=llm
    )

    content_curator_task = Task(
        description="""
        The Content Curator plays a pivotal role in guaranteeing that published content is error-free, stylistically appropriate, and prepared to meet the publication's standards and expectations.
        """,
        agent=content_curator_agent,
        expected_output="""
        - Apply SEO best practices to the generated content. This may involve:
            - Keyword optimization.
            - Meta tags and descriptions.
            - Readability improvements.

        The expected output of a Content Curator is optimizing content for SEO best practices, including keyword density, meta descriptions, and title tags. Recommending improvements to enhance content ranking on search engines. Monitoring content performance and providing insights for content optimization.
        """,
        llm=llm,
        context=[researcher_task]
    )

    visual_content_creator_task = Task(
        description="""
        Incorporate an AI-based image generation model to create relevant images for the content. Ensure these images are saved locally.
        """,
        agent=visual_content_creator_agent,
        expected_output="""Generate a .png or .jpg file image based on the input and return it in images folder.""",
        context=["{topic}"]
    )

    seo_analyst_task = Task(
        description="""
        The role involves optimizing content for search engines by analyzing, recommending improvements, and monitoring performance, ultimately aiming to enhance content discoverability online and improve its ranking on search engine results pages.
        """,
        agent=seo_analyst_agent,
        expected_output="""
        Apply SEO best practices to the generated content. This may involve:
        - Keyword optimization.
        - Meta tags and descriptions.
        - Readability improvements.

        The expected output of an SEO Analyst is analyzing content for SEO best practices, including keyword density, meta descriptions, and title tags. Recommending improvements to enhance content ranking on search engines. Monitoring content performance and providing insights for content optimization.
        """,
        context=[content_creator_task]
    )

    editorial_assistant_task = Task(
        description="""
        The Editorial Assistant plays a pivotal role in guaranteeing that published content is error-free, stylistically appropriate, and prepared to meet the publication's standards and expectations.
        """,
        agent=editorial_assistant_agent,
        expected_output="""
        The expected output is high-quality content that is polished, accurate, and in line with the publication's editorial standards, ensuring a positive reader experience and maintaining the publication's reputation for excellence.
        """,
        context=[seo_analyst_task],
        output_file="outputs/content_creator.md"
    )


except Exception as err:
    raise CustomException(err, sys)
