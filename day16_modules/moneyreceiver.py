from pyinputplus import inputInt

from .outputformat import OutputFormat


class MoneyReceiver:
    def __init__(self):
        self.received_money = None
        self.total_money = 0

    def receive_money_for_drink(self):
        self.received_money = 0
        coins = {25: 'quarters', 10: 'dimes', 5: 'nickles', 1: 'pennies'}
        for key, name in coins.items():
            self.received_money += inputInt(f'How many {name}? ', min=1) * key
        self.received_money /= 100

    def get_total_money(self):
        return self.total_money

    def add_total_money(self, received_money):
        self.total_money += received_money

    def give_charge(self, item_price):
        if self.received_money > item_price:
            print(f'Your charge is {OutputFormat.money_format(self.received_money - item_price)}.')
