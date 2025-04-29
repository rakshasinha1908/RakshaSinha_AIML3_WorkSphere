"""
This module handles preprocessing of textual answers
from the morning check-in form into numerical features
for ML model prediction.
"""
 
def preprocess_answers(answers_dict):
    """
    Converts textual morning check-in responses into numeric values for ML prediction.

    Example input:
    answers_dict = {
        "How would you describe your energy levels this morning?": "Moderate",
        "How motivated do you feel to work today?": "High",
        ...
    }

    Returns:
        List of numerical features (ints) corresponding to each question.
    """

    mapping = {
        "Low": 1,
        "A bit": 2,
        "Moderate": 3,
        "Somewhat": 3,
        "Balanced": 3,
        "Good": 4,
        "High": 4,
        "Very high": 5,
        "Very confident": 5,
        "Excited": 5,
        "No": 1,
        "Yes": 5,
        "Productivity": 4,
        "Learning": 4,
        "Coding": 4,
        "Very much": 5,
    }
 
    features = []
    for q, a in answers_dict.items():
        features.append(mapping.get(a, 3))  # default = 3 (neutral)

    return features
def predict_wellbeing_score(answers_dict, model):
    features = preprocess_answers(answers_dict)
    print("Features after preprocessing:", features)  # Debug: check features
    
    # Predict using the model
    input_data = [features]
    print("Input data to model:", input_data)  # Debug: check input data
    
    predicted_score = model.predict(input_data)[0]  # Model prediction
    print("Predicted score from model:", predicted_score)  # Debug: check model's raw output
    
    # Clamp the predicted score to range [0, 100] if required
    predicted_score = max(min(predicted_score, 100), 0)
    print("Clamped predicted score:", predicted_score)  # Debug: check final score after clamping
    
    return predicted_score
