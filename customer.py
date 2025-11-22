from order import Order
from coffee import Coffee

class Customer:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string 1-15 characters")
        self._name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string 1-15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide a Coffee instance")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide a Coffee instance")
        orders_for_coffee = [order for order in Order.all if order.coffee == coffee]
        if not orders_for_coffee:
            return None
        spending = {}
        for order in orders_for_coffee:
            spending[order.customer] = spending.get(order.customer, 0) + order.price
        return max(spending, key=spending.get)
