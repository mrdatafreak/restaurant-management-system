
from scripts.order import Order


class Customer:
    def __init__(self, first_name, last_name, email=None, last_order=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.last_order = last_order

    def __repr__(self):
        return self.name

    def full_name(self):
        return self.first_name + " " + self.last_name

    def order(self, franchise, menu_name, order_time):
        """
        This method takes in a franchise object, a menu name, and an order time and returns a new Order object.
        """
        for menu in franchise.menus:
            if menu.name == menu_name and menu.start_time <= order_time <= menu.end_time:
                new_order = Order(menu, self)
                if self.last_order is not None and self.last_order.franchise == franchise:
                    new_order.set_previous_order(self.last_order)
                self.last_order = new_order
                return new_order
        return None

    def repeat_last_order(self):
        """
        This method returns a new Order object that is a copy of the customer's last order.
        """
        if self.last_order is not None:
            new_order = Order(self.last_order.menu, self)
            new_order.set_previous_order(self.last_order)
            return new_order
        return None
