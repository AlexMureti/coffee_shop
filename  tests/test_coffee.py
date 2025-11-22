import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_coffee_creation():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

def test_coffee_name_validation():
    with pytest.raises(Exception):
        Coffee("")  # too short
    with pytest.raises(Exception):
        Coffee("AB")  # too short

def test_coffee_orders_and_customers():
    customer = Customer("Alice")
    coffee = Coffee("Flat White")
    order = customer.create_order(coffee, 3.5)

    assert order in coffee.orders()
    assert customer in coffee.customers()

def test_coffee_num_orders_and_average_price():
    customer1 = Customer("Tom")
    customer2 = Customer("Jerry")
    coffee = Coffee("Americano")

    customer1.create_order(coffee, 3)
    customer2.create_order(coffee, 5)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0
