import unittest
from ShoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def test_initialization(self):
        cart = ShoppingCart("ABC12345XY-A")
        self.assertEqual(cart.customer_id, "ABC12345XY-A")
        self.assertEqual(cart.items, {})
        self.assertEqual(cart.total_cost, 0)

    def test_add_item(self):
        cart = ShoppingCart("ABC12345XY-A")
        cart.add_item("Apple", 3)
        self.assertEqual(cart.items, {"Apple": 3})
        self.assertEqual(cart.total_cost, 4.5)