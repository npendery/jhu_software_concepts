#!/usr/bin/env python3
"""
Demo script for the Pizza Ordering System

This script demonstrates the functionality with the example orders
mentioned in the assignment.
"""

from src.order import Order
from src.pizza import Pizza


def main():
    print("=== Pizza Ordering System Demo ===\n")

    # Order 1 from assignment
    print("Order 1:")
    order1 = Order()

    # Pizza(thin, pesto, mozzarella, mushrooms)
    pizza1_1 = Pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])

    # Pizza(thick, marinara, mozzarella, mushrooms)
    pizza1_2 = Pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])

    order1.input_pizza(pizza1_1)
    order1.input_pizza(pizza1_2)

    print(order1)
    print(f"\nOrder 1 Total: ${order1.cost}")
    print("-" * 50)

    # Order 2 from assignment
    print("\nOrder 2:")
    order2 = Order()

    # Pizza(gluten_free, marinara, mozzarella, pineapple)
    pizza2_1 = Pizza("gluten_free", ["marinara"], "mozzarella", ["pineapple"])

    # Pizza(thin, liv_sauce, pesto, mozzarella, mushrooms, pepperoni)
    pizza2_2 = Pizza(
        "thin", ["liv_sauce", "pesto"], "mozzarella", ["mushrooms", "pepperoni"]
    )

    order2.input_pizza(pizza2_1)
    order2.input_pizza(pizza2_2)

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
