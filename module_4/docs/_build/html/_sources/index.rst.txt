.. Pizza Ordering System documentation master file, created by
   sphinx-quickstart on Sat Jan 25 16:23:23 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pizza Ordering System's documentation!
==================================================

The Pizza Ordering System is a scalable and extensible application built with Python using Test-Driven Development (TDD) principles.

Features
--------

* **Pizza Customization**: Create pizzas with various crusts, sauces, cheese, and toppings
* **Order Management**: Add multiple pizzas to an order and track total cost
* **Payment Tracking**: Mark orders as paid/unpaid
* **Cost Calculation**: Automatic cost calculation based on ingredient pricing
* **Extensible Design**: Easy to add new ingredients and pricing structures

Quick Start
-----------

Creating a Pizza::

    from src.pizza import Pizza
    
    # Create a pizza with thin crust, marinara sauce, mozzarella cheese, and pepperoni
    pizza = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
    print(pizza)  # Pizza: thin crust, marinara sauce, mozzarella cheese, pepperoni toppings - $10

Creating an Order::

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

API Reference
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pizza
   order

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

