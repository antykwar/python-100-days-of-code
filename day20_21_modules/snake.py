from turtle import Turtle


class Snake:
    SEGMENT_SIZE = 20

    def __init__(self, screen, color='white', length=3):
        self.segments = []
        self.head = None
        self.color = color
        self.screen = screen
        self.turn_direction = []
        self.init_snake(length)

    def init_snake(self, length):
        for index in range(length):
            segment = self._init_segment()
            segment.backward(self.SEGMENT_SIZE * index)
            self.segments.append(segment)
        self.head = self.segments[0]
        self.segments.reverse()

    def _init_segment(self):
        segment = Turtle(shape='square')
        segment.color(self.color)
        segment.penup()
        return segment

    def move_forward(self):
        for index, segment in enumerate(self.segments):
            if index == len(self.segments) - 1:
                self._rotate_head()
                segment.forward(self.SEGMENT_SIZE)
                continue
            previous_segment = self.segments[index + 1]
            segment.goto(previous_segment.xcor(), previous_segment.ycor())

    def turn_left(self):
        self.turn_direction.append(90)

    def turn_right(self):
        self.turn_direction.append(-90)

    def can_eat_food(self, food):
        return self.head.distance(food) < food.get_fruit_size() + 5

    def grow_up(self):
        new_last_segment = self._init_segment()
        old_last_segment = self.segments[0]
        new_last_segment.goto(old_last_segment.xcor(), old_last_segment.ycor())
        self.segments.insert(0, new_last_segment)

    def has_boarder_collision(self, field_params):
        x_cor = self.head.xcor()
        y_cor = self.head.ycor()
        return x_cor > field_params['x_max'] \
            or x_cor < field_params['x_min'] \
            or y_cor > field_params['y_max'] \
            or y_cor < field_params['y_min']

    def has_self_collision(self):
        for segment in self.segments[:len(self.segments) - 1]:
            if self.head.distance(segment) < self.SEGMENT_SIZE / 2:
                return True
        return False

    def _rotate_head(self):
        if len(self.turn_direction) == 0:
            return
        direction = self.turn_direction.pop(0)
        self.head.setheading(self.head.heading() + direction)
