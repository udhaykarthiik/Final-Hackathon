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
    input_variables=["feedback", "previous_script"],
    template="""
Given this pitch script:
{previous_script}

And the following feedback:
{feedback}

Summarize the feedback, refine the script, and list focus improvements.
Output in structured JSON.
"""
)

chain = prompt | llm

def run_feedback_refiner(feedback: str, previous_script: str):
    return chain.invoke({
        "feedback": feedback,
        "previous_script": previous_script
    })
