from day16_modules.coffeemachine import CoffeeMachine
from day16_modules.moneyreceiver import MoneyReceiver
from day16_modules.menu import Menu
from day16_modules.data import MENU_ITEMS


menu = Menu(MENU_ITEMS)
money_receiver = MoneyReceiver()
machine = CoffeeMachine(money_receiver, menu)
machine.run()
