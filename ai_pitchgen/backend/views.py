from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .langgraph_flow.main_graph import flow_app  # full pipeline
# Optional: You can still import individual agents if you want to use them separately

@csrf_exempt
def generate_pitch(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            feedback = data.get("feedback", "")
            project_title = data.get("project_title", "")
            project_desc = data.get("project_desc", "")
            persona = data.get("persona", "college student")
            refinement_feedback = data.get("refinement_feedback", "")

            # Combine title and description for better context
            full_project_desc = f"{project_title}: {project_desc}"

            # Run the LangGraph pipeline
            state = {
                "feedback": feedback,
                "project_description": full_project_desc,
                "persona": persona,
                "refinement_feedback": refinement_feedback
            }

            result = flow_app.invoke(state)
            return JsonResponse({"result": result})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method is allowed."}, status=405)
