class Menu:
    def __init__(self, name, dishes, start_time, end_time):
        """
        This class represents a menu object, which contains a list of dishes available at certain times.

        name: str, name of the menu
        dishes: list, list of Dish objects available on the menu
        start_time: int, start time of the menu in hours (24-hour clock)
        end_time: int, end time of the menu in hours (24-hour clock)
        """
        self.name = name
        self.dishes = dishes
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time}:00 to {self.end_time}:00"


class Dish:
    def __init__(self, name, price, ingredients):
        """
        This class represents a dish object, which contains a name, price and list of ingredients.

        name: str, name of the dish
        price: float, price of the dish in dollars
        ingredients: list, list of str representing the ingredients used in the dish
        """
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})"
