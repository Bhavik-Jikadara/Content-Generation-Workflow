### Project Description
Implementing a scalable content team using AI involves creating a framework that blends the strengths of AI technologies with the creative and supervisory capabilities of human team members. This strategy aims to enhance efficiency, creativity, and content output quality.

This code is a high-level conceptualization and would require adaptation to fit the actual CrewAI framework and toolset specifics. It illustrates how different AI agents, equipped with specialized roles and tools, can collaborate within a content creation process. Each agent focuses on a key area—research, writing, and SEO—streamlining the content development workflow and enhancing output quality through specialized AI-driven tasks.

### Objective
Implement a content generation workflow using the Crew AI framework. This workflow should autonomously process input topics, research, plan content, generate images, optimize for SEO, and perform final editorial checks.

### Tools and Frameworks:
* Crew AI framework
* Streamlit - User Interface(UI)
* Python for scripting
* AI models or APIs (e.g., `gemini-pro` for content, `stable-diffusion-xl-base` for images)

### Prerequisites
To complete this project, you should understand Python programming, data manipulation, visualization libraries such as Pandas and Matplotlib, and machine learning libraries such as Scikit-Learn. Additionally, some background knowledge of natural language processing (NLP) techniques and generating text-to-image and image-to-text methods would be helpful.

### Resources
- Live demo link: [Article Generate using CrewAI]()
- Check out  [CrewAI](https://docs.crewai.com/)
- Project code [GitHub](https://github.com/Bhavik-Jikadara/Content-Generation-Workflow.git)

-----------------------------------------------------------------------------------------------------------------
## Notes: This step is crucial:
### [Click here](https://www.c-sharpcorner.com/article/how-to-addedit-path-environment-variable-in-windows-11/) to set four API_KEYs in the Environment Variable, and use this link as a reference. 
* [Click here to OpenAI API Key](https://platform.openai.com/api-keys)
    $ OPENAI_API_KEY="Your-API-key"
  
* [Click here to Google API Key](https://aistudio.google.com/)  
    $ GOOGLE_API_KEY="Your-API-key"
  
* [Click here to Serper API Key](https://serper.dev/api-key)  
    $ SERPER_API_KEY="Your-API-key"
  
* [Click here to HUGGINGFACE_API_KEY](https://huggingface.co/settings/tokens)  
    $ HUGGINGFACE_API_KEY="Your-API-key"
-----------------------------------------------------------------------------------------------------------------         

### Step 1: Clone the repository
    $ git clone https://github.com/Bhavik-Jikadara/Content-Generation-Workflow.git
    $ cd Content-Generation-Workflow/

### Step 2: Create a virtualenv (windows user)
    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/Scripts/activate

### Step 3: Rename the .env.example filename to the .env file and add API keys
    $ OPENAI_API_KEY=""
    $ GOOGLE_API_KEY=""
    $ SERPER_API_KEY=""
    $ HUGGINGFACE_API_KEY=""

### Step 4: Install the requirements libraries using pip
    $ pip install -r requirements.txt

### Step 5: Type this command and run the project:
    $ streamlit run Home.py
