import  pytest
from coffee import Customer
from coffee import Coffee
from coffee import Order

def test_order_creation():
    customer = Customer("Sam")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 4.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.0

def test_order_price_validation():
    customer = Customer("Sam")
    coffee = Coffee("Latte")
    with pytest.raises(Exception):
        Order(customer, coffee, 0.5)  # too low
    with pytest.raises(Exception):
        Order(customer, coffee, 15)   # too high
    with pytest.raises(Exception):
        Order(customer, coffee, "5")  # not a float
