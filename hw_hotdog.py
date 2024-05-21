from abc import ABC, abstractmethod
import json
'''ABC (Abstract Base Class):'''


# Base Hotdog class
class Hotdog(ABC):
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    def __str__(self):
        return f"{self.name} hotdog - {' and '.join(self.toppings)}"

    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)


# Hotdog Factory using registration to avoid modifying the factory when adding new hotdog types
class HotdogFactory:
    hotdog_types = {}

    @staticmethod
    def register_hotdog(hotdog_type, constructor):
        HotdogFactory.hotdog_types[hotdog_type] = constructor

    @staticmethod
    def create_hotdog(hotdog_type, *args):
        constructor = HotdogFactory.hotdog_types.get(hotdog_type)
        if not constructor:
            raise ValueError(f"Unknown hotdog type: {hotdog_type}")
        return constructor(*args)


# Stock of ingredients for making hot dogs
class Stock:
    ingredients = {}

    @staticmethod
    def register_ingredient(ingredient, constructor_stock):
        Stock.ingredients[ingredient] = constructor_stock

    @staticmethod
    def get_ingredient


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
        self.hotdogs = []
        self.payment_method = payment_method
        self.logger = logger

    def add_hotdog(self, hotdog):
        self.hotdogs.append(hotdog)

    def checkout(self):
        total_cost = 0
        for i in range(len(self.hotdogs)):
            if (i + 1) % 4 != 0:  # every fourth hotdog is free
                total_cost += 3.99

        # total_cost = len(self.hotdogs) * 3.99  # Example cost calculation
        # if len(self.hotdogs) >= 3:
            # total_cost *= 0.9  # apply 10% discount

        self.payment_method.pay(total_cost)
        for hotdog in self.hotdogs:
            print(hotdog)
        self.logger.log(self.hotdogs)


# Logger class
class Logger(ABC):
    @abstractmethod
    def log(self, data):
        pass


class FileLogger(Logger):
    def log(self, data):
        with open("orders_hds.txt", "a") as file:
            for item in data:
                file.write(str(item) + "\n")


# Registering hotdog types
HotdogFactory.register_hotdog("normal", lambda: Hotdog("Normal", ["bun", "sausage", "onion"]))
HotdogFactory.register_hotdog("cheese", lambda: Hotdog("Cheese", ["bun", "sausage", "cheese"]))
HotdogFactory.register_hotdog("spicy", lambda: Hotdog("Spicy", ["bun", "sausage", "jalapenos"]))
HotdogFactory.register_hotdog("custom", lambda toppings: Hotdog("Custom", toppings))

# Example usage
payment_method = CashPayment()
logger = FileLogger()
order = Order(payment_method, logger)
order.add_hotdog(HotdogFactory.create_hotdog("normal"))
order.add_hotdog(HotdogFactory.create_hotdog("normal"))
order.add_hotdog(HotdogFactory.create_hotdog("cheese"))
order.add_hotdog(HotdogFactory.create_hotdog("cheese"))
order.add_hotdog(HotdogFactory.create_hotdog("custom", ["bun", "sausage", "mayo", "bacon"]))
order.checkout()
