from errors import ItemError
from item import Item


class Bottled_Drink (Item):

    def __init__(self, Inventory, Ingredient_Costs, Name):
        
        if Name == "coke" or Name == "pepsi":
            if Inventory[Name] < 1:
                raise ItemError("This drink is out of stock.")
            else:
                super().__init__(Inventory, Ingredient_Costs)
                self._Name = Name
                Inventory[Name] -= 1
        else:
            raise ItemError("Invalid drink.")

        

    def __str__(self):
        
        return self._Name.capitalize()

    def Calculate_Cost(self):
        
        return self._Ingredient_Costs[self._Name]

    def Check_Ingredients (self):
        return True

    def Clear_Ingredients(self):
        
        self._Inventory[self._Name] += 1
