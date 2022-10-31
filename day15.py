from pyinputplus import inputCustom

from day15_modules.logic import *


machine_state = get_initial_machine_state()

while True:
    user_selection = inputCustom(actions_validation, prompt='Hello! What would you like? ')

    if user_selection == 'off':
        print('Bye-bye!')
        quit()

    if user_selection in ('report', 'refill'):
        if user_selection == 'refill':
            machine_state = refill_machine(machine_state)
        print(get_status_report(machine_state))
        continue

    print('Please, insert coins:')
    money_for_coffee = receive_money_for_coffee()

    if not is_enough_money(money_for_coffee, user_selection):
        print(f'You paid {human_money_format(money_for_coffee)}, '
              f'but it costs {human_money_format(get_drink_price(user_selection))}, refund.')
        continue

    has_enough_resources, message = check_resources(machine_state, user_selection)

    if not has_enough_resources:
        print(f'Not enough resources, missing {message}, refund.')
        continue

    charge = get_charge(money_for_coffee, user_selection)
    if charge > 0:
        print(f'Your charge is {human_money_format(charge)}.')

    machine_state = prepare_coffee(machine_state, user_selection)
    print(serve_coffee(user_selection))
