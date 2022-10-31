import datetime
from random import randrange, uniform, choice

from turtle import Turtle

from .super_turtle_directions import SuperTurtleDirections


class SuperTurtle(Turtle):
    def __init__(self, colormode=255):
        super().__init__(shape='turtle')
        self.colormode = colormode

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

    def rectangle(self, x_size, y_size, direction=SuperTurtleDirections.DIRECTION_TOP_RIGHT, rotation=0):
        if direction not in SuperTurtleDirections.get_list():
            direction = SuperTurtleDirections.DIRECTION_TOP_RIGHT

        old_heading = self.heading()
        self.setheading(direction + rotation)

        if direction in (SuperTurtleDirections.DIRECTION_TOP_RIGHT, SuperTurtleDirections.DIRECTION_BOTTOM_LEFT):
            x_size, y_size = y_size, x_size

        movements = (x_size, y_size) * 2

        for side_size in movements:
            self.forward(side_size)
            self.right(90)

        self.setheading(old_heading)

    def square(self, size, direction=SuperTurtleDirections.DIRECTION_TOP_RIGHT, rotation=0):
        self.rectangle(size, size, direction, rotation)

    def draw_shape(self, side, angles_amount, direction=SuperTurtleDirections.DIRECTION_TOP_RIGHT, rotation=0):
        old_heading = self.heading()
        self.setheading(direction + rotation)

        rotation_angle = 360 / angles_amount
        for _ in range(angles_amount):
            self.forward(side)
            self.right(rotation_angle)

        self.setheading(old_heading)

    def set_random_color(self):
        if self.colormode == 255:
            # noinspection PyTypeChecker
            self.pencolor(tuple(randrange(1, 255, 1) for _ in range(3)))
            return
        # noinspection PyTypeChecker
        self.pencolor(tuple(uniform(0, 1) for _ in range(3)))

    def draw_spirography(self, radius=100, steps=30):
        rotation_angle = 360 / steps
        for _ in range(steps):
            self.circle(radius)
            self.set_random_color()
            self.right(rotation_angle)

    def random_walk(self, step_size=50, time_to_walk=30):
        directions = SuperTurtleDirections.get_list()
        begin_time = datetime.datetime.now().timestamp()

        while datetime.datetime.now().timestamp() < begin_time + time_to_walk:
            direction = choice(directions)
            self.setheading(direction)
            self.forward(step_size)
            self._prevent_border_crossing(step_size)
            self.set_random_color()

    def paint_spots_picture(self, colors_list, size_x=10, size_y=10, spot_size=20, space=50):
        is_down_old = self.isdown()
        self.penup()

        initial_x = self.xcor() - self._calculate_initial_shift(size_x, spot_size, space)
        initial_y = self.ycor() - self._calculate_initial_shift(size_y, spot_size, space)
        shift = space + spot_size

        self.goto(initial_x, initial_y)

        for y_position in range(1, size_y + 1):
            for x_position in range(1, size_x + 1):
                self.dot(spot_size, choice(colors_list))
                if x_position != size_x:
                    self.forward(shift)
            if y_position != size_y:
                self.goto(initial_x, initial_y + shift * y_position)

        if is_down_old:
            self.pendown()

    def _prevent_border_crossing(self, step_size):
        screen = self.getscreen()
        width = screen.window_width()
        height = screen.window_height()

        if not -(width / 2) < self.xcor() - step_size < (width / 2):
            self.backward(step_size)
        if not -(height / 2) < self.ycor() - step_size < (height / 2):
            self.backward(step_size)

    @staticmethod
    def _calculate_initial_shift(size, spot_size, space):
        if size % 2 == 0:
            return size / 2 * spot_size + space * (size / 2 - 0.5) - 0.5 * spot_size
        else:
            return (size // 2) * (spot_size + space) - 0.5 * spot_size
