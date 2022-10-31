from day16_modules.menuitem import MenuItem


class Menu:
    def __init__(self, items_data: list):
        self.items = {}
        self._load_items(items_data)

    def get_available_drinks(self):
        return [item for item in self.items.keys()]

    def is_enough_money(self, received_sum, drink_type):
        drink: MenuItem = self.items[drink_type]
        if drink.cost > received_sum:
            return False
        return True

    def get_item_price(self, drink_type):
        return self.items[drink_type].cost

    def get_item_ingredients(self, drink_type):
        return self.items[drink_type].get_ingredients_dict()

    def _load_items(self, items_data: list):
        for item in items_data:
            self._add_item(MenuItem(item))

    def _add_item(self, item: MenuItem):
        self.items.update({item.name: item})
