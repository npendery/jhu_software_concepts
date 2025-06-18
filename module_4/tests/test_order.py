"""
Unit tests for Order class
"""

import pytest
from src.order import Order
from src.pizza import Pizza


class TestOrder:
    """Unit tests for Order class"""

    @pytest.mark.order
    def test_order_init(self):
        """Test order initialization"""
        order = Order()

        # Assert order should include an empty list of pizza objects
        assert not order.pizzas
        assert isinstance(order.pizzas, list)

        # Assert order should have a zero cost until an order is input
        assert order.cost == 0

        # Assert order should not have yet been paid
        assert order.paid is False

    @pytest.mark.order
    def test_order_str(self):
        """Test order string representation"""
        order = Order()
        pizza1 = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
        pizza2 = Pizza("thick", ["pesto"], "mozzarella", ["mushrooms"])

        order.input_pizza(pizza1)
        order.input_pizza(pizza2)

        order_str = str(order)

        # Test order should return a string containing customer full order and cost
        assert isinstance(order_str, str)
        assert str(order.cost) in order_str
        assert "pizza" in order_str.lower() or "order" in order_str.lower()

    @pytest.mark.order
    def test_order_input_pizza(self):
        """Test order input_pizza method"""
        order = Order()
        pizza1 = Pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
        pizza2 = Pizza("thick", ["pesto"], "mozzarella", ["mushrooms"])

        # Test method should update cost
        initial_cost = order.cost
        order.input_pizza(pizza1)
        assert order.cost > initial_cost
        assert order.cost == pizza1.cost()

        # Test adding another pizza
        cost_after_first = order.cost
        order.input_pizza(pizza2)
        assert order.cost > cost_after_first
        assert order.cost == pizza1.cost() + pizza2.cost()

    @pytest.mark.order
    def test_order_order_paid(self):
        """Test order payment method"""
        order = Order()

        # Test method should update paid to true
        assert order.paid is False
        order.order_paid()
        assert order.paid is True
