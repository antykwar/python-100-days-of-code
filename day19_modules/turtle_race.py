from random import randrange

from turtle import Turtle, Screen


class TurtleRace:
    COLORS = ['red', 'blue', 'yellow', 'black', 'magenta', 'palegreen', 'gold', 'chocolate', 'silver', 'darkgreen']
    WINDOW_BORDER_SHIFT = 40

    def __init__(self, screen: Screen):
        self.turtles = []
        self.screen = screen
        self.amount = None
        self.winner = None

    def init_turtles(self, amount):
        amount = int(amount)
        if not 2 <= amount <= 10:
            raise ValueError('Please specify amount between 2 and 10')

        self.amount = amount
        self.winner = None

        for order_number in range(self.amount):
            turtle = Turtle(shape='turtle')
            turtle.penup()
            turtle.color(self.COLORS[order_number])
            self.turtles.append(turtle)

        self.reset_positions()

    def reset_positions(self):
        if not self.amount:
            raise AttributeError('Amount of turtles is not set - missing init_turtles() call?')

        start_coordinates = self._generate_start_coordinates()

        for index, turtle in enumerate(self.turtles):
            turtle.goto(start_coordinates[index])

    def perform_race(self):
        winner_position = (self.screen.window_width() - self.WINDOW_BORDER_SHIFT) / 2
        while True:
            for turtle in self.turtles:
                turtle.forward(randrange(5, 15))
                if turtle.xcor() >= winner_position:
                    self.winner = turtle
                    return

    def announce_race_result(self, supposed_winner):
        self._prepare_screen_for_race_result()
        text = 'Victory!'
        if not self._is_winner(supposed_winner):
            text = f'Failure! Winner is {self.winner.fillcolor().lower()}!'
        self._write_label(text)

    def _prepare_screen_for_race_result(self):
        for turtle in self.turtles:
            turtle.hideturtle()
        self.winner.reset()
        self.winner.hideturtle()

    def _is_winner(self, supposed_winner: str):
        return supposed_winner.lower() == self.winner.fillcolor().lower()

    def _write_label(self, text):
        self.winner.write(text, align='center', font=('Arial', 32, 'normal'))

    def _generate_start_coordinates(self):
        initial_x = self._generate_start_line_shift()
        initial_y_list = self._generate_lines_coordinates()
        return [(initial_x, initial_y) for initial_y in initial_y_list]

    def _generate_start_line_shift(self):
        return -1 * (self.screen.window_width() - self.WINDOW_BORDER_SHIFT) / 2

    def _generate_lines_coordinates(self):
        initial_y_list = []
        strip_height = (self.screen.window_height() - self.WINDOW_BORDER_SHIFT) / self.amount

        side_selector = 1
        shift_number = 0
        add_shift_number = False
        is_amount_even = (self.amount % 2 == 0)

        for index in range(self.amount):
            current_shift_number = shift_number + 0.5 if is_amount_even else shift_number
            initial_y_list.append(current_shift_number * strip_height * side_selector)
            side_selector *= -1

            if not is_amount_even and index == 0:
                shift_number += 1
                continue

            if not add_shift_number:
                add_shift_number = True
                continue

            add_shift_number = False
            shift_number += 1

        return initial_y_list
