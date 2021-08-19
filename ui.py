from tkinter import *
from quiz_brain import QuizBrain

# Files
LOGO_IMG = "images/logo.png"
TRUE_IMG = "images/true.png"
FALSE_IMG = "images/false.png"

# Stylistics
COLORS = {
    "dark blue": "#14213d",
    "blue": "78c0e0",
    "orange": "#fca311",
    "green": "#419d78",
    "red": "#ee6352",
    "white": "#e5e5e5"
}

QUESTION_FONT = ("arial", 16, "italic")
SCORE_FONT = ("arial", 12)

# Functionality
TIME_BG_COLOR = 1000


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        # Window
        self.window = Tk()
        self.window.title("Leo's Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=COLORS["dark blue"])

        # Canvas
        self.logo_canvas = Canvas(width=200, height=200, bg=COLORS["dark blue"], highlightthickness=0)
        logo_img = PhotoImage(file=LOGO_IMG)
        self.logo_canvas.create_image(100, 100, image=logo_img)
        self.logo_canvas.grid(row=0, column=0, columnspan=2)

        self.text_box_canvas = Canvas(width=300, height=250, bg=COLORS["white"], highlightthickness=0)
        question = self.quiz_brain.next_question()
        self.question_text = self.text_box_canvas.create_text(
            150,
            125,
            width=280,
            text=question,
            font=QUESTION_FONT,
            fill=COLORS["dark blue"]
        )
        self.text_box_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Label
        self.score_label = Label(text=f"Score: {self.quiz_brain.score}", font=SCORE_FONT, bg=COLORS["dark blue"], fg=COLORS["white"])
        self.score_label.grid(row=0, column=1, sticky="ne")

        # Buttons
        true_img = PhotoImage(file=TRUE_IMG)
        self.correct_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)

        false_img = PhotoImage(file=FALSE_IMG)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.text_box_canvas.configure(bg=COLORS["white"])
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.text_box_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.text_box_canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz.\n\n"
                     f"Your final score was {self.quiz_brain.score}/{self.quiz_brain.question_number}."
            )
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_correct = self.quiz_brain.check_answer("True")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz_brain.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_right):
        if is_right:
            self.text_box_canvas.configure(bg=COLORS["green"])
        else:
            self.text_box_canvas.configure(bg=COLORS["red"])

        self.window.after(TIME_BG_COLOR, self.get_next_question)


