from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.lbl_score = Label(text=f"Score:{0}", bg=THEME_COLOR, fg="white", font=("Arial", 14))
        self.lbl_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.txt_questions = self.canvas.create_text(150, 125, width=280, text="Here goes the question", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.img_right = PhotoImage(file="images/true.png")
        self.btn_right = Button(image=self.img_right, highlightthickness=0, command=self.true_pressed)
        self.btn_right.grid(row=2, column=0, pady=10)

        self.img_wrong = PhotoImage(file="images/false.png")
        self.btn_wrong = Button(image=self.img_wrong, highlightthickness=0, command=self.false_pressed)
        self.btn_wrong.grid(row=2, column=1)

        self.get_next_questions()

        self.window.mainloop()

    def get_next_questions(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.txt_questions, text=q_text)
        else:
            self.canvas.itemconfig(self.txt_questions, text="You've reached the end of the quiz.")
            self.btn_wrong.config(state="disabled")
            self.btn_right.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_questions)
