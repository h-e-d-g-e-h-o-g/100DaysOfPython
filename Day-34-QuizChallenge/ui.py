from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        right_button_img = PhotoImage(file="images/true.png")
        wrong_button_img = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_button_img, command=self.true_said)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=wrong_button_img, command=self.false_said)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.right_button.config(state=ACTIVE)
        self.wrong_button.config(state=ACTIVE)
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached at the end!")
            self.right_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)

    def true_said(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_said(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.right_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)
        else:
            self.canvas.config(background="red")
            self.right_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)
        self.window.after(1000, self.get_next_question)