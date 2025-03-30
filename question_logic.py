import random

# 🧠 List of meaningful morning questions
MORNING_QUESTIONS = [
    "What's one thing you're looking forward to today?",
    "Is there any support you need from your team or manager today?",
    "How would you describe your energy levels this morning?",
    "Are there any blockers that might affect your productivity today?",
    "What's your top priority task for today?",
    "How motivated do you feel to work today?",
    "How well did you sleep last night?",
    "Is there something you're anxious or excited about today?",
    "What can make today a good day for you?",
    "Are you facing any personal distractions today?",
    "How confident are you feeling about achieving your goals today?",
    "Is there any feedback you’d like to share from yesterday?",
    "What’s your intention or focus for today?",
    "Do you feel connected with your work and team today?",
    "Is there anything you’d like to improve in your daily routine?"
]

def get_morning_questions(user_name=None):
    """
    Returns 3–4 random morning questions. Optionally adds the user's name to personalize.
    """
    selected_questions = random.sample(MORNING_QUESTIONS, k=random.choice([3, 4]))

    if user_name:
        personalized = []
        for q in selected_questions:
            if q.startswith("What's") or q.startswith("What’s"):
                personalized.append(f"{user_name}, {q}")
            else:
                personalized.append(q)
        return personalized

    return selected_questions
