import pytest
from bytebites.models import Customer, FoodItem, Menu, Transaction

# Happy path tests
def test_transaction_total_with_multiple_items():
    burger = FoodItem(name="Spicy Burger", price=10.0, category="Food")
    soda = FoodItem(name="Large Soda", price=5.0, category="Drinks")
    txn = Transaction(items=[burger, soda])
    assert txn.total_cost == 15.0

# Edge case tests
def test_order_total_is_zero_when_empty():
    txn = Transaction()
    assert txn.total_cost == 0.0

def test_filter_by_category_returns_correct_items():
    menu = Menu()
    menu.add_item(FoodItem(name="Large Soda", price=2.99, category="Drinks"))
    menu.add_item(FoodItem(name="Spicy Burger", price=9.99, category="Food"))
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 1
    assert drinks[0].name == "Large Soda"

def test_customer_tracks_total_spent():
    customer = Customer(name="Alice")
    txn = Transaction(items=[FoodItem(name="Burger", price=10.0, category="Food")])
    customer.add_transaction(txn)
    assert customer.total_spent == 10.0
