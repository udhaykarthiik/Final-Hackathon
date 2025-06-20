from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

from backend.langchain_agents.user_research_extractor import run_user_research_agent
from backend.langchain_agents.need_pain_mapper import run_need_pain_mapper
from backend.langchain_agents.pitch_structure_composer import run_pitch_structure_composer
from backend.langchain_agents.pitch_script_generator import run_pitch_script_generator
from backend.langchain_agents.feedback_refiner import run_feedback_refiner


# Define each step as a LangChain Runnable
def step_user_research(state):
    feedback = state["feedback"]
    result = run_user_research_agent(feedback)
    return {**state, "user_model": result}

def step_need_pain(state):
    user_model = state["user_model"]
    result = run_need_pain_mapper(user_model)
    return {**state, "mapped_goals": result}

def step_structure(state):
    project = state["project_description"]
    goals = state["mapped_goals"]
    result = run_pitch_structure_composer(goals, project)
    return {**state, "pitch_structure": result}

def step_script(state):
    structure = state["pitch_structure"]
    persona = state["persona"]
    result = run_pitch_script_generator(structure, persona)
    return {**state, "pitch_script": result}

def step_refiner(state):
    script = state["pitch_script"]
    feedback = state["refinement_feedback"]
    result = run_feedback_refiner(feedback, str(script))
    return {**state, "refined_pitch": result}


# Register nodes in LangGraph
workflow = StateGraph()

workflow.add_node("extract_user_research", RunnableLambda(step_user_research))
workflow.add_node("map_need_pain", RunnableLambda(step_need_pain))
workflow.add_node("compose_structure", RunnableLambda(step_structure))
workflow.add_node("generate_script", RunnableLambda(step_script))
workflow.add_node("refine_script", RunnableLambda(step_refiner))

# Define the flow
workflow.set_entry_point("extract_user_research")
workflow.add_edge("extract_user_research", "map_need_pain")
workflow.add_edge("map_need_pain", "compose_structure")
workflow.add_edge("compose_structure", "generate_script")
workflow.add_edge("generate_script", "refine_script")
workflow.set_finish_point("refine_script")

# Build the app
flow_app = workflow.compile()
