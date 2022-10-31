import tkinter.font
from tkinter import *

from .settings import Settings


class Card(Canvas):
    INIT_STATE = 'front'

    IMAGES = {
        'back': 'day31_files/images/card_back.png',
        'front': 'day31_files/images/card_front.png',
    }

    BACKGROUNDS = {
        'back': Settings.BACKGROUND_COLOR_LABEL_BACK,
        'front': Settings.BACKGROUND_COLOR_LABEL_FRONT,
    }

    def __init__(self, width, height):
        super().__init__(
            width=width,
            height=height,
            border=0,
            highlightthickness=0,
            bg=Settings.BACKGROUND_COLOR,
        )
        self._background_image = PhotoImage(file=self.IMAGES[self.INIT_STATE])
        self._canvas_background_image = self.create_image(width // 2, height // 2, image=self._background_image)
        self._init_labels(self.INIT_STATE, width, height)
        self.set_labels_text(language='Welcome!', word="Press any button\nto start")

    def _init_labels(self, label_type, field_width, field_height):
        self._labels = {
            'language': Label(font=('Arial', 40, tkinter.font.ITALIC), bg=Settings.BACKGROUND_COLOR),
            'word': Label(font=('Arial', 60, tkinter.font.BOLD), bg=Settings.BACKGROUND_COLOR),
        }
        self._labels['language'].place(x=field_width // 2, y=field_height // 2 - field_height // 4, anchor='center')
        self._labels['word'].place(x=field_width // 2, y=field_height // 2, anchor='center')
        self._set_labels_background_color(label_type)

    def _set_labels_background_color(self, label_type):
        if label_type not in self.BACKGROUNDS:
            raise KeyError(f'Background of type <{label_type}> not found in the list.')
        for label in self._labels.values():
            label.config(bg=self.BACKGROUNDS[label_type])

    def set_labels_text(self, mode='front', language=None, word=None):
        if language is not None:
            self._labels['language'].config(text=language)
        if word is not None:
            self._labels['word'].config(text=word)
        self._set_labels_background_color(mode)
        self._background_image = PhotoImage(file=self.IMAGES[mode])
        self.itemconfig(self._canvas_background_image, image=self._background_image)
