from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class FoodItem:
    """Represents a food item sold by ByteBites."""

    name: str
    price: float
    category: str
    popularity_rating: float = 0.0

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if not (0 <= self.popularity_rating <= 5):
            raise ValueError("Popularity rating must be between 0 and 5")


@dataclass
class Transaction:
    """A transaction groups together one or more FoodItems and can compute a total cost."""

    items: List[FoodItem] = field(default_factory=list)

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the transaction."""
        self.items.append(item)

    @property
    def total_cost(self) -> float:
        """Compute the total cost of all items in the transaction."""
        return sum(item.price for item in self.items)


@dataclass
class Customer:
    """Represents a customer with a name and purchase history."""

    name: str
    purchase_history: List[Transaction] = field(default_factory=list)

    def add_transaction(self, txn: Transaction) -> None:
        """Record a new transaction in the customer's history."""
        self.purchase_history.append(txn)

    @property
    def total_spent(self) -> float:
        """Compute the total amount spent across all transactions."""
        return sum(txn.total_cost for txn in self.purchase_history)


@dataclass
class Menu:
    """A menu holds a collection of FoodItems and allows filtering by category."""

    items: List[FoodItem] = field(default_factory=list)

    def add_item(self, item: FoodItem) -> None:
        """Add a new food item to the menu."""
        self.items.append(item)

    def remove_item(self, name: str) -> bool:
        """Remove an item by name. Returns True if removed, False if not found."""
        for i, item in enumerate(self.items):
            if item.name == name:
                del self.items[i]
                return True
        return False

    def filter_by_category(self, category: str) -> List[FoodItem]:
        """Return all items matching the given category."""
        return [item for item in self.items if item.category == category]
