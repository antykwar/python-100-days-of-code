from turtle import Turtle, Screen


class MessageWriter(Turtle):
    def __init__(self, screen: Screen, slot='center', align='center', font=('Arial', 24, 'normal'), color='black'):
        super().__init__(visible=False)
        self.screen = screen
        self.font = font
        self.align = align
        self.set_slot(slot)
        self.color(color)

    def set_slot(self, slot, x_position=None, y_position=None):
        if slot not in ('top', 'center', 'bottom'):
            return

        self.setheading(0)

        if slot == 'center':
            self.goto(0, 0)
            return

        if not x_position:
            x_position = 0

        if not y_position:
            extra_space = self.font[1] * 2 if slot == 'top' else self.font[1]
            y_position = self.screen.window_height() / 2 - extra_space
            if slot == 'bottom':
                y_position *= -1

        self.goto(x_position, y_position)

    def write_message(self, message: str):
        self.clear_message()
        self.write(message, align=self.align, font=self.font)

    def clear_message(self):
        self.clear()

    def get_height_on_screen(self):
        return self.screen.window_height() / 2 - self.ycor()


