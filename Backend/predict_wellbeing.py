import pickle
from data_preprocessing import preprocess_answers

def predict_wellbeing(user_answers):
    # Preprocess karo answers ko (mapping to numbers)
    features = preprocess_answers(user_answers)

    # Load trained model
    with open("wellbeing_model.pkl", "rb") as file:
        model = pickle.load(file)

    # Predict wellbeing score
    prediction = model.predict([features])[0]
    return round(prediction, 2)  # 2 decimal places
