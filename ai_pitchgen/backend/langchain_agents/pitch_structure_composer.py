from langchain.prompts import PromptTemplate
from langchain_community.llms import Together
import os
from dotenv import load_dotenv
load_dotenv()

llm = Together(
    model="togethercomputer/llama-3-8b-chat",
    api_key=os.getenv("TOGETHER_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["mapped_goals", "project_description"],
    template="""
Use the following project description:
{project_description}

And these mapped user insights:
{mapped_goals}

Create a sales pitch structure in 5 sections:
1. Identify Need
2. Evaluate Alternatives
3. Present Fit
4. Offer Benefits
5. Align with Market

Include supporting user insights in bullet points.
"""
)

chain = prompt | llm

def run_pitch_structure_composer(mapped_goals: dict, project_description: str):
    return chain.invoke({
        "mapped_goals": str(mapped_goals),
        "project_description": project_description
    })
