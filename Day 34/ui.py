from time import sleep
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, )

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Quastion Goes HERE", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file="Day 34/images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.pressing_right)
        self.right_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file="Day 34/images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.pressing_wrong)
        self.wrong_button.grid(row=2, column=1)        

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig( self.question_text, 
                text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def pressing_right(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)
    
    def pressing_wrong(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background='green')
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)