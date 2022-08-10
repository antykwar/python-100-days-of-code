from random import shuffle
from pyinputplus import inputCustom

from day14_modules import database, art, validation


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


def get_initial_sequence():
    sequence = database.data
    shuffle(sequence)
    return sequence


def fill_next_data(initial_sequence: list):
    try:
        return initial_sequence.pop()
    except IndexError:
        return None


def get_description_string(account: dict, variant: str):
    return f"Variant {variant}: {account['name']}, {account['description']}, {account['country']}"


@static_vars(score=0)
def compare_followers(account_a: dict, account_b: dict, user_selection: str):
    if user_selection == 'A' and account_a['follower_count'] >= account_b['follower_count']:
        compare_followers.score += 1
        return compare_followers.score, True
    elif user_selection == 'B' and account_a['follower_count'] < account_b['follower_count']:
        compare_followers.score += 1
        return compare_followers.score, True
    return compare_followers.score, False


print(art.logo)

accounts_list = get_initial_sequence()

account_a = fill_next_data(accounts_list)
account_b = fill_next_data(accounts_list)

if account_a is None or account_b is None:
    print('Not enough data!')
    quit()

while True:
    print(get_description_string(account_a, 'A'))
    print(art.vs)
    print(get_description_string(account_b, 'B'))

    user_selection = inputCustom(validation.variants, prompt='Choose who has more followers (A or B): ')

    score, success = compare_followers(account_a, account_b, user_selection)
    if not success:
        print(f'That is wrong. Your score is {score}.')
        quit()

    print(f'That is right. Your score is {score}.')
    account_a = account_b
    account_b = fill_next_data(accounts_list)

    if account_b is None:
        print('You passed all tests, congratulations!')
        quit()
