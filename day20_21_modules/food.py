from random import randint

from turtle import Turtle


class Food(Turtle):
    SEGMENT_SIZE = 20
    SIZE_MULTIPLIER = 0.5

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.penup()
        self.shape('circle')
        self.color('yellow')
        self.shapesize(stretch_wid=self.SIZE_MULTIPLIER, stretch_len=self.SIZE_MULTIPLIER)

    def appear_randomly(self, margin_top=0, margin_bottom=0, margin_left=0, margin_right=0):
        max_x = self.screen.window_width() / 2 - self.SEGMENT_SIZE
        max_y = self.screen.window_height() / 2 - self.SEGMENT_SIZE
        x_position = randint(-1 * (max_x - margin_left), max_x - margin_right)
        y_position = randint(-1 * (max_y - margin_bottom), max_y - margin_top)
        self.goto(x_position, y_position)

    def get_fruit_size(self):
        return self.SEGMENT_SIZE * self.SIZE_MULTIPLIER
