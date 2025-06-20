from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_community.llms import Together
import os
from dotenv import load_dotenv
load_dotenv()

together_llm = Together(
    model="togethercomputer/llama-3-8b-chat",
    api_key=os.getenv("TOGETHER_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["feedback"],
    template="""
    Given this user feedback:
    "{feedback}"

    Extract the user's main task, influences, and needs in this format:
    {{
        "need": "...",
        "influences": ["..."],
        "task": "..."
    }}
    """
)

chain = prompt | together_llm

def run_user_research_agent(feedback: str):
    return chain.invoke({"feedback": feedback})
