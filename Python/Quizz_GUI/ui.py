from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(pady=20, padx=20,background=THEME_COLOR)
        #buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1)
        #canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, width= 270, text="", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #clabel
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.next()

        self.window.mainloop()

    def next(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(background="white")

    def true(self):
        self.feedback(self.quiz.check_answer("true"))

    def false(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, on_off):
        if on_off:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next)






