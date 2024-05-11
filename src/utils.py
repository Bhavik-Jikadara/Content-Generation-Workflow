from langchain_google_genai import GoogleGenerativeAI
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv
load_dotenv()

# search tool
search_tool = SerperDevTool(n_results=5)
# model for generate content
llm = GoogleGenerativeAI(
    model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
