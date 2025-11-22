import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_customer_creation():
    c = Customer("Alice")
    assert c.name == "Alice"
    assert isinstance(c, Customer)

def test_customer_name_validation():
    with pytest.raises(Exception):
        Customer("")  # name too short
    with pytest.raises(Exception):
        Customer("A"*16)  # name too long
    with pytest.raises(Exception):
        Customer(123)  # not a string

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    order1 = customer.create_order(coffee1, 4.5)
    order2 = customer.create_order(coffee2, 5.0)

    assert order1 in customer.orders()
    assert order2 in customer.orders()
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_most_aficionado():
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    coffee = Coffee("Cappuccino")

    customer1.create_order(coffee, 5)
    customer1.create_order(coffee, 5)
    customer2.create_order(coffee, 6)

    top = Customer.most_aficionado(coffee)
    assert top == customer1
