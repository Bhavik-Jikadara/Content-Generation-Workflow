"""
Combine your agents into a crew, setting the workflow process they'll follow to accomplish the tasks, now with the option to configure language models for enhanced interaction.
"""

from crewai import Crew, Process
from src.components.agents import researcher_agent, content_creator_agent, seo_analyst_agent, visual_content_creator_agent, editorial_assistant_agent, content_curator_agent
from src.components.tasks import researcher_task, content_creator_task, seo_analyst_task, visual_content_creator_task, editorial_assistant_task, content_curator_task


# all crew
all_crew = Crew(
    agents=[researcher_agent, content_creator_agent, content_curator_agent, seo_analyst_agent,
            visual_content_creator_agent, editorial_assistant_agent],
    tasks=[researcher_task, content_creator_task, content_curator_task, seo_analyst_task,
            visual_content_creator_task, editorial_assistant_task],
    process=Process.sequential
)
