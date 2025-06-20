function sendFeedback() {
    // Collect values from the HTML form
    const project_title = document.getElementById("project_title").value;
    const project_desc = document.getElementById("project_desc").value;
    const feedback = document.getElementById("feedback").value;
    const persona = document.getElementById("persona").value;
    const refinement_feedback = document.getElementById("refinement_feedback").value;

    // Construct the request payload
    const payload = {
        project_title: project_title,
        project_desc: project_desc,
        feedback: feedback,
        persona: persona,
        refinement_feedback: refinement_feedback
    };

    // Make the API call
    fetch("/api/generate-pitch/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
        if (data.result) {
            document.getElementById("result").innerText = JSON.stringify(data.result, null, 2);
        } else {
            document.getElementById("result").innerText = "❌ Error: " + data.error;
        }
    })
    .catch(err => {
        document.getElementById("result").innerText = "❌ Exception: " + err.message;
    });
}
