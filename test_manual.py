from models import Customer, FoodItem, Menu, Transaction

# Create some FoodItems
burger = FoodItem("Spicy Burger", 9.99, "Food", 4.5)
soda = FoodItem("Large Soda", 2.99, "Drinks", 4.0)

# Create a Menu and add items
menu = Menu()
menu.add_item(burger)
menu.add_item(soda)

# Filter by category
drinks = menu.filter_by_category("Drinks")
print("Drinks:", [item.name for item in drinks])

# Create a Transaction
txn = Transaction([burger, soda])
print("Transaction total:", txn.total_cost)

# Create a Customer
customer = Customer("Alice")
customer.add_transaction(txn)
print("Customer:", customer.name)
print("Total spent:", customer.total_spent)
