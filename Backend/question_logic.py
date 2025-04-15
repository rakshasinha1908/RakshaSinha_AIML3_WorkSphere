import random

# 🧠 List of meaningful morning questions with metadata
MORNING_QUESTIONS = [
    {"id": "q1", "text": "What's one thing you're looking forward to today?", "type": "text"},
    {"id": "q2", "text": "Is there any support you need from your team or manager today?", "type": "text"},
    {"id": "q3", "text": "How would you describe your energy levels this morning?", "type": "slider"},
    {"id": "q4", "text": "Are there any blockers that might affect your productivity today?", "type": "text"},
    {"id": "q5", "text": "What's your top priority task for today?", "type": "text"},
    {"id": "q6", "text": "How motivated do you feel to work today?", "type": "slider"},
    {"id": "q7", "text": "How well did you sleep last night?", "type": "slider"},
    {"id": "q8", "text": "Is there something you're anxious or excited about today?", "type": "text"},
    {"id": "q9", "text": "What can make today a good day for you?", "type": "text"},
    {"id": "q10", "text": "Are you facing any personal distractions today?", "type": "text"},
    {"id": "q11", "text": "How confident are you feeling about achieving your goals today?", "type": "slider"},
    {"id": "q12", "text": "Is there any feedback you’d like to share from yesterday?", "type": "text"},
    {"id": "q13", "text": "What’s your intention or focus for today?", "type": "text"},
    {"id": "q14", "text": "Do you feel connected with your work and team today?", "type": "slider"},
    {"id": "q15", "text": "Is there anything you’d like to improve in your daily routine?", "type": "text"}
]

def get_morning_questions(user_name=None):
    """
    Returns 3–4 random morning questions as dictionaries.
    Optionally adds the user's name to personalize.
    """
    selected_questions = random.sample(MORNING_QUESTIONS, k=random.choice([3, 4]))

    if user_name:
        for q in selected_questions:
            if q["text"].startswith("What's") or q["text"].startswith("What’s"):
                q["text"] = f"{user_name}, {q['text']}"

    return selected_questions
