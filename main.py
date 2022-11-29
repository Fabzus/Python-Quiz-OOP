from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Import classes

question_bank = []
# A list that holds objects

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    # Appends question objects to the list

quiz = QuizBrain(question_bank)
quiz.next_question()
# initialize game

while quiz.still_has_questions():
    # while True:
    quiz.next_question()

# When still has questions becomes False:
print("==--==--==--==--==--==--==--==\n"
      "You've completed the quiz!!")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")
