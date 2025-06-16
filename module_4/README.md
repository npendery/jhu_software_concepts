# Pizza Ordering System

## Features

- **Pizza Customization**: Create pizzas with various crusts, sauces, cheese, and toppings
- **Order Management**: Add multiple pizzas to an order and track total cost
- **Payment Tracking**: Mark orders as paid/unpaid
- **Cost Calculation**: Automatic cost calculation based on ingredient pricing
- **Extensible Design**: Easy to add new ingredients and pricing structures

## Installation

1.  **Clone the repository.**
2.  **Navigate to the `module_4` directory:**
    ```bash
    cd module_4
    ```
3.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

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

