# Pizza Ordering System

A scalable and extensible pizza ordering application built with Python using Test-Driven Development (TDD) principles.

## Features

- **Pizza Customization**: Create pizzas with various crusts, sauces, cheese, and toppings
- **Order Management**: Add multiple pizzas to an order and track total cost
- **Payment Tracking**: Mark orders as paid/unpaid
- **Cost Calculation**: Automatic cost calculation based on ingredient pricing
- **Extensible Design**: Easy to add new ingredients and pricing structures

## Installation

1. Clone the repository
2. Navigate to the module_4 directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Creating a Pizza

```python
from src.pizza import Pizza

# Create a pizza with thin crust, marinara sauce, mozzarella cheese, and pepperoni
pizza = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
print(pizza)  # Pizza: thin crust, marinara sauce, mozzarella cheese, pepperoni toppings - $10
print(f"Cost: ${pizza.cost()}")  # Cost: $10
```

### Creating an Order

```python
from src.order import Order
from src.pizza import Pizza

# Create an order
order = Order()

# Add pizzas to the order
pizza1 = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
pizza2 = Pizza("thick", ["pesto"], "mozzarella", ["mushrooms"])

order.input_pizza(pizza1)
order.input_pizza(pizza2)

print(f"Total cost: ${order.cost}")  # Total cost: $23
print(order)  # Displays full order details

# Mark as paid
order.order_paid()
```

## Pricing Structure

### Crusts
- Thin: $5
- Thick: $5
- Gluten Free: $6

### Sauces
- Marinara: $2
- Pesto: $4
- Liv Sauce: $5

### Cheese
- Mozzarella: $1

### Toppings
- Pepperoni: $2
- Mushrooms: $3
- Pineapple: $3

## Running Tests

Run all tests:
```bash
python -m pytest tests/ -v
```

Run only pizza tests:
```bash
python -m pytest tests/ -m "pizza" -v
```

Run only order tests:
```bash
python -m pytest tests/ -m "order" -v
```

## Project Structure

```
module_4/
├── src/
│   ├── __init__.py
│   ├── pizza.py          # Pizza class implementation
│   └── order.py          # Order class implementation
├── tests/
│   ├── __init__.py
│   ├── test_pizza.py     # Pizza unit tests
│   ├── test_order.py     # Order unit tests
│   └── test_integration.py  # Integration tests
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Development

This project follows Test-Driven Development (TDD) principles:

1. Tests were written first to define the requirements
2. Code was implemented to make tests pass
3. Code was refactored while maintaining test coverage

### Test Coverage

The test suite includes:
- **Unit Tests**: Testing individual components (Pizza and Order classes)
- **Integration Tests**: Testing the interaction between components
- **Test Markers**: Custom pytest markers for organizing tests by functionality

## Requirements

- Python 3.10+
- pytest >= 7.0.0
- sphinx >= 5.0.0 (for documentation)
- sphinx-rtd-theme >= 1.0.0 (for documentation theme)

## Documentation

Full API documentation is generated using Sphinx and available on Read the Docs.

## Contributing

When contributing to this project:

1. Follow TDD principles - write tests first
2. Ensure all tests pass before submitting changes
3. Use appropriate test markers (`@pytest.mark.pizza` or `@pytest.mark.order`)
4. Update documentation as needed

## License

This project is part of JHU EP 605.256 – Modern Software Concepts in Python coursework. 
