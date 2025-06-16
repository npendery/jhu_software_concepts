import pytest
from src.order import Order
from src.pizza import Pizza


class TestIntegration:
    """Integration tests for Pizza Ordering System"""

    @pytest.mark.order
    @pytest.mark.pizza
    def test_multiple_pizza_objects_per_order(self):
        """Test that code can handle multiple pizza objects per order"""
        order = Order()

        # Create multiple pizzas
        pizza1 = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
        pizza2 = Pizza("thick", ["pesto"], "mozzarella", ["mushrooms"])
        pizza3 = Pizza("gluten_free", ["liv_sauce"], "mozzarella", ["pineapple"])

        # Add pizzas to order
        order.input_pizza(pizza1)
        order.input_pizza(pizza2)
        order.input_pizza(pizza3)

        # Ensure multiple pizza objects within a given order result in an additively larger cost
        expected_cost = pizza1.cost() + pizza2.cost() + pizza3.cost()
        assert order.cost == expected_cost

        # Verify all pizzas are in the order
        assert len(order.pizzas) == 3
        assert pizza1 in order.pizzas
        assert pizza2 in order.pizzas
        assert pizza3 in order.pizzas

    @pytest.mark.order
    @pytest.mark.pizza
    def test_assignment_example_orders(self):
        """Test the specific orders mentioned in the assignment"""
        # Order 1: Pizza(thin, pesto, mozzarella, mushrooms) + Pizza(thick, marinara, mozzarella, mushrooms)
        order1 = Order()
        pizza1_1 = Pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
        pizza1_2 = Pizza("thick", ["marinara"], "mozzarella", ["mushrooms"])

        order1.input_pizza(pizza1_1)
        order1.input_pizza(pizza1_2)

        # Thin: $5, Pesto: $4, Mozzarella: $1, Mushrooms: $3 = $13
        # Thick: $5, Marinara: $2, Mozzarella: $1, Mushrooms: $3 = $11
        # Total: $24
        assert order1.cost == 24

        # Order 2: Pizza(gluten_free, marinara, mozzarella, pineapple) + Pizza(thin, liv_sauce, pesto, mozzarella, mushrooms, pepperoni)
        order2 = Order()
        pizza2_1 = Pizza("gluten_free", ["marinara"], "mozzarella", ["pineapple"])
        pizza2_2 = Pizza(
            "thin", ["liv_sauce", "pesto"], "mozzarella", ["mushrooms", "pepperoni"]
        )

        order2.input_pizza(pizza2_1)
        order2.input_pizza(pizza2_2)

        # Gluten Free: $6, Marinara: $2, Mozzarella: $1, Pineapple: $3 = $12
        # Thin: $5, Liv Sauce: $5, Pesto: $4, Mozzarella: $1, Mushrooms: $3, Pepperoni: $2 = $20
        # Total: $32
        assert order2.cost == 32
