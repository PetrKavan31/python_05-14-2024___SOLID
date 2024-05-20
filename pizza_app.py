from abc import ABC, abstractmethod
import json
'''ABC (Abstract Base Class):'''

# Base Pizza class
class Pizza(ABC):
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    def __str__(self):
        return f"{self.name} with {' and '.join(self.toppings)}"

    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)

# Pizza Factory using registration to avoid modifying the factory when adding new pizza types
class PizzaFactory:
    pizza_types = {}

    @staticmethod
    def register_pizza(pizza_type, constructor):
        PizzaFactory.pizza_types[pizza_type] = constructor

    @staticmethod
    def create_pizza(pizza_type, *args):
        constructor = PizzaFactory.pizza_types.get(pizza_type)
        if not constructor:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
        return constructor(*args)

# Payment strategies
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} by card.")

# Order handling
class Order:
    def __init__(self, payment_method, logger):
        self.pizzas = []
        self.payment_method = payment_method
        self.logger = logger

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def checkout(self):
        total_cost = len(self.pizzas) * 10  # Example cost calculation
        self.payment_method.pay(total_cost)
        for pizza in self.pizzas:
            print(pizza)
        self.logger.log(self.pizzas)

# Logger class
class Logger(ABC):
    @abstractmethod
    def log(self, data):
        pass

class FileLogger(Logger):
    def log(self, data):
        with open("orders.txt", "a") as file:
            for item in data:
                file.write(str(item) + "\n")

# Registering pizza types
PizzaFactory.register_pizza("margherita", lambda: Pizza("Margherita", ["tomato sauce", "mozzarella"]))
PizzaFactory.register_pizza("pepperoni", lambda: Pizza("Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"]))
PizzaFactory.register_pizza("hawaiian", lambda: Pizza("Hawaiian", ["tomato sauce", "mozzarella", "pineapple", "ham"]))
PizzaFactory.register_pizza("vegan", lambda: Pizza("Vegan", ["tomato sauce", "vegan cheese"]))
PizzaFactory.register_pizza("custom", lambda toppings: Pizza("Custom", toppings))

# Example usage
payment_method = CardPayment()
logger = FileLogger()
order = Order(payment_method, logger)
order.add_pizza(PizzaFactory.create_pizza("margherita"))
order.add_pizza(PizzaFactory.create_pizza("custom", ["onion", "bell peppers"]))
order.checkout()
