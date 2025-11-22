from order import Order

class Coffee:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders_list = self.orders()
        if not orders_list:
            return 0
        return sum(order.price for order in orders_list) / len(orders_list)
