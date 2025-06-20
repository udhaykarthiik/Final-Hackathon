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
    input_variables=["user_model"],
    template="""
Given the following structured user model:
{user_model}

Return structured goals, pain points, decision points, and success criteria in JSON. Cluster the insights into functional, emotional, and social themes.
"""
)

chain = prompt | llm

def run_need_pain_mapper(user_model: dict):
    return chain.invoke({"user_model": str(user_model)})
