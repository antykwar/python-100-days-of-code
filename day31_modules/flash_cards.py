from tkinter import *

from .card import Card
from .image_button import ImageButton
from .settings import Settings
from .data_provider import DataProvider


class FlashCards(Tk):
    def __init__(self):
        super().__init__()
        self._interface = {}
        self.init_interface()
        self._provider = DataProvider(new_language='French', known_language='English')
        self._active_timer = None

    def start(self):
        self.mainloop()

    def init_interface(self):
        self.config(
            padx=50,
            pady=50,
            bg=Settings.BACKGROUND_COLOR,
        )
        self.title(Settings.APPLICATION_TITLE)
        self.resizable(False, False)
        self._interface['card'] = Card(width=800, height=528)
        self._interface['card'].grid(column=0, row=0, columnspan=2)
        self._interface['wrong_button'] = ImageButton(
            width=100,
            height=100,
            button_type='wrong',
            command=lambda: self.set_random_word(False)
        )
        self._interface['wrong_button'].grid(column=0, row=1)
        self._interface['right_button'] = ImageButton(
            width=100,
            height=100,
            button_type='right',
            command=lambda: self.set_random_word(True)
        )
        self._interface['right_button'].grid(column=1, row=1)

    def set_random_word(self, is_word_known):
        self._clear_timer()

        if self._provider.current_new_word is not None:
            self._provider.mark_word_as_known(is_word_known)

        word = self._provider.get_random_word()
        if word is None:
            return
        self._interface['card'].set_labels_text(
            language=self._provider.new_language,
            word=self._provider.current_new_word
        )
        self._active_timer = self.after(3000, self._flip_card)

    def _flip_card(self):
        self._clear_timer()
        self._interface['card'].set_labels_text(
            language=self._provider.known_language,
            word=self._provider.current_known_word,
            mode='back'
        )

    def _clear_timer(self):
        if self._active_timer is not None:
            self.after_cancel(self._active_timer)
            self._active_timer = None
