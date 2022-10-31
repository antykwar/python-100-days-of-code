from turtle import Turtle

from .paddle import Paddle


class Ball(Turtle):
    SEGMENT_SIZE = 20
    STEP = 5

    def __init__(self, screen, initial_speed, color='white', speed_multiplier=0.95):
        super().__init__(shape='circle')
        self.screen = screen
        self.x_move = self.STEP
        self.y_move = self.STEP
        self.initial_speed = initial_speed
        self.speed = self.initial_speed
        self.speed_multiplier = speed_multiplier
        self.penup()
        self.color(color)
        self.goto(0, 0)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        if self._need_bounce_y():
            self._bounce_y()

    def check_paddle_hit(self, paddle: Paddle):
        if self._need_bounce_x(paddle):
            self._bounce_x()

    def check_success_side(self, back_lines: tuple):
        if not (self.xcor() < back_lines[0] or self.xcor() > back_lines[1]):
            return None
        success_side = 'right' if self.xcor() < 0 else 'left'
        self._reset()
        return success_side

    def _need_bounce_x(self, paddle: Paddle):
        ball_back_line = paddle.get_back_line_for_ball()
        if not (0 > ball_back_line >= self.xcor() or self.xcor() >= ball_back_line > 0):
            return False
        if self.distance(paddle) > paddle.get_hit_distance_for_ball():
            return False
        return True

    def _need_bounce_y(self):
        return abs(self.ycor()) > self.screen.window_height() / 2 - self.SEGMENT_SIZE

    def _bounce_x(self):
        self.x_move *= -1
        self.speed *= self.speed_multiplier

    def _bounce_y(self):
        self.y_move *= -1
        self.speed *= self.speed_multiplier

    def _reset(self):
        self.goto(0, 0)
        self.speed = self.initial_speed
        self._bounce_x()
