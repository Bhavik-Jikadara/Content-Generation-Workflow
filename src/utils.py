from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool
from crewai import Task, Agent
import os
from dotenv import load_dotenv
load_dotenv()
# API SETUP
google_api_key = os.getenv("GOOGLE_API_KEY")

# model for generate content
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

# search tool
search_tool = SerperDevTool()


class CreateTask:
    def __init__(self, description, expected_output, tool, agent) -> None:
        self.description = description
        self.expected_output = expected_output
        self.tool = tool
        self.agent = agent

    def create_task(self, output_file='outputs/new-blog-post.md'):
        task = Task(
            description=self.description,
            expected_output=self.expected_output,
            tools=[self.tool],
            agent=self.agent,
            output_file=output_file
        )
        return task


class CreateAgent:
    def __init__(self, role: str, goal: str, backstory, model) -> None:
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.model = model

    def create_agent(self, allow_delegation=True):
        agent = Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=True,
            memory=True,
            tools=[search_tool],
            allow_delegation=allow_delegation,
            llm=self.model
        )

        return agent
