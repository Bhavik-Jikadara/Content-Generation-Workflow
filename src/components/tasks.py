from src.exception import CustomException
from src.utils import search_tool, CreateTask
from src.components.agents import researcher, writer, seo_analyst, visual_content_creator, content_curator, content_personalization_specialist
import sys

try:
    research_assistant_task = CreateTask(
        """
        Analyse the given task {topic}. Prepare comprehensive pin-points for accomplishing the given task.
        Make sure the ideas are to the point, coherent, and compelling.
        Make sure you abide by the rules. Don't use any tools.
        RULES:
        - Write ideas in bullet points.
        - Avoid adult ideas.
        """,
        'A 4 paragraph article on {topic} advancements formatted as markdown. Assists in content research by gathering, analyzing, and summarizing information on specified topics.',
        search_tool,
        researcher
    ).create_task()

    content_creator_task = CreateTask(
        """
        Write a compelling story in 1200 words based on the blueprint ideas given by the Idea analyst.
        Make sure the contents are coherent, easily communicable, and captivating.
        Don't use any tools.
        Make sure you abide by the rules.
        RULES:
        - Writing must be grammatically correct.
        - Use as little jargon as possible
        """,
        "Generates initial drafts of content based on templates, guidelines, and inputs from the research phase. A 5 paragraph article on {topic} advancements formatted as markdown.",
        search_tool,
        writer
    ).create_task()

    seo_analyst_task = CreateTask(
        """
        Analyzing content for SEO best practices, including keyword density, meta descriptions, and title tags.
        Recommending improvements to enhance content ranking on search engines.
        """,
        "A 4 paragraph article on {topic} advancements formatted as markdown. Optimizes content for search engines and improves content discoverability online.",
        search_tool,
        seo_analyst
    ).create_task()


    content_personalization_specialist_task = CreateTask(
        """
        Segmenting audiences based on their interactions, preferences, and behaviors of {topic}.
        Customizing content delivery to different audience segments to increase engagement and conversion rates.
        """,
        'A 4 paragraph article on {topic} advancements formatted as markdown.',
        search_tool,
        content_personalization_specialist,
    ).create_task()

    content_curator_task = CreateTask(
        """
        Scanning various sources for high-quality, relevant content. {topic} Summarizing and contextualizing curated content for different platforms.
        Scheduling curated content for publication in line with the content calendar.
        """,
        'A 3 paragraph article on {topic} advancements formatted as markdown.',
        search_tool,
        content_curator
    ).create_task()

    visual_content_creator_task = CreateTask(
        """
        {topic} Creating visual content based on textual content themes and highlights.
        Adhering to brand visual guidelines and aesthetics.
        Automatically resizing and adapting visual content for different platforms and devices.
        """,
        "A 3 paragraph article on {topic} advancements formatted as markdown.",
        search_tool,
        visual_content_creator
    ).create_task()



except Exception as err:
    raise CustomException(err, sys)
