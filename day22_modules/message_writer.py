from turtle import Turtle, Screen


class MessageWriter(Turtle):
    def __init__(self, screen: Screen, align='center', font=('Arial', 24, 'normal'), color='white'):
        super().__init__(visible=False)
        self.screen = screen
        self.font = font
        self.align = align
        self.color(color)
        self.penup()

    def write_message(self, message: str):
        self.clear_message()
        self.write(message, align=self.align, font=self.font)

    def clear_message(self):
        self.clear()
