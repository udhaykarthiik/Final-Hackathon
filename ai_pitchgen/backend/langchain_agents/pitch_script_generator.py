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
    input_variables=["pitch_structure", "persona"],
    template="""
Given this pitch structure:
{pitch_structure}

Write a 300-word pitch script targeted to a {persona}.
Sections: opening hook, customer pain, value prop, product solution, CTA.
Ensure the tone matches the persona.
"""
)

chain = prompt | llm

def run_pitch_script_generator(pitch_structure: dict, persona: str):
    return chain.invoke({
        "pitch_structure": str(pitch_structure),
        "persona": persona
    })
