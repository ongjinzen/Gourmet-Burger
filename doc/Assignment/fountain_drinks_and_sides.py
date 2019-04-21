from errors import ItemError
from item import Item


class Fountain_Drinks_and_Sides (Item):

    def __init__(self, Inventory, Ingredient_Costs, Name,):
        
        if Name in ["apple juice", "orange juice", "fries", "nuggets", "chocolate sundae", "strawberry sundae"]:
            self._Name = Name
            self._Size = None
            self._Inventory = Inventory
            self._Ingredient_Costs = Ingredient_Costs
        else:
            raise ItemError("Invalid item.")

    def __str__(self):
        
        if self._Size == None:
            return f'{self._Name.capitalize()}'
        else:
            return f'{self._Size.capitalize()} {self._Name.capitalize()}'

    def Calculate_Cost(self):

        cost = 0
        if self._Name == "apple juice":
            if self._Size == "small":
                cost = 2.5
            elif self._Size == "medium":
                cost = 3.5
            elif self._Size == "large":
                cost = 4
        elif self._Name == "orange juice":
            if self._Size == "small":
                cost = 2
            elif self._Size == "medium":
                cost = 3
            elif self._Size == "large":
                cost = 3.5
        elif self._Name == "fries":
            if self._Size == "small":
                cost = 2
            elif self._Size == "medium":
                cost = 3
            elif self._Size == "large":
                cost = 3.5
        elif self._Name == "nuggets":
            if self._Size == "small":
                cost = 4
            elif self._Size == "medium":
                cost = 7
            elif self._Size == "large":
                cost = 10
        elif self._Name in ["chocolate sundae", "strawberry sundae"]:
            if self._Size == "small":
                cost = 4
            elif self._Size == "medium":
                cost = 6
            elif self._Size == "large":
                cost = 11

        return cost

    def Check_Ingredients (self):

        if not (self._Name in ["apple juice", "orange juice", "fries", "nuggets", "chocolate sundae", "strawberry sundae"]):
            raise ItemError("Invalid item.")
        elif not (self._Size in ["small", "medium", "large"]):
            raise ItemError("Invalid size.")

        return True

    def Clear_Ingredients(self):
        
        if self._Name in ["apple juice", "orange juice"]:
            if self._Size == "small":
                self._Inventory[self._Name] += 250
            if self._Size == "medium":
                self._Inventory[self._Name] += 500
            if self._Size == "large":
                    self._Inventory[self._Name] += 750
        elif self._Name in ["fries", "chocolate sundae", "strawberry sundae"]:
            if self._Size == "small":
                self._Inventory[self._Name] += 200
            if self._Size == "medium":
                self._Inventory[self._Name] += 400
            if self._Size == "large":
                self._Inventory[self._Name] += 600
        elif self._Name == "nuggets":
            if self._Size == "small":
                self._Inventory[self._Name] += 4
            if self._Size == "medium":
                self._Inventory[self._Name] += 8
            if self._Size == "large":
                self._Inventory[self._Name] += 12

    @property
    def Size(self):
        return self._Size

    # Choose the size of the item
    @Size.setter
    def Size(self, Size):

        if self._Size in ["small", "medium", "large"] and self._Size != Size:
            if self._Name in ["apple juice", "orange juice"]:
                if self._Size == "small":
                    self._Inventory[self._Name] += 250
                if self._Size == "medium":
                    self._Inventory[self._Name] += 500
                if self._Size == "large":
                    self._Inventory[self._Name] += 750
            elif self._Name in ["fries", "chocolate sundae", "strawberry sundae"]:
                if self._Size == "small":
                    self._Inventory[self._Name] += 200
                if self._Size == "medium":
                    self._Inventory[self._Name] += 400
                if self._Size == "large":
                    self._Inventory[self._Name] += 600
            elif self._Name == "nuggets":
                if self._Size == "small":
                    self._Inventory[self._Name] += 4
                if self._Size == "medium":
                    self._Inventory[self._Name] += 8
                if self._Size == "large":
                    self._Inventory[self._Name] += 12
        if self._Name == "apple juice" or self._Name == "orange juice":
            if Size == "small":
                if self._Inventory[self._Name] < 250:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 250
                    self._Size = Size
            elif Size == "medium":
                if self._Inventory[self._Name] < 500:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 500
                    self._Size = Size
            elif Size == "large":
                if self._Inventory[self._Name] < 750:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 750
                    self._Size = Size
            else:
                raise ItemError("Invalid size.")

        elif self._Name in ["fries","chocolate sundae", "strawberry sundae"]:
            if Size == "small":
                if self._Inventory[self._Name] < 200:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 200
                    self._Size = Size
            elif Size == "medium":
                if self._Inventory[self._Name] < 400:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 400
                    self._Size = Size
            elif Size == "large":
                if self._Inventory[self._Name] < 600:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 600
                    self._Size = Size
            else:
                raise ItemError("Invalid size.")

        elif self._Name == "nuggets":
            if Size == "small":
                if self._Inventory[self._Name] < 4:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 4
                    self._Size = Size
            elif Size == "medium":
                if self._Inventory[self._Name] < 8:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 8
                    self._Size = Size
            elif Size == "large":
                if self._Inventory[self._Name] < 12:
                    raise ItemError(f'Not enough {self._Name} in stock.')
                else:
                    self._Inventory[self._Name] -= 12
                    self._Size = Size
            else:
                raise ItemError("Invalid size.")
