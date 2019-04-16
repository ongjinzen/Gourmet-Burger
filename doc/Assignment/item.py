from abc import ABC, abstractmethod


class Item (ABC):

    def __init__(self, Inventory, Ingredient_Costs):
        self._Inventory = Inventory
        self._Ingredient_Costs = Ingredient_Costs

    # Calculates the cost of the item.
    @abstractmethod
    def Calculate_Cost(self):
        pass

    # Checks that the item's options are valid.
    @abstractmethod
    def Check_Ingredients(self):
        pass

    # Removes all ingredients from an item and restores the inventory.
    @abstractmethod
    def Clear_Ingredients(self):
        pass