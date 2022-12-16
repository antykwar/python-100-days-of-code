from tkinter import *

from day34_modules.quiz_brain import QuizBrain


class Quizzer:
    THEME_COLOR = "#375362"
    WHITE_COLOR = "#FFFFFF"
    RED_COLOR = "#FF0000"
    GREEN_COLOR = "#00FF00"

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.current_question = None
        self._active_timer = None
        self._prepare_interface()

    def _prepare_interface(self):
        self.window = Tk()
        self.window.title('Quizzer')
        self.window.resizable(False, False)
        self.window.configure(
            padx=20,
            pady=20,
            bg=self.THEME_COLOR
        )

        self._images = []
        self.current_question = None

        self.score_label = Label(font=('Arial', 20), bg=self.THEME_COLOR, fg=self.WHITE_COLOR)
        self.set_score(0)
        self.score_label.grid(row=0, column=1)

        self.question_field = Canvas(
            width=500,
            height=250,
            bg=self.WHITE_COLOR,
            border=0,
            highlightthickness=0
        )
        self.question_field.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.question_field.create_text(
            250,
            125,
            width=400,
            text='',
            font=('Arial', 20, 'italic'),
            fill=self.THEME_COLOR
        )

        self._images.append(PhotoImage(file='./day34_files/images/true.png'))
        self.true_button = Button(
            height=97,
            width=100,
            bg=self.THEME_COLOR,
            image=self._images[-1],
            command=lambda: self.check_question(True)
        )
        self.true_button.grid(row=2, column=0)

        self._images.append(PhotoImage(file='./day34_files/images/false.png'))
        self.false_button = Button(
            height=97,
            width=100,
            bg=self.THEME_COLOR,
            image=self._images[-1],
            command=lambda: self.check_question(False)
        )
        self.false_button.grid(row=2, column=1)

    def start(self):
        self.ask_question()
        self.window.mainloop()

    def set_score(self, score):
        self.score_label.configure(text=f'Score: {score}')

    def set_question(self, text):
        self.question_field.itemconfig(self.question_text, text=text)
        self.question_field.configure(bg=self.WHITE_COLOR)

    def check_question(self, answer):
        self.disable_buttons()
        if self.current_question.is_correct(answer):
            self.quiz_brain.add_score()
            self.set_score(self.quiz_brain.get_total_score())
            self.question_field.configure(bg=self.GREEN_COLOR)
        else:
            self.question_field.configure(bg=self.RED_COLOR)
        self._active_timer = self.window.after(3000, self.clear_by_timer)

    def ask_question(self):
        self.current_question = self.quiz_brain.ask_question()
        if self.current_question is None:
            self.disable_buttons()
            self.set_question('That`s all, folks!')
            return
        self.set_question(self.current_question.text)

    def clear_by_timer(self):
        self.disable_buttons(False)
        self.window.after_cancel(self._active_timer)
        self.question_field.configure(bg=self.WHITE_COLOR)
        self.ask_question()

    def disable_buttons(self, disable=True):
        state = 'disabled' if disable else 'normal'
        self.true_button['state'] = state
        self.false_button['state'] = state
