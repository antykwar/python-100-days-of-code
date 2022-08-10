from replit import clear
from pyinputplus import inputYesNo, inputNum

from day9_modules.art import logo


print(logo)
bids = {}

while True:
    if len(bids):
        clear()

    name = input('What is your name? ')
    bid = inputNum('What is your price? ')

    bids[name] = bid

    if inputYesNo('Anyone else? ') != 'yes':
        break

maxBid = max(bids.items(), key=lambda pair: pair[1])
clear()

print(f'Winner is {maxBid[0]}, bid is {maxBid[1]}!')
