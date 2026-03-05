# ByteBites UML Design

classDiagram
    class FoodItem {
        - name: str
        - price: float
        - category: str
        - popularity_rating: float
    }
    class Transaction {
        - items: List~FoodItem~
        + add_item(item: FoodItem)
        + total_cost: float
    }
    class Customer {
        - name: str
        - purchase_history: List~Transaction~
        + add_transaction(txn: Transaction)
        + total_spent: float
    }
    class Menu {
        - items: List~FoodItem~
        + add_item(item: FoodItem)
        + remove_item(name: str): bool
        + filter_by_category(category: str): List~FoodItem~
    }
    Transaction "1" --> "*" FoodItem : contains
    Customer "1" --> "*" Transaction : has
    Menu "1" --> "*" FoodItem : manages
