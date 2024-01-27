import uuid
import re

class ShoppingCart:
    def __init__(self, customer_id=None):
        if not re.match(r"^[a-zA-Z0-9 ]+$", customer_id) or len(customer_id) > 20:
            raise ValueError("Invalid customer ID")
        self._id = uuid.uuid4()
        self._customer_id = customer_id
        self._items = {}
        self._total_cost = 0

    def add_item(self, item_name, quantity):
        self._validate_item_name(item_name)
        self._validate_quantity(quantity)
        self._items[item_name] = quantity
        self._total_cost = sum(quantity * self._items.get(item_name, 0) for item_name in self._items)

    def update_item_quantity(self, item_name, quantity):
        self._validate_item_name(item_name)
        self._validate_quantity(quantity)
        if item_name in self._items:
            self._items[item_name] = quantity
        else:
            self._items[item_name] = 0
        self._total_cost = sum(quantity * self._items.get(item_name, 0) for item_name in self._items)

    @property
    def total_cost(self):
        return self._total_cost

    @property
    def items(self):
        return {item_name: item_quantity for item_name, item_quantity in self._items.items()}

    def recalculate_total_cost(self):
        self._total_cost = sum(self._items.values())

    def remove_item(self, item_name):
        if item_name in self._items:
            self._items.pop(item_name)
            self.recalculate_total_cost()

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__init__(customer_id)

    def _validate_item_name(self, item_name):
        if not re.match(r"^[a-zA-Z0-9 ]+$", item_name):
            raise ValueError("Invalid characters in item name.")
        if len(item_name) > 20:
            raise ValueError("Item name too long.")

    def _validate_quantity(self, quantity):
        if quantity < 1 or quantity > 100:
            raise ValueError("Quantity must be between 1 and 100.")