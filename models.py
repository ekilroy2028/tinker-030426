# ByteBites Models
# Four core classes:
# - Customer: tracks name and purchase history
# - FoodItem: tracks name, price, category, and popularity rating
# - Menu: manages full collection of food items, filterable by category
# - Transaction: groups selected items and computes total cost

class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

class Transaction:
    def __init__(self, items: list[FoodItem]):
        self.items = items
        self.total_cost = self._calculate_total()

    def _calculate_total(self) -> float:
        return sum(item.price for item in self.items)

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Transaction] = []

    def add_transaction(self, txn: Transaction) -> None:
        self.purchase_history.append(txn)

    @property
    def total_spent(self) -> float:
        return sum(txn.total_cost for txn in self.purchase_history)

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        return [item for item in self.items if item.category == category]
