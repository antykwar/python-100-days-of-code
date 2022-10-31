import math
from tkinter import *

from PIL import Image as PilImage

from .pomodoro_settings import PomodoroSettings


class Pomodoro(Tk):
    CHECKMARK = '✔'

    def __init__(self):
        super().__init__()
        self.settings = PomodoroSettings
        self._step = 0
        self._setup()
        self._create_ui()

    def start(self):
        self.mainloop()

    def _setup(self):
        self.title(self.settings.APPLICATION_TITLE)
        self.minsize(width=self.settings.WINDOW_MIN_WIDTH, height=self.settings.WINDOW_MIN_HEIGHT)
        self.iconphoto(False, PhotoImage(file=self.settings.APPLICATION_ICON))
        self.resizable(False, False)

    def _reset_header(self):
        self._header.config(
            text='Ready to work',
            fg=PomodoroSettings.LABEL_COLOR
        )

    def _reset_footer(self):
        self._check_deck.config(text='')

    def _reset_timer(self):
        self._canvas.itemconfig(
            self._timer_screen,
            text='00:00'
        )

    def _create_ui(self):
        self.config(
            padx=self.settings.WINDOW_PADDING_X,
            pady=self.settings.WINDOW_PADDING_Y,
            bg=self.settings.BACKGROUND_COLOR,
        )
        self._prepare_canvas()
        self._prepare_header()
        self._prepare_check_deck()
        self._prepare_buttons()

    def _prepare_buttons(self):
        _, padding_y = Pomodoro._get_canvas_size(self.settings.BACKGROUND_IMAGE)
        start_button = Button(
            text='Start',
            font=self.settings.FONT_BUTTON,
            command=self._start_button_command
        )
        start_button.grid(
            column=0,
            row=1,
            padx=self.settings.START_BUTTON_PADDING,
            pady=(padding_y, 0)
        )
        reset_button = Button(
            text='Reset',
            font=self.settings.FONT_BUTTON,
            command=self._reset_button_command
        )
        reset_button.grid(
            column=2,
            row=1,
            padx=self.settings.STOP_BUTTON_PADDING,
            pady=(padding_y, 0)
        )

    def _start_button_command(self, auto_mode=False):
        if self._step > 0 and not auto_mode:
            return

        self._step += 1
        work_map = self.settings.get_work_map()
        if self._step > len(work_map):
            self._header.config(text='Work finished')
            return

        self._is_stage = work_map[self._step]['is_stage']

        self._header.config(
            text=work_map[self._step]['header'],
            fg=work_map[self._step]['color']
        )
        self._count_down(work_map[self._step]['length'])

    def _reset_button_command(self):
        if self._timer:
            self.after_cancel(self._timer)
        self._step = 0
        self._reset_header()
        self._reset_footer()
        self._reset_timer()

    def _prepare_check_deck(self):
        self._check_deck = Label(
            text='',
            font=self.settings.get_check_deck_font(),
            bg=self.settings.BACKGROUND_COLOR,
            fg=self.settings.LABEL_COLOR
        )
        self._check_deck.grid(column=1, row=2, pady=self.settings.DECK_PADDING_Y)

    def _prepare_header(self):
        self._header = Label(
            font=self.settings.get_header_font(),
            bg=self.settings.BACKGROUND_COLOR,
            fg=self.settings.LABEL_COLOR
        )
        self._reset_header()
        self._header.grid(column=1, row=0, pady=self.settings.HEADER_PADDING_Y)

    def _prepare_canvas(self):
        background_image_path = self.settings.BACKGROUND_IMAGE
        canvas_width, canvas_height = Pomodoro._get_canvas_size(background_image_path)
        self._canvas = Canvas(
            width=canvas_width,
            height=canvas_height,
            bg=self.settings.BACKGROUND_COLOR,
            border=0,
            highlightthickness=0
        )
        self._background_image = PhotoImage(file=background_image_path)
        self._canvas.create_image(canvas_width / 2, canvas_height / 2, image=self._background_image)
        self._timer_screen = self._canvas.create_text(
            canvas_width / 2 + self.settings.CLOCK_HORIZONTAL_SHIFT,
            canvas_height / 2 + self.settings.CLOCK_VERTICAL_SHIFT,
            font=self.settings.get_timer_font()
        )
        self._reset_timer()
        self._canvas.grid(column=1, row=1)

    def _count_down(self, start_value):
        minutes, seconds = divmod(start_value, 60)
        self._canvas.itemconfig(
            self._timer_screen,
            text=f'{minutes:02d}:{seconds:02d}'
        )
        if start_value > 0:
            self._timer = self.after(1000, self._count_down, start_value - 1)
        else:
            if self._is_stage:
                self._add_check_mark()
                self._is_stage = False
            self._start_button_command(auto_mode=True)

    def _add_check_mark(self):
        current_marks = self._check_deck['text']
        self._check_deck.config(text=current_marks + self.CHECKMARK)

    @staticmethod
    def _get_canvas_size(background_image_path):
        background_image = PilImage.open(background_image_path)
        canvas_width = Pomodoro._round_to_nearest_even_number(background_image.width)
        canvas_height = Pomodoro._round_to_nearest_even_number(background_image.height)
        background_image.close()
        return canvas_width, canvas_height

    @staticmethod
    def _round_to_nearest_even_number(number):
        return math.ceil(number / 2) * 2
