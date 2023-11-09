from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from tkinter import *

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ai = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
# quiz_ui.canvas_white.itemconfig(text={question_bank[1]})
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
