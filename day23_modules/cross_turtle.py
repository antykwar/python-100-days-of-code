from turtle import Turtle, Screen


class CrossTurtle(Turtle):
    HEADING = 90
    SEGMENT_SIZE = 20
    STEP = 10

    road_is_crossed: False

    def __init__(self, screen: Screen, color: str):
        super().__init__(shape='turtle')
        self.screen = screen
        self.penup()
        self.color(color)
        self.setheading(self.HEADING)
        self.goto_start()

    def goto_start(self):
        self.road_is_crossed = False
        self.goto(0, -1 * (self.screen.window_height() / 2 - self.SEGMENT_SIZE))

    def move(self):
        self.forward(self.STEP)
        if self.has_crossed_the_road():
            self.road_is_crossed = True

    def has_crossed_the_road(self):
        return self.ycor() > self.screen.window_height() / 2 - 2.5 * self.SEGMENT_SIZE
