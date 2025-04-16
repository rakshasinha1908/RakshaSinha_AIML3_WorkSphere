import csv
import random
from data_preprocessing import preprocess_answers

# Sample answer options for variety
answer_choices = [
    "Low", "A bit", "Moderate", "Somewhat", "Balanced", "Good", 
    "High", "Very high", "Very confident", "Excited", 
    "No", "Yes", "Productivity", "Learning", "Coding", "Very much"
]

# 15 sample questions (same order as in app)
questions = [
    "How would you describe your energy levels this morning?",
    "How motivated do you feel to work today?",
    "How well did you sleep last night?",
    "How confident are you feeling about achieving your goals today?",
    "Do you need any support today?",
    "What’s your top priority task for today?",
    "Are you facing any personal distractions today?",
    "Do you feel connected with your work and team today?",
    "What can make today a good day for you?",
    "Is there something you're anxious or excited about today?",
    "What’s your intention or focus for today?",
    "How confident are you about today's work?",
    "How do you feel about your workload for today?",
    "How much do you value feedback?",
    "Would you prefer a lighter workload today?"
]

# Generate 200 sample rows
with open('sample_wellbeing_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    header = [f"Q{i+1}" for i in range(len(questions))] + ["wellbeing_score"]
    writer.writerow(header)

    for _ in range(200):
        # Random responses
        answers = {q: random.choice(answer_choices) for q in questions}
        features = preprocess_answers(answers)

        # Randomly generate a target score based on average of features
        avg_score = sum(features) / len(features)
        wellbeing_score = round((avg_score / 5) * 100 + random.uniform(-10, 10), 2)
        wellbeing_score = max(min(wellbeing_score, 100), 0)

        writer.writerow(features + [wellbeing_score])
