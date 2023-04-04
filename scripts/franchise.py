class Franchise:
    """
    This class represents a franchise location of the restaurant chain. Each franchise has an address and a list of menus
    that it offers.
    """

    def __init__(self, address, menus):
        """
        Initializes a new instance of the Franchise class with the given address and list of menus.
        """
        self.address = address
        self.menus = menus

    def __repr__(self):
        """
        Returns a string representation of the Franchise object.
        """
        return f"Franchise at {self.address}"

    def available_menus(self, time):
        """
        This method takes in a time (in hours) and returns a list of menu objects that are available at that time.
        """
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu)
        return available_menus
