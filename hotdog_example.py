# Hot Dog Spot Simulation App

# Hot Dog Classes
class HotDog:
    def __init__(self, name):
        self.name = name
        self.condiments = []
        self.toppings = []

    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        return f"{self.name} with {', '.join(self.condiments + self.toppings)}"


class StandardHotDog(HotDog):
    def __init__(self, name):
        super().__init__(name)
        # predefined condiments and toppings for standard recipes


class CustomHotDog(HotDog):
    def __init__(self):
        super().__init__("Custom Hot Dog")


# Order Classes
class OrderItem:
    def __init__(self, hot_dog, quantity):
        self.hot_dog = hot_dog
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} x {self.hot_dog}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = sum(item.quantity for item in self.items)
        return total

    def apply_discount(self, discount_strategy):
        return discount_strategy.calculate_discount(self.get_total())

    def save_order(self):
        with open("orders.txt", "a") as file:
            for item in self.items:
                file.write(str(item) + "\n")


class DiscountStrategy:
    def calculate_discount(self, total):
        pass


class BulkDiscount(DiscountStrategy):
    def calculate_discount(self, total):
        if total >= 3:
            return total * 0.9
        return total


# Payment Classes
class Payment:
    def __init__(self, method):
        self.method = method

    def pay(self, amount):
        if self.method == "cash":
            print(f"Paid {amount} in cash.")
        elif self.method == "card":
            print(f"Paid {amount} by card.")


# Inventory Classes
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False

    def is_low(self):
        return self.quantity < 10


class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.ingredients = {}
        return cls._instance

    def add_ingredient(self, ingredient):
        self.ingredients[ingredient.name] = ingredient

    def use_ingredient(self, name, amount):
        if name in self.ingredients and self.ingredients[name].use(amount):
            if self.ingredients[name].is_low():
                self.notify_low_stock(name)
            return True
        return False

    def notify_low_stock(self, name):
        print(f"Ingredient {name} is running low!")

    def check_availability(self):
        for name, ingredient in self.ingredients.items():
            print(f"{name}: {ingredient.quantity}")


# Sales Classes
class SalesManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.sales = []
            cls._instance.returns = 0
        return cls._instance

    def add_sale(self, order):
        self.sales.append(order)

    def add_return(self, quantity):
        self.returns += quantity

    def calculate_profit(self):
        profit = sum(order.get_total() for order in self.sales)
        return profit

    def show_stats(self):
        print(f"Hot dogs sold: {len(self.sales)}")
        print(f"Returns: {self.returns}")
        print(f"Profit: {self.calculate_profit()}")


# Example Usage

# Create inventory and add ingredients
inventory = InventoryManager()
inventory.add_ingredient(Ingredient("Hot Dog Bun", 50))
inventory.add_ingredient(Ingredient("Sausage", 50))
inventory.add_ingredient(Ingredient("Mayonnaise", 20))
inventory.add_ingredient(Ingredient("Mustard", 20))
inventory.add_ingredient(Ingredient("Ketchup", 20))
inventory.add_ingredient(Ingredient("Sweet Onions", 15))
inventory.add_ingredient(Ingredient("Jalapenos", 15))
inventory.add_ingredient(Ingredient("Chile", 15))
inventory.add_ingredient(Ingredient("Pickles", 15))

# Create a custom hot dog
custom_hot_dog = CustomHotDog()
custom_hot_dog.add_condiment("Mayonnaise")
custom_hot_dog.add_topping("Jalapenos")

# Create an order and add items
order = Order()
order.add_item(OrderItem(custom_hot_dog, 3))

# Apply discount and save the order
discount = BulkDiscount()
total = order.apply_discount(discount)
order.save_order()

# Make payment
payment = Payment("card")
payment.pay(total)

# Update sales
sales_manager = SalesManager()
sales_manager.add_sale(order)
sales_manager.show_stats()

# Check inventory
inventory.check_availability()
