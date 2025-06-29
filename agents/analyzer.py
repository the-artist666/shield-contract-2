def analyze_contract(text):
    summary = (
        "⚠️ Found vague payment terms.\n"
        "⚠️ Termination clause favors client heavily.\n"
        "✅ Delivery timeline appears acceptable.\n"
    )

    tasks = [
        {"Task": "Kickoff", "Start": "2025-07-01", "End": "2025-07-03"},
        {"Task": "Milestone 1", "Start": "2025-07-04", "End": "2025-07-10"},
        {"Task": "Review + Feedback", "Start": "2025-07-11", "End": "2025-07-14"},
        {"Task": "Final Delivery", "Start": "2025-07-15", "End": "2025-07-20"},
    ]
    return summary, tasks
