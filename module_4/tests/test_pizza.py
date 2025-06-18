"""
Unit tests for Pizza class
"""

import pytest
from src.pizza import Pizza


class TestPizza:
    """Unit tests for Pizza class"""

    @pytest.mark.pizza
    def test_pizza_init(self):
        """Test pizza initialization"""
        pizza = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])

        # Test pizza should return an initialized pizza
        assert pizza is not None

        # Test pizza should have
        # - crust (str)
        # - sauce (list of str)
        # - cheese (str)
        # - toppings (list of str)
        assert isinstance(pizza.crust, str)
        assert isinstance(pizza.sauce, list)
        assert all(isinstance(s, str) for s in pizza.sauce)
        assert isinstance(pizza.cheese, str)
        assert isinstance(pizza.toppings, list)
        assert all(isinstance(t, str) for t in pizza.toppings)

        # Test pizza should return a non-zero cost
        assert pizza.cost() > 0

    @pytest.mark.pizza
    def test_pizza_str(self):
        """Test pizza string representation"""
        pizza = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
        pizza_str = str(pizza)

        # Test pizza should return a string containing the pizza and cost
        assert isinstance(pizza_str, str)
        assert "thin" in pizza_str.lower()
        assert "marinara" in pizza_str.lower()
        assert "mozzarella" in pizza_str.lower()
        assert "pepperoni" in pizza_str.lower()
        assert str(pizza.cost()) in pizza_str

    @pytest.mark.pizza
    def test_pizza_cost(self):
        """Test pizza cost calculation"""
        # Test single sauce and topping
        pizza1 = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
        # Thin: $5, Marinara: $2, Mozzarella: $1, Pepperoni: $2 = $10
        assert pizza1.cost() == 10

        # Test multiple sauces and toppings
        pizza2 = Pizza(
            "thick", ["marinara", "pesto"], "mozzarella", ["pepperoni", "mushrooms"]
        )
        # Thick: $5, Marinara: $2, Pesto: $4, Mozzarella: $1, Pepperoni: $2, Mushrooms: $3 = $17
        assert pizza2.cost() == 17

        # Test gluten free crust
        pizza3 = Pizza("gluten_free", ["marinara"], "mozzarella", ["pineapple"])
        # Gluten Free: $6, Marinara: $2, Mozzarella: $1, Pineapple: $3 = $12
        assert pizza3.cost() == 12

        # Test liv sauce
        pizza4 = Pizza("thin", ["liv_sauce"], "mozzarella", ["mushrooms"])
        # Thin: $5, Liv Sauce: $5, Mozzarella: $1, Mushrooms: $3 = $14
        assert pizza4.cost() == 14
