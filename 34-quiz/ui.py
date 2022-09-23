import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)
        self.btn_img_green = tk.PhotoImage(file="./images/true.png")
        self.btn_img_red = tk.PhotoImage(file="./images/false.png")

        self.btn_green = tk.Button(
            image=self.btn_img_green,
            width=100,
            height=100,
            fg="white",
            highlightthickness=0,
            command=self.true_pressed,
        )

        self.btn_red = tk.Button(
            image=self.btn_img_red,
            width=100,
            height=100,
            fg="white",
            highlightthickness=0,
            command=self.false_pressed,
        )

        self.label = tk.Label(
            text="Score: 0", font=("Arial", 10), bg=THEME_COLOR, fg="white"
        )
        self.label.grid(row=0, column=1)
        self.btn_green.grid(row=2, column=0)
        self.btn_red.grid(row=2, column=1)

        self.canvas = tk.Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, text="HEllo", font=("Arial", 20, "italic"), width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You reached the end of game"
            )
            self.btn_red.config(state="disabled")
            self.btn_green.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
