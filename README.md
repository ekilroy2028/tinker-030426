# ByteBites Backend

This repository contains the basic backend models for the ByteBites application.

## Structure

- `bytebites/models.py`: contains the `FoodItem`, `Menu`, `Transaction`, and `Customer` classes.
- `tests/test_models.py`: unit tests for the models using `pytest`.

## Getting Started

1. Ensure you have Python 3.10+ installed.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install `pytest` if you don't already have it:
   ```bash
   pip install pytest
   ```
4. Run the tests:
   ```bash
   pytest
   ```

## Example Usage

```python
from bytebites.models import FoodItem, Menu, Transaction, Customer

burger = FoodItem(name="Spicy Burger", price=8.99, category="Main", popularity_rating=4.5)
soda = FoodItem(name="Large Soda", price=2.49, category="Drinks")

menu = Menu()
menu.add_item(burger)
menu.add_item(soda)

txn = Transaction(items=[burger, soda])
print(txn.total_cost)  # 11.48

customer = Customer(name="Eve")
customer.add_transaction(txn)
print(customer.total_spent)
```
