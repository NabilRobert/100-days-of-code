from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 30, "bold")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=50, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=1)
        # text
        self.question_text = self.canvas.create_text(150, 125, text=f'"goofy"', width=280,
                                                     font=("Arial", 15, "bold"), fill="black")
        self.score_label = Label(text="score:0", font=("Arial", 15, "bold"), bg=f"{THEME_COLOR}", fg="white")
        self.score_label.grid(row=0, column=2)
        self.canvas.place()

        # button
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_button)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command = self.false_button)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="There are no more questions, mortal")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)