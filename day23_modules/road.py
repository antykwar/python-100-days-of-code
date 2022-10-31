import random
import string

from day23_modules.car import Car


class Road:
    SEGMENT_SIZE = 20
    TRAFFIC_LINES = 8

    def __init__(self, screen, initial_speed, speed_multiplier):
        self.screen = screen

        self.initial_speed = initial_speed
        self.speed = self.initial_speed
        self.speed_multiplier = speed_multiplier

        self.cars = {}
        self._turtle_is_touched = False
        self.lines = self.generate_lines()

    def move_cars(self, turtle):
        for y_coord in self.lines:
            if random.random() > 0.02:
                continue
            new_key = self._generate_key()
            new_car = Car(self.screen)
            new_car.goto_start(y_coord)
            self.cars[new_key] = new_car

        cars_to_remove = []
        hit_key = None

        for key, car in self.cars.items():
            car.move_forward()

            if car.out_of_sight():
                car.stop()
                cars_to_remove.append(key)

            if car.hits(turtle):
                self._turtle_is_touched = True
                hit_key = key

        for key in cars_to_remove:
            del self.cars[key]

        if hit_key:
            self._clear_the_road(hit_key)

    def turtle_is_hit(self):
        return self._turtle_is_touched

    def generate_lines(self):
        min_y = int(-1 * (self.screen.window_height() / 2 - 4 * self.SEGMENT_SIZE))
        max_y = int(self.screen.window_height() / 2 - 2 * self.SEGMENT_SIZE)
        return list(range(min_y, max_y, int((max_y - min_y) / self.TRAFFIC_LINES)))

    def increase_speed(self):
        self.speed *= self.speed_multiplier

    def _clear_the_road(self, hit_key):
        for key, car in self.cars.items():
            if key == hit_key:
                continue
            car.stop()

    @staticmethod
    def _generate_key():
        return ''.join(random.choice(string.ascii_letters) for i in range(8))
