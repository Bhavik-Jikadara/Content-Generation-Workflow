"""
Combine your agents into a crew, setting the workflow process they'll follow to accomplish the tasks, now with the option to configure language models for enhanced interaction.
"""

from crewai import Crew, Process
from src.components.agents import researcher, writer, seo_analyst, visual_content_creator, content_curator, content_personalization_specialist

from src.components.tasks import research_assistant_task, content_creator_task, seo_analyst_task, visual_content_creator_task, content_curator_task, content_personalization_specialist_task

researcher_crew = Crew(
    agents=[researcher],
    tasks=[research_assistant_task],
    process=Process.sequential
)

writer_crew = Crew(
    agents=[writer],
    tasks=[content_creator_task],
    process=Process.sequential
)

SEO_analyst_crew = Crew(
    agents=[seo_analyst],
    tasks=[seo_analyst_task],
    process=Process.sequential
)
visual_content_creator_crew = Crew(
    agents=[visual_content_creator],
    tasks=[visual_content_creator_task],
    process=Process.sequential
)

content_personalization_specialist_crew = Crew(
    agents=[content_personalization_specialist],
    tasks=[content_personalization_specialist_task],
    process=Process.sequential
)

content_curator_crew = Crew(
    agents=[content_curator],
    tasks=[content_curator_task],
    process=Process.sequential
)

# all crew
all_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_assistant_task, content_creator_task, seo_analyst_task],
    process=Process.sequential
)
