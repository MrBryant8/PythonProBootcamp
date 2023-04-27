from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
WRONG = "images/false.png"
RIGHT = "images/true.png"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=270, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Questions",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        wrong_img = PhotoImage(file=WRONG)
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false_clicked)
        self.wrong_button.grid(column=1, row=2)

        right_img = PhotoImage(file=RIGHT)
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true_clicked)
        self.right_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        self.score_label.config(text="Score: {}".format(self.quiz.score))

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question,
                                   text="You've completed the quiz!\nFinal score: {}/10".format(self.quiz.score))
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.canvas.config(bg="green") if is_right else self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
