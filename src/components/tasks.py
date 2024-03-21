from src.exception import CustomException
from src.utils import search_tool, CreateTask
from src.components.agents import researcher, writer, seo_analyst
import sys

try:
    research_assistant_task = CreateTask(
        """
        Conducting keyword research and identifying trending topics relevant to the content strategy.
        Collecting data and insights from reputable sources to support content creation.
        Providing summaries and briefs to human content creators to streamline their research phase.
        """,
        'Assists in content research by gathering, analyzing, and summarizing information on specified topics.',
        search_tool,
        researcher
    ).create_task()

    content_creator_task = CreateTask(
        """
        Creating initial content drafts for various formats (e.g., blog posts, articles, social media updates) using natural language generation technologies.
        Adhering to brand voice, style guides, and content objectives outlined by content strategists.
        Generating creative ideas for content, including headlines, taglines, and calls-to-action.
        """,
        "Generates initial drafts of content based on templates, guidelines, and inputs from the research phase.",
        search_tool,
        writer
    ).create_task()

    seo_analyst_task = CreateTask(
        """
        Analyzing content for SEO best practices, including keyword density, meta descriptions, and title tags.
        Recommending improvements to enhance content ranking on search engines.
        Monitoring content performance and providing insights for content optimization.
        """,
        "Optimizes content for search engines and improves content discoverability online.",
        search_tool,
        seo_analyst
    ).create_task()


    # content_personalization_specialist_task = CreateTask(
    #     """
    #     Segmenting audiences based on their interactions, preferences, and behaviors.
    #     Customizing content delivery to different audience segments to increase engagement and conversion rates.
    #     Testing and optimizing personalization strategies for maximum impact.
    #     """,
    #     "Tailors content to individual users' preferences, behaviors, and historical interactions with the brand.",
    #     search_tool,
    #     content_personalization_specialist
    # ).create_task()

    # content_curator_task = CreateTask(
    #     """
    #     Scanning various sources for high-quality, relevant content.
    #     Summarizing and contextualizing curated content for different platforms.
    #     Scheduling curated content for publication in line with the content calendar.
    #     """,
    #     "Identifies and curates relevant external content to share with the audience, enhancing brand authority and engagement.",
    #     search_tool,
    #     content_curator
    # ).create_task()

    # visual_content_creator_task = CreateTask(
    #     """
    #     Creating visual content based on textual content themes and highlights.
    #     Adhering to brand visual guidelines and aesthetics.
    #     Automatically resizing and adapting visual content for different platforms and devices.
    #     """,
    #     "Generates visual content such as images, infographics, and simple videos to complement textual content.",
    #     search_tool,
    #     visual_content_creator
    # ).create_task()



except Exception as err:
    raise CustomException(err, sys)
