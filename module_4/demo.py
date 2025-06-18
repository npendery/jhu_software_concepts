#!/usr/bin/env python3
"""
Demo script for the Pizza Ordering System

This script demonstrates the functionality with the example orders
mentioned in the assignment.
"""

from src.order import Order
from src.pizza import Pizza


def main():
    """
    Main function to demonstrate the pizza ordering system.
    """
    print("=== Pizza Ordering System Demo ===\n")

    # Order 1 from assignment
    print("Order 1:")
    order1 = Order()

    # Pizza(thin, pesto, mozzarella, mushrooms)
    pizza_1 = Pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])

    # Pizza(thick, marinara, mozzarella, mushrooms)
    pizza_2 = Pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])

    order1.input_pizza(pizza_1)
    order1.input_pizza(pizza_2)

    print(order1)
    print(f"\nOrder 1 Total: ${order1.cost}")
    print("-" * 50)

    # Order 2 from assignment
    print("\nOrder 2:")
    order2 = Order()

    # Pizza(gluten_free, marinara, mozzarella, pineapple)
    pizza_3 = Pizza("gluten_free", ["marinara"], "mozzarella", ["pineapple"])

    # Pizza(thin, liv_sauce, pesto, mozzarella, mushrooms, pepperoni)
    pizza_4 = Pizza(
        "thin", ["liv_sauce", "pesto"], "mozzarella", ["mushrooms", "pepperoni"]
    )

    order2.input_pizza(pizza_3)
    order2.input_pizza(pizza_4)

    print(order2)
    print(f"\nOrder 2 Total: ${order2.cost}")
    print("-" * 50)

    # Mark orders as paid
    order1.order_paid()
    order2.order_paid()

    print(f"\nOrder 1 Payment Status: {'Paid' if order1.paid else 'Unpaid'}")
    print(f"Order 2 Payment Status: {'Paid' if order2.paid else 'Unpaid'}")

    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
