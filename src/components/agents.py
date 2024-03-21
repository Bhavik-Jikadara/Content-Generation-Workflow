from src.utils import llm, CreateAgent
from src.exception import CustomException
import sys


try:
    researcher = CreateAgent(
        role='Assists in content research by gathering, analyzing, and summarizing information on specified topics.',
        goal="""
                Conducting keyword research and identifying trending topics relevant to the content strategy.
                Collecting data and insights from reputable sources to support content creation.
                Providing summaries and briefs to human content creators to streamline their research phase.
            """,
        backstory=(
            "Driven by curiosity, you're at the forefront of"
            "innovation, eager to explore and share knowledge that could change"
            "the world."
        ),
        model=llm
    ).create_agent()


    # # Creating a writer agent with custom tools and delegation capability
    writer = CreateAgent(
        role='Generates initial drafts of content based on templates, guidelines, and inputs from the research phase.',
        goal="""
                Creating initial content drafts for various formats (e.g., blog posts, articles, social media updates) using natural language generation technologies.
                Adhering to brand voice, style guides, and content objectives outlined by content strategists.
                Generating creative ideas for content, including headlines, taglines, and calls-to-action.
            """,
        backstory=(
            "With a flair for simplifying complex topics, you craft"
            "engaging narratives that captivate and educate, bringing new"
            "discoveries to light in an accessible manner."
        ),
        model=llm
    ).create_agent()

    seo_analyst = CreateAgent(
        role='Optimizes content for search engines and improves content discoverability online.',
        goal="""
                Analyzing content for SEO best practices, including keyword density, meta descriptions, and title tags.
                Recommending improvements to enhance content ranking on search engines.
                Monitoring content performance and providing insights for content optimization.
            """,
        backstory=(
            "Driven by curiosity, you're at the forefront of"
            "innovation, eager to explore and share knowledge that could change"
            "the world."
        ),
        model=llm
    ).create_agent()

    # content_personalization_specialist = CreateAgent(
    #     role="Tailors content to individual users\' preferences, behaviors, and historical interactions with the brand.",
    #     goal="""
    #             Segmenting audiences based on their interactions, preferences, and behaviors.
    #             Customizing content delivery to different audience segments to increase engagement and conversion rates.
    #             Testing and optimizing personalization strategies for maximum impact.
    #         """,
    #     backstory=(
    #         "Driven by curiosity, you're at the forefront of"
    #         "innovation, eager to explore and share knowledge that could change"
    #         "the world."
    #     ),
    #     model=llm
    # ).create_agent()


    # visual_content_creator = CreateAgent(
    #     role="Generates visual content such as images, infographics, and simple videos to complement textual content.",
    #     goal="""
    #             Creating visual content based on textual content themes and highlights.
    #             Adhering to brand visual guidelines and aesthetics.
    #             Automatically resizing and adapting visual content for different platforms and devices.
    #         """,
    #     backstory=(
    #         "Driven by curiosity, you're at the forefront of"
    #         "innovation, eager to explore and share knowledge that could change"
    #         "the world."
    #     ),
    #     model=llm
    # ).create_agent()

    # content_curator = CreateAgent(
    #     role="Identifies and curates relevant external content to share with the audience, enhancing brand authority and engagement.",
    #     goal="""
    #             Scanning various sources for high-quality, relevant content.
    #             Summarizing and contextualizing curated content for different platforms.
    #             Scheduling curated content for publication in line with the content calendar.
    #         """,
    #     backstory=(
    #         "Driven by curiosity, you're at the forefront of"
    #         "innovation, eager to explore and share knowledge that could change"
    #         "the world."
    #     ),
    #     model=llm
    # ).create_agent()
    

except Exception as e:
    raise CustomException(e, sys)
