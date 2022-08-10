import random
from day11_modules import art
from replit import clear


def initial_cards():
    cards = []
    for _ in range(2):
        cards = add_card(cards)
    return cards


def add_card(hand: list):
    blackjack_deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    hand.append(random.choice(blackjack_deck))
    return hand


def sum_cards(cards: list):
    special_weights = {'A': 11, 'J': 10, 'Q': 10, 'K': 10}
    total_sum = 0
    for card in cards:
        if card not in special_weights.keys():
            total_sum += card
            continue
        if card != 'A':
            total_sum += special_weights[card]
            continue
        if (total_sum + special_weights[card]) > 21:
            total_sum += 1
            continue
        total_sum += special_weights[card]
    return total_sum


def is_blackjack(cards):
    return sum_cards(cards) == 21 and len(cards) == 2


def clear_interface():
    clear()
    print(art.logo)


def message_function(player_hand, computer_hand, result):
    print(f'{result}')
    print(f'Your cards: {player_hand}, current score: {sum_cards(player_hand)}')
    print(f'Computer cards: {computer_hand}, current score: {sum_cards(computer_hand)}')


def analyze_result(player_deck, computer_deck):
    player_sum = sum_cards(player_deck)
    computer_sum = sum_cards(computer_deck)

    if player_sum > 21:
        message_function(player_deck, computer_deck, 'You loose!')
        return

    if computer_sum > 21:
        message_function(player_deck, computer_deck, 'You win!')
        return

    if player_sum < computer_sum:
        message_function(player_deck, computer_deck, 'You loose!')
        return
    elif player_sum > computer_sum:
        message_function(player_deck, computer_deck, 'You win!')
        return

    message_function(player_deck, computer_deck, 'It`s a draw!')


while True:
    if input('Wanna play? ').lower() != 'y':
        break

    clear_interface()

    player_cards = initial_cards()
    computer_cards = initial_cards()
    end_current_game = False

    if is_blackjack(player_cards) or is_blackjack(computer_cards):
        analyze_result(player_cards, computer_cards)
        continue

    while True:
        print(f'Your cards: {player_cards}, current score: {sum_cards(player_cards)}')
        print(f'Computer\'s first card: {computer_cards[0]}')

        action = input("Type 'y' to take another card, 'n' to pass: ")
        if action != 'y':
            break

        player_cards = add_card(player_cards)
        if sum_cards(player_cards) > 21:
            message_function(player_cards, computer_cards, 'You lost!')
            end_current_game = True
            break

    if end_current_game:
        continue

    if sum_cards(computer_cards) < 17:
        while sum_cards(computer_cards) < 21:
            computer_cards = add_card(computer_cards)

    analyze_result(player_cards, computer_cards)
