from pyinputplus import inputInt

from .menu import MENU
from .resources import RESOURCES


def actions_validation(value):
    available_coffee_types = tuple(sorted(MENU.keys()))
    available_service_actions = ('report', 'refill', 'off')
    if value.lower().strip() not in (available_coffee_types + available_service_actions):
        raise Exception(f'Please choose your coffee from list: {available_coffee_types}')


def get_initial_machine_state():
    state = RESOURCES.copy()
    state.update({'money': 0})
    return state


def refill_machine(current_state):
    current_state.update(RESOURCES)
    return current_state


def get_status_report(current_state):
    return f"""
    Water: {current_state['water']}ml
    Milk: {current_state['milk']}ml
    Coffee: {current_state['coffee']}g
    Money: ${current_state['money']:.2f}
    """


def receive_money_for_coffee():
    received_sum = 0
    coins = {25: 'quarters', 10: 'dimes', 5: 'nickles', 1: 'pennies'}
    for key, name in coins.items():
        received_sum += inputInt(f'How many {name}? ', min=1) * key
    return received_sum / 100


def get_drink_price(drink_type):
    return MENU[drink_type]['cost']


def get_drink_ingredients(drink_type):
    return MENU[drink_type]['ingredients']


def is_enough_money(received_sum, drink_type):
    if get_drink_price(drink_type) > received_sum:
        return False
    return True


def check_resources(current_state, drink_type):
    needed_resources = get_drink_ingredients(drink_type)
    enough_resources = True
    missing_resources = []
    for key, value in needed_resources.items():
        if value > current_state[key]:
            enough_resources = False
            missing_resources.append(key)

    return (True, None) if enough_resources else (False, ', '.join(missing_resources))


def get_charge(received_sum, drink_type):
    return received_sum - get_drink_price(drink_type)


def human_money_format(received_sum):
    return f'${received_sum:.2f}'


def prepare_coffee(current_state, drink_type):
    current_state['money'] += get_drink_price(drink_type)
    needed_resources = get_drink_ingredients(drink_type)
    for key, value in needed_resources.items():
        current_state[key] -= value
    return current_state


def serve_coffee(drink_type):
    return f'Here is your {drink_type}, enjoy!'
