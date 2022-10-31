from tkinter import *


class ImageButton(Button):
    IMAGES = {
        'right': 'day31_files/images/right.png',
        'wrong': 'day31_files/images/wrong.png',
    }

    def __init__(self, width, height, button_type, command):
        self._image = None
        if button_type in self.IMAGES.keys():
            self._image = PhotoImage(file=self.IMAGES[button_type])
        super().__init__(
            width=width,
            height=height,
            image=self._image,
            highlightthickness=0,
            command=command
        )

