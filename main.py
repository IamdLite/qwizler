from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []


for data in question_data:
    question = Question(data["question"], data["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
user_interface = QuizInterface(quiz)




# while quiz.still_has_question() == False:
#     quiz.next_question()
# print("You've completed the quiz")
# print(f"Your total score is {quiz.score}/{quiz.question_number}")
     
