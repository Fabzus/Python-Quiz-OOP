class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        # object variables

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # Returns a true of False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # Loads a question from the list
        self.question_number += 1
        # Increments question number by 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True or False?: \n").capitalize()
        # Gets input from user
        # Question number. Question text True or False?
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right!\nThe correct answer was {correct_answer}\n"
                  f"Your current score is {self.score}/{self.question_number}\n")
        else:
            print(f"I'm sorry, you got it wrong!\nThe correct answer was {correct_answer}\n "
                  f"Your current score is {self.score}/{self.question_number}\n")
        # Checks if answer given matches the correct answer
