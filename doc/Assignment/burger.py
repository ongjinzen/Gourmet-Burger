from errors import ItemError
from item import Item


class Burger (Item):

    def __init__(self, Inventory, Ingredient_Costs):
        super().__init__(Inventory, Ingredient_Costs)
        self._Bun_Type = None
        self._Num_Buns = 0
        self._Patty_Type = None
        self._Num_Patties = 0
        self._Other = []

    def __str__(self):
        output = 'This burger contains:\n'
        output += f'{self._Num_Buns} pieces of {self._Bun_Type} buns\n'
        output += f'{self._Num_Patties} pieces of {self._Patty_Type} patties\n'
        output += f'and the following sides:\n'
        
        for ingredient in self._Other:
            output += ingredient.capitalize()
            output += ', '

        output = output[:-2]

        return output

    def Calculate_Cost(self):
        
        base_cost = 3
        bun_cost = self._Num_Buns * self._Ingredient_Costs[self._Bun_Type]
        patty_cost = self._Num_Patties * self._Ingredient_Costs[self._Patty_Type]

        other_cost = 0

        for other in self._Other:
            other_cost += self._Ingredient_Costs[other]

        return base_cost + bun_cost + patty_cost + other_cost

    def Check_Ingredients (self):
        
        if self._Num_Buns < 2 or self._Num_Buns > 4:
            raise ItemError("Invalid number of buns selected.")
        elif self._Num_Patties <1 or self._Num_Patties > 3:
            raise ItemError("Invalid number of patties selected.")

        return True

    def Clear_Ingredients(self):
        
        self._Inventory[self._Bun_Type] += self._Num_Buns
        self._Num_Buns = 0
        self._Inventory[self._Patty_Type] += self._Num_Patties
        self._Num_Patties = 0

        for ingredient in self._Other:
            self._Inventory[ingredient] += 1
            
        for ingredient in self._Other:
            self._Other.remove(ingredient)

    @property
    def Bun_Type(self):
        return self._Bun_Type

    # Choose the type of bun
    @Bun_Type.setter
    def Bun_Type(self, Bun_Type):
        
        if Bun_Type == "white" or Bun_Type == "sesame":
            if self._Bun_Type == None:
                self._Bun_Type = Bun_Type
            elif Bun_Type != self._Bun_Type:
                self._Inventory[self._Bun_Type] += self._Num_Buns
                self._Num_Buns = 0
                self._Bun_Type = Bun_Type
        else:
            raise ItemError("Invalid bun type.")


    @property
    def Num_Buns(self):
        return self._Num_Buns

    # Increment the number of buns by 1
    def Add_Bun(self):

        if self._Bun_Type == None:
            raise ItemError("Please select a bun type.")
        else:
            if self._Num_Buns < 4:
                if (self._Inventory[self._Bun_Type] > 0):
                    self._Inventory[self._Bun_Type] -= 1
                    self._Num_Buns += 1
                else:
                    raise ItemError(f"Not enough {self._Bun_Type} buns in stock.")
            else:
                raise ItemError("A burger cannot have more than 4 buns.")

    # Decrement the number of buns by 1
    def Remove_Bun(self):
        
        if (self._Num_Buns > 2):
            self._Inventory[self._Bun_Type] += 1
            self._Num_Buns -= 1
        else:
            raise ItemError("A burger cannot have less than 2 buns.")
        
    @property
    def Patty_Type(self):
        return self._Patty_Type

    # Choose the type of patty
    @Patty_Type.setter
    def Patty_Type(self, Patty_Type):
        if Patty_Type == "beef" or Patty_Type == "chicken":
            if self._Patty_Type == None:
                self._Patty_Type = Patty_Type
            elif Patty_Type != self._Patty_Type:
                self._Inventory[self._Patty_Type] += self._Num_Patties
                self._Num_Patties = 0
                self._Patty_Type = Patty_Type
        else:
            raise ItemError("Invalid patty type.")

    @property
    def Num_Patties(self):
        return self._Num_Patties

    # Increment the number of patties by 1
    def Add_Patty(self):
        
        if self._Patty_Type == None:
            raise ItemError("Please select a patty type.")
        else:
            if self._Num_Patties < 3:
                if (self._Inventory[self._Patty_Type] > 0):
                    self._Inventory[self._Patty_Type] -= 1
                    self._Num_Patties += 1
                else:
                    raise ItemError(f"Not enough {self._Patty_Type} patties in stock.")
            else:
                raise ItemError("A burger cannot have more than 3 patties.")

    # Decrement the number of patties by 1
    def Remove_Patty(self):
        if (self._Num_Patties > 1):
            self._Inventory[self._Patty_Type] += 1
            self._Num_Patties -= 1
        else:
            raise ItemError("A burger cannot have less than 1 patty.")

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
