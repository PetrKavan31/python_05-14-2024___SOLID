from abc import ABC, abstractmethod


class HotDog(ABC):
    def __init__(self, recipe, toppings):
        self.recipe = recipe
        self.toppings = toppings

