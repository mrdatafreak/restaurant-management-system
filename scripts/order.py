class Order:
    def __init__(self, customer, franchise, menu_name, order_time):
        """
        This class represents an order object, which contains a customer, franchise, menu, and order time.

        customer: Customer object, the customer placing the order
        franchise: Franchise object, the franchise where the order is placed
        menu_name: str, the name of the menu being ordered
        order_time: int, the time the order was placed (24-hour format)
        """
        self.customer = customer
        self.franchise = franchise
        self.menu = None
        for menu in franchise.menus:
            if menu.name == menu_name and menu.start_time <= order_time <= menu.end_time:
                self.menu = menu
                break
        self.dishes = []

    def add_dish(self, dish_name):
        """
        This method adds a Dish object to the order by name.

        dish_name: str, the name of the dish being added
        """
        for dish in self.menu.dishes:
            if dish.name == dish_name:
                self.dishes.append(dish)
                break

    def set_previous_order(self, previous_order):
        """
        This method sets a previous order for the current order.

        previous_order: Order object, the previous order to set
        """
        self.previous_order = previous_order

    def total_price(self):
        """
        This method returns the total price of the order by summing the prices of all the dishes in the order.
        """
        return sum(dish.price for dish in self.dishes)
