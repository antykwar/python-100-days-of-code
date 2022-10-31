from turtle import Turtle


class NetDrawer(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()

    def dashed_line(self, length, strip_size=10, gap_size=10):
        total_distance = 0
        is_down_old = self.isdown()

        self.pendown()

        while total_distance < length:
            is_down = self.isdown()
            step_length = strip_size if is_down else gap_size
            self.forward(step_length)
            self.penup() if is_down else self.pendown()
            total_distance += step_length

        self.pendown() if is_down_old else self.penup()
