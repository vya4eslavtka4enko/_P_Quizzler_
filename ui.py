from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)
        self.label = Label()
        self.label.config(text='Score : 0')
        self.label.grid(column=1, row=0, pady=20)
        self.canvas_white = Canvas(width=300, height=250, bg='white')
        self.canvas_white.configure()
        self.canvas_white.grid(column=0, row=2, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas_white.create_text(155, 125, text="HELLO WORLD", fill="black", width=280,
                                                           font='Helvetica 15 bold')
        self.photoYes = PhotoImage(file="images/true.png")
        self.photoNo = PhotoImage(file="images/false.png")
        self.button_yes = Button()
        self.button_yes.config(image=self.photoYes, command=self.get_checkAnswer)
        self.button_yes.grid(column=0, row=3)
        self.button_no = Button()
        self.button_no.config(image=self.photoNo)
        self.button_no.grid(column=1, row=3, pady=20)
        self.get_next_question()
        self.get_checkAnswer()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas_white.itemconfig(self.question_text, text=q_text)

    def get_checkAnswer(self):
        q_answer = self.quiz.check_answer()
        print(q_answer)
