import random 

# 🧠 List of meaningful morning questions with metadata (all MCQ/Slider/Dropdown)
MORNING_QUESTIONS = [
    {"id": "q1", "text": "How would you describe your energy levels this morning?", "type": "slider"},
    {"id": "q2", "text": "How motivated do you feel to work today?", "type": "slider"},
    {"id": "q3", "text": "How well did you sleep last night?", "type": "slider"},
    {"id": "q4", "text": "How confident are you feeling about achieving your goals today?", "type": "slider"},
    {"id": "q5", "text": "Do you need any support today?", "type": "dropdown", "options": ["Yes", "No", "Maybe later"]},
    {"id": "q6", "text": "What’s your top priority task for today?", "type": "dropdown", "options": ["Meeting", "Coding", "Emails", "Documentation", "Other"]},
    {"id": "q7", "text": "Are you facing any personal distractions today?", "type": "dropdown", "options": ["Yes", "No", "A bit"]},
    {"id": "q8", "text": "Do you feel connected with your work and team today?", "type": "slider"},
    {"id": "q9", "text": "What can make today a good day for you?", "type": "dropdown", "options": ["Good communication", "Productivity", "Teamwork", "Self-care"]},
    {"id": "q10", "text": "Is there something you're anxious or excited about today?", "type": "dropdown", "options": ["Anxious", "Excited", "Both", "Neither"]},
    {"id": "q11", "text": "What’s your intention or focus for today?", "type": "dropdown", "options": ["Productivity", "Learning", "Teamwork", "Focus", "Well-being"]},
    {"id": "q12", "text": "How confident are you about today's work?", "type": "slider"},
    {"id": "q13", "text": "How do you feel about your workload for today?", "type": "slider"},
    {"id": "q14", "text": "How much do you value feedback?", "type": "dropdown", "options": ["Very much", "Somewhat", "Not much"]},
    {"id": "q15", "text": "Would you prefer a lighter workload today?", "type": "dropdown", "options": ["Yes", "No", "Indifferent"]}
]

def get_morning_questions(user_name=None):
    selected_questions = random.sample(MORNING_QUESTIONS, k=random.choice([3, 4]))

    if user_name:
        for q in selected_questions:
            if q["text"].startswith("What's") or q["text"].startswith("What’s"):
                q["text"] = f"{user_name}, {q['text']}"

    return selected_questions
