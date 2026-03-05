import pytest

from bytebites.models import FoodItem, Menu, Transaction, Customer


def test_food_item_validation():
    # price negative should raise
    with pytest.raises(ValueError):
        FoodItem(name="Test", price=-1.0, category="Misc")
    # rating out of range
    with pytest.raises(ValueError):
        FoodItem(name="Test", price=1.0, category="Misc", popularity_rating=6)


def test_transaction_total():
    burger = FoodItem(name="Burger", price=5.0, category="Main")
    soda = FoodItem(name="Soda", price=2.5, category="Drinks")
    txn = Transaction(items=[burger])
    assert txn.total_cost == 5.0
    txn.add_item(soda)
    assert pytest.approx(txn.total_cost) == 7.5


def test_menu_operations():
    menu = Menu()
    burger = FoodItem(name="Burger", price=5.0, category="Main")
    soda = FoodItem(name="Soda", price=2.5, category="Drinks")
    menu.add_item(burger)
    menu.add_item(soda)
    assert burger in menu.items
    drinks = menu.filter_by_category("Drinks")
    assert drinks == [soda]
    assert menu.remove_item("Burger") is True
    assert burger not in menu.items
    assert menu.remove_item("Nonexistent") is False


def test_customer_history():
    cust = Customer(name="Alice")
    assert cust.total_spent == 0
    burger = FoodItem(name="Burger", price=5.0, category="Main")
    txn = Transaction(items=[burger])
    cust.add_transaction(txn)
    assert cust.purchase_history == [txn]
    assert cust.total_spent == 5.0
