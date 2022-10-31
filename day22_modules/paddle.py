from turtle import Turtle


class Paddle(Turtle):
    SEGMENT_SIZE = 20

    def __init__(self, screen, color='white', length=4, position='left'):
        super().__init__()
        self.screen = screen
        self.back_line_coordinate = None
        self.length = length

        self.shape('square')
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=length, stretch_len=1)

        self._set_position(position)

    def up(self):
        self._move_paddle(self.SEGMENT_SIZE)
        pass

    def down(self):
        self._move_paddle(-1 * self.SEGMENT_SIZE)
        pass

    def get_back_line_for_ball(self):
        ball_back_line = \
            self.back_line_coordinate - self.SEGMENT_SIZE \
            if self.back_line_coordinate > 0 \
            else self.back_line_coordinate + self.SEGMENT_SIZE
        return ball_back_line

    def get_hit_distance_for_ball(self):
        return self.length * self.SEGMENT_SIZE / 2

    def _set_position(self, position):
        max_x = self.screen.window_width() / 2
        self.back_line_coordinate = \
            (max_x // self.SEGMENT_SIZE) \
            * (self.SEGMENT_SIZE - 1) \
            * (1 if position == 'right' else -1)

        self.goto(self.back_line_coordinate, 0)

    def _move_paddle(self, shift):
        max_y = self.screen.window_height() / 2
        if shift < 0 and self.ycor() <= -1 * (max_y - self.SEGMENT_SIZE * self.length / 2):
            return
        if shift > 0 and self.ycor() >= (max_y - self.SEGMENT_SIZE * self.length / 2):
            return
        self.goto(self.xcor(), self.ycor() + shift)
