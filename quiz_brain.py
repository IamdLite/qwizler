import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_answer = ""
        self.score = 0
        self.is_right: bool = None  
    def still_has_question(self):
        if self.question_number <= len(self.question_list) - 1:
            return True
        else:
            return False
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            # print("You got it right!")
            # print(f"The correct answer was: {correct_answer}.")
            # print(f"Your current score is: {self.score}/{self.question_number}.\n")
            return True
        else:
            # print("You got it wrong!")
            # print(f"The correct answer was: {correct_answer}.")
            # print(f"Your current score is: {self.score}/{self.question_number}.\n")
            return False
            
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.q_text)
        return f"Q.{self.question_number}: {q_text} (True/False)?: "
        # self.user_answer = input(f"Q.{self.question_number}: {q_text} (True/False)?: ")
        # self.check_answer(self.user_answer, self.current_question.q_answer)
