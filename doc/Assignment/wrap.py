from errors import ItemError
from item import Item


class Wrap(Item):
    
    def __init__(self, Inventory, Ingredient_Costs):
        super().__init__(Inventory, Ingredient_Costs)
        self._Wrap_Type = None
        self._Filling_Type = None
        self._Other = []

    def __str__(self):
        output = 'This wrap contains:\n'
        output += f'A {self._Wrap_Type} wrap\n'
        output += f'{self._Filling_Type} filling\n'
        
        for ingredient in self._Other:
            output += ingredient.capitalize()
            output += ', '

        output = output[:-2]

        return output

    def Calculate_Cost(self):
        
        base_cost = 4
        if self._Wrap_Type == None:
            wrap_cost = 0
        else:
            wrap_cost = self._Ingredient_Costs[self._Wrap_Type]
        
        if self._Filling_Type == None:
            filling_cost = 0
        else:
            filling_cost = self._Ingredient_Costs[self._Filling_Type]

        other_cost = 0

        for other in self._Other:
            other_cost += self._Ingredient_Costs[other]

        return base_cost + wrap_cost + filling_cost + other_cost

    def Check_Ingredients (self):
        
        if self._Wrap_Type == None:
            raise ItemError("No wrap selected.")
        elif self._Filling_Type == None:
            raise ItemError("No filling selected.")

        return True

    def Clear_Ingredients(self):
        
        if self._Wrap_Type != None:
            self._Inventory[self._Wrap_Type] += 1
        if self._Filling_Type != None:
            self._Inventory[self._Filling_Type] += 1

        for ingredient in self._Other:
            self._Inventory[ingredient] += 1
            
        for ingredient in self._Other:
            self._Other.remove(ingredient)

    @property
    def Wrap_Type(self):
        return self._Wrap_Type

    # Choose the type of wrap
    @Wrap_Type.setter
    def Wrap_Type(self, Wrap_Type):
        
        if Wrap_Type == "pita" or Wrap_Type == "tortilla":
            if self._Inventory[Wrap_Type] > 0:
                if Wrap_Type != self._Wrap_Type and self._Wrap_Type != None:
                    self._Inventory[self._Wrap_Type] += 1
                self._Wrap_Type = Wrap_Type
                self._Inventory[self._Wrap_Type] -= 1
            else:
                raise ItemError(f"Not enough {Wrap_Type} wraps in stock.")
        else:
            raise ItemError("Invalid wrap type.")

    @property
    def Filling_Type(self):
        return self._Filling_Type

    # Choose the type of filling
    @Filling_Type.setter
    def Filling_Type(self, Filling_Type):
        
        if Filling_Type == "pork" or Filling_Type == "tuna":
            if self._Inventory[Filling_Type] > 0:
                if Filling_Type != self._Filling_Type and self._Filling_Type != None:
                    self._Inventory[self._Filling_Type] += 1
                self._Filling_Type = Filling_Type
                self._Inventory[self._Filling_Type] -= 1
            else:
                raise ItemError(f"Not enough {Filling_Type} filling in stock.")
        else:
            raise ItemError("Invalid filling type.")

    @property
    def Other(self):
        return self._Other

    # Add other ingredients
    def Add_Other(self, ingredient):
        
        if ingredient in {"cheese", "lettuce", "onion", "tomato", "avocado"}:
            if self._Inventory[ingredient] > 0:
                self._Inventory[ingredient] -= 1
                self._Other.append(ingredient)
            else:
                raise ItemError(f"Not enough {ingredient} in stock.")
        else:
            raise ItemError("Please select a valid ingredient.")

    # Remove other ingredients
    def Remove_Other(self, ingredient):
        
        if ingredient in self._Other:
            self._Inventory[ingredient] += 1
            self._Other.remove(ingredient)
        else:
            raise ItemError("Ingredient not in item.")
