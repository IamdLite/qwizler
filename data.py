import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_d = {}
question_data = data["results"]


# print("\n", question_data)



# question_data = [
#     {"q_text": "A slug's blood is green.", 
#      "q_answer": "True"},
    
#     {"q_text": "The loudest animal is the African Elephant.", 
#      "q_answer": "False"},

#     {"q_text": "Approximately one quarter of hman bones are in the feet.", 
#      "q_answer": "True"},

#     {"q_text": "The total surface area of a human long is the size of a football pitch.", 
#      "q_answer": "False"},

#      {"q_text": "In West Virginia, if you accidentally hit an animal with a car, you are free to take him home", 
#      "q_answer": "False"},

#      {"q_text": "Falling in love is as a result of a chemical reaction that happens in your brain.", 
#      "q_answer": "True"},

#      {"q_text": "It is illegal to pee in the ocean in Portugal.", 
#      "q_answer": "True"},

#      {"q_text": "You can lead a car donstairs but not upstairs.", 
#      "q_answer": "False"},

#      {"q_text": "Google was originally called 'Backrub.", 
#      "q_answer": "True"},

#      {"q_text": "Prostitution is legal in Spain.", 
#      "q_answer": "True"},

#      {"q_text": "Solomon was the richest man of his time.", 
#      "q_answer": "True"},

#      {"q_text": "A few ounces of chocolate can kill a small dog.", 
#      "q_answer": "True"},


# ]