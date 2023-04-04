class Business:
    def __init__(self, name, address, phone_number, email):
        """
        Initialize a new business with the given name, address, phone number, and email.

        Args:
            name (str): The name of the business.
            address (str): The address of the business.
            phone_number (str): The phone number of the business.
            email (str): The email address of the business.
        """
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.franchises = []

    def add_franchise(self, franchise):
        """
        Add a franchise to the list of franchises for this business.

        Args:
            franchise (Franchise): The franchise to add.
        """
        self.franchises.append(franchise)

    def remove_franchise(self, franchise):
        """
        Remove a franchise from the list of franchises for this business.

        Args:
            franchise (Franchise): The franchise to remove.
        """
        self.franchises.remove(franchise)

    def get_franchises(self):
        """
        Get a list of all franchises for this business.

        Returns:
            list: A list of all franchises for this business.
        """
        return self.franchises
