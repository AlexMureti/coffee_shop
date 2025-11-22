from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

c1.create_order(latte, 5.0)
c1.create_order(espresso, 3.5)
c2.create_order(latte, 6.0)

print("Customer coffees:", c1.coffees())
print("Coffee orders:", latte.num_orders())
print("Coffee average price:", latte.average_price())
print("Most aficionado of Latte:", Customer.most_aficionado(latte).name)
