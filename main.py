from scripts.business import Business
from scripts.franchise import Franchise
from scripts.menu import Menu
from scripts.order import Order
from scripts.customer import Customer
from scripts.employee import Employee


# create menu items for franchises
menus = [Menu("Brunch", ["pancakes", "waffles", "eggs"], 1100, 1600),
         Menu("Early Bird", ["salumeria pizza",
              "garlic bread", "salad"], 1500, 1800),
         Menu("Dinner", ["pizza", "pasta", "salad", "steak"], 1700, 2300),
         Menu("Kids", ["chicken nuggets", "fries", "apple juice"], 1100, 2100)]


# create franchises
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)


# create the business

my_business = Business("Basta Fazoolin' with my Heart",
                       "123-456-7890", "info@basta.com", [flagship_store, new_installment])


manager = Employee("Jane", "Doe", "Manager",
                   "janedoe@gmail.com", 25, "General Manager")
server = Employee("John", "Doe", "Server",
                  "johndoe@gmail.com", 15, "Head Server")
chef = Employee("Jack", "Smith", "Chef",
                "jacksmith@gmail.com", 20, "Head Chef")

print("\nOur employees:")
for employee in [manager, server, chef]:
    print(employee.full_name() + " - " + employee.job_title)


# create customers
customer1 = Customer("John", "Smith", "johnsmith@gmail.com")
customer2 = Customer("Alice", "Johnson", "alicejohnson@gmail.com")


# create orders
order1 = Order(customer1, flagship_store, "Early Bird", 1530)
order2 = Order(customer2, new_installment, "Dinner", 2000)


# print details
print("Welcome to " + my_business.name)
print("We have " + str(len(my_business.franchises)) + " locations:")
for franchise in my_business.franchises:
    print(franchise)

print("\nOur employees:")
for employee in [manager, server, chef]:
    print(employee.full_name() + " - " + employee.job_title)

print("\nCustomers who placed an order with us today:")
for customer in [customer1, customer2]:
    print(customer.full_name() + " - " + customer.email)

print("\nOrders placed today:")
for order in [order1, order2]:
    print(order)

print("\nAvailable menus at " + flagship_store.address + " at 11am:")
for menu in flagship_store.available_menus(1100):
    print(menu)

print("\nAvailable menus at " + new_installment.address + " at 6pm:")
for menu in new_installment.available_menus(1800):
    print(menu)
