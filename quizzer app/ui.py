from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text="nvfjvjd",
            fill=THEME_COLOR,
            font=("Arial", 20 ,"italic")
        )
        self.canvas.grid(row=1,column=0, columnspan = 2,pady=30)
        self.score_label  = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, command=self.true_anz)
        self.true_button.grid(row=2, column=0)
        false_button = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button,highlightthickness=0, command=self.false_anz)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)

    def true_anz(self):
        self.quiz.check_answer('True')

    def false_anz(self):
        self.quiz.check_answer("False")

