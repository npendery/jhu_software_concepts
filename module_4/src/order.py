"""Order module for the pizza ordering system.

This module contains the Order class that manages a collection of pizzas,
tracks the total cost, and handles payment status.
"""

from typing import List

from .pizza import Pizza


class Order:
    """An order containing one or more pizzas.

    Attributes:
        pizzas (List[Pizza]): List of pizzas in the order
        cost (int): Total cost of all pizzas in the order
        paid (bool): Whether the order has been paid for
    """

    def __init__(self):
        """Initialize an empty order.

        Creates an order with no pizzas, zero cost, and unpaid status.
        """
        self.pizzas: List[Pizza] = []
        self.cost: int = 0
        self.paid: bool = False

    def input_pizza(self, pizza: Pizza) -> None:
        """Add a pizza to the order and update the total cost.

        Args:
            pizza (Pizza): The pizza to add to the order
        """
        if not isinstance(pizza, Pizza):
            raise ValueError("Only Pizza objects can be added to an order")

        self.pizzas.append(pizza)
        self.cost += pizza.cost()

    def order_paid(self) -> None:
        """Mark the order as paid."""
        self.paid = True

    def __str__(self) -> str:
        """Return string representation of the order.

        Returns:
            str: A formatted string describing the complete order and total cost
        """
        if not self.pizzas:
            return f"Empty order - Total: ${self.cost}"

        order_lines = ["Customer Order:"]
        order_lines.append("-" * 40)

        for i, pizza in enumerate(self.pizzas, 1):
            order_lines.append(f"{i}. {pizza}")

        order_lines.append("-" * 40)
        order_lines.append(f"Total Cost: ${self.cost}")
        order_lines.append(f"Payment Status: {'Paid' if self.paid else 'Unpaid'}")

        return "\n".join(order_lines)
