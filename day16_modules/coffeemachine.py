from pyinputplus import inputCustom

from .moneyreceiver import MoneyReceiver
from .menu import Menu
from .data import COFFEE_MACHINE_FULL_STATE
from .outputformat import OutputFormat


class CoffeeMachine:
    def __init__(self, receiver: MoneyReceiver, menu: Menu):
        self.receiver = receiver
        self.menu = menu
        self.state = None
        self.user_selection = None
        self.refill_machine()

    def refill_machine(self):
        if self.state is None:
            self.state = COFFEE_MACHINE_FULL_STATE.copy()
            return
        self.state.update(COFFEE_MACHINE_FULL_STATE)

    def get_status_report(self):
        return f"""
        Water: {self.state['water']}ml
        Milk: {self.state['milk']}ml
        Coffee: {self.state['coffee']}g
        Money: {OutputFormat.money_format(self.receiver.get_total_money())}
        """

    def _get_user_selection(self):
        return inputCustom(self._validate_user_selection, prompt='Hello! What would you like? ')

    def _validate_user_selection(self, value):
        available_drink_types = tuple(sorted(self.menu.get_available_drinks()))
        available_service_actions = ('report', 'refill', 'off')
        if value.lower().strip() not in (available_drink_types + available_service_actions):
            raise Exception(f'Please choose your drink from list: {available_drink_types}')

    def check_resources(self):
        needed_resources = self.menu.get_item_ingredients(self.user_selection)
        enough_resources = True
        missing_resources = []
        for key, value in needed_resources.items():
            if value > self.state[key]:
                enough_resources = False
                missing_resources.append(key)
        return (True, None) if enough_resources else (False, ', '.join(missing_resources))

    def prepare_drink(self):
        self.receiver.add_total_money(self.menu.get_item_price(self.user_selection))
        needed_resources = self.menu.get_item_ingredients(self.user_selection)
        for key, value in needed_resources.items():
            self.state[key] -= value

    def serve_drink(self):
        return f'Here is your {self.user_selection}, enjoy!'

    def run(self):
        while True:
            self.user_selection = self._get_user_selection()

            if self.user_selection == 'off':
                print('Bye-bye!')
                break

            if self.user_selection in ('report', 'refill'):
                if self.user_selection == 'refill':
                    self.refill_machine()
                print(self.get_status_report())
                continue

            print('Please, insert coins:')
            self.receiver.receive_money_for_drink()

            if not self.menu.is_enough_money(self.receiver.received_money, self.user_selection):
                print(
                    f'You paid {OutputFormat.money_format(self.receiver.received_money)}, '
                    f'but it costs {OutputFormat.money_format(self.menu.get_item_price(self.user_selection))}, '
                    f'refund.'
                )
                continue

            has_enough_resources, message = self.check_resources()

            if not has_enough_resources:
                print(f'Not enough resources, missing {message}, refund.')
                continue

            self.receiver.give_charge(self.menu.get_item_price(self.user_selection))

            self.prepare_drink()
            print(self.serve_drink())
