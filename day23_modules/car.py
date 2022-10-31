import random

from turtle import Turtle, Screen


class Car(Turtle):
    HEADING = 180
    SEGMENT_SIZE = 20
    STRETCH_FACTOR = 2
    SPEED = 30

    def __init__(self, screen: Screen):
        super().__init__(shape='square')
        self.screen = screen
        self.penup()
        self.color(self._get_color())
        self.turtlesize(stretch_len=self.STRETCH_FACTOR, stretch_wid=1)
        self.setheading(self.HEADING)

    def goto_start(self, y_coord):
        self.goto(self.screen.window_width() / 2 + self.SEGMENT_SIZE * self.STRETCH_FACTOR, y_coord)

    def move_forward(self):
        self.forward(self.speed())

    def out_of_sight(self):
        return self.xcor() < -1 * self.screen.window_width() / 2

    def stop(self):
        self.color('white')

    def hits(self, turtle):
        return (abs(self.ycor() - turtle.ycor()) <= self.SEGMENT_SIZE / 2) \
               and (self.distance(turtle) <= (self.STRETCH_FACTOR + 1) * self.SEGMENT_SIZE / 2) \
               and turtle.xcor() < self.xcor()

    @staticmethod
    def _get_color():
        return random.choice(['red', 'blue', 'yellow', 'black', 'silver', 'cyan'])
