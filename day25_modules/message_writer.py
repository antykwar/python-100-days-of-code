from turtle import Turtle, Screen


class MessageWriter(Turtle):
    def __init__(self, align='center', font=('Arial', 12, 'normal'), color='black'):
        super().__init__(visible=False)
        self.font = font
        self.align = align
        self.color(color)
        self.penup()

    def write_message(self, message: str):
        self.write(message, align=self.align, font=self.font)
        self._to_front()

    def _to_front(self):
        self.forward(0)
