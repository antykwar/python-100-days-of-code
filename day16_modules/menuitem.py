from day16_modules.ingredient import Ingredient


class MenuItem:
    def __init__(self, params: dict):
        self.ingredients = []
        self.name = params['name']
        self.parse_ingredients(params['ingredients'])
        self.cost = params['cost']
        pass

    def parse_ingredients(self, ingredients: dict):
        for name, amount in ingredients.items():
            self.ingredients.append(Ingredient(name, amount))

    def get_ingredients_dict(self):
        ingredients = {}
        for ingredient in self.ingredients:
            ingredients.update(ingredient.to_dict())
        return ingredients
