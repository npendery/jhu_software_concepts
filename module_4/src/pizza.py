"""Pizza module for the pizza ordering system.

This module contains the Pizza class that represents a pizza with various
crusts, sauces, cheese, and toppings, along with cost calculation.
"""


class Pizza:
    """A pizza with crust, sauce, cheese, and toppings.

    Attributes:
        crust (str): The type of crust for the pizza
        sauce (list): List of sauces on the pizza
        cheese (str): The type of cheese on the pizza
        toppings (list): List of toppings on the pizza
    """

    # Pricing structure based on assignment requirements
    CRUST_PRICES = {"thin": 5, "thick": 5, "gluten_free": 6}

    SAUCE_PRICES = {"marinara": 2, "pesto": 4, "liv_sauce": 5}

    CHEESE_PRICES = {"mozzarella": 1}

    TOPPING_PRICES = {"pepperoni": 2, "mushrooms": 3, "pineapple": 3}

    def __init__(self, crust: str, sauce: list, cheese: str, toppings: list):
        """Initialize a pizza with the given ingredients.

        Args:
            crust (str): The type of crust
            sauce (list): List of sauce types
            cheese (str): The type of cheese
            toppings (list): List of topping types

        Raises:
            ValueError: If required ingredients are missing or invalid
        """
        if not crust or crust not in self.CRUST_PRICES:
            raise ValueError(f"Invalid crust: {crust}")

        if not sauce or not isinstance(sauce, list) or len(sauce) == 0:
            raise ValueError("Pizza must have at least one sauce")

        for s in sauce:
            if s not in self.SAUCE_PRICES:
                raise ValueError(f"Invalid sauce: {s}")

        if not cheese or cheese not in self.CHEESE_PRICES:
            raise ValueError(f"Invalid cheese: {cheese}")

        if not toppings or not isinstance(toppings, list) or len(toppings) == 0:
            raise ValueError("Pizza must have at least one topping")

        for t in toppings:
            if t not in self.TOPPING_PRICES:
                raise ValueError(f"Invalid topping: {t}")

        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self) -> str:
        """Return string representation of the pizza.

        Returns:
            str: A formatted string describing the pizza and its cost
        """
        sauce_str = ", ".join(self.sauce)
        toppings_str = ", ".join(self.toppings)

        return (
            f"Pizza: {self.crust} crust, {sauce_str} sauce, "
            f"{self.cheese} cheese, {toppings_str} toppings - ${self.cost()}"
        )

    def cost(self) -> int:
        """Calculate the total cost of the pizza.

        Returns:
            int: The total cost of the pizza in dollars
        """
        total_cost = 0

        # Add crust cost
        total_cost += self.CRUST_PRICES[self.crust]

        # Add sauce costs
        for sauce in self.sauce:
            total_cost += self.SAUCE_PRICES[sauce]

        # Add cheese cost
        total_cost += self.CHEESE_PRICES[self.cheese]

        # Add topping costs
        for topping in self.toppings:
            total_cost += self.TOPPING_PRICES[topping]

        return total_cost
