from abc import ABC, abstractmethod
from errors import ItemError

class Item (ABC):

    def __init__(self, Inventory, Ingredient_Costs):
        self._Inventory = Inventory
        self._Ingredient_Costs = Ingredient_Costs

    @abstractmethod
    def Calculate_Cost(self):
        pass

    @abstractmethod
    def Check_Ingredients(self):
        pass

    @abstractmethod
    def Clear_Ingredients(self):
        pass

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
        output += f'and the following sides: '
        
        for ingredient in self._Other:
            output += ingredient
            output += ','

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

    def Remove_Bun(self):
        
        if (self._Num_Buns > 2):
            self._Inventory[self._Bun_Type] += 1
            self._Num_Buns -= 1
        else:
            raise ItemError("A burger cannot have less than 2 buns.")
        
    @property
    def Patty_Type(self):
        return self._Patty_Type

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

    def Remove_Patty(self):
        if (self._Num_Patties > 1):
            self._Inventory[self._Patty_Type] += 1
            self._Num_Patties -= 1
        else:
            raise ItemError("A burger cannot have less than 1 patty.")

    @property
    def Other(self):
        return self._Other

    def Add_Other(self, ingredient):
        
        if ingredient in {"cheese", "lettuce", "onion", "tomato", "avocado"}:
            if self._Inventory[ingredient] > 0:
                self._Inventory[ingredient] -= 1
                self._Other.append(ingredient)
            else:
                raise ItemError(f"Not enough {ingredient} in stock.")
        else:
            raise ItemError("Please select a valid ingredient.")

    def Remove_Other(self, ingredient):
        
        if ingredient in self._Other:
            self._Inventory[ingredient] += 1
            self._Other.remove(ingredient)
        else:
            raise ItemError("Ingredient not in item.")

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
        output += f'and the following sides: '
        
        for ingredient in self._Other:
            output += ingredient
            output += ','

        return output

    def Calculate_Cost(self):
        
        base_cost = 4
        wrap_cost = self._Ingredient_Costs[self._Wrap_Type]
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
        
        self._Inventory[self._Wrap_Type] += 1
        self._Inventory[self._Filling_Type] += 1

        for ingredient in self._Other:
            self._Inventory[ingredient] += 1
            
        for ingredient in self._Other:
            self._Other.remove(ingredient)

    @property
    def Wrap_Type(self):
        return self._Wrap_Type

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

    def Add_Other(self, ingredient):
        
        if ingredient in {"cheese", "lettuce", "onion", "tomato", "avocado"}:
            if self._Inventory[ingredient] > 0:
                self._Inventory[ingredient] -= 1
                self._Other.append(ingredient)
            else:
                raise ItemError(f"Not enough {ingredient} in stock.")
        else:
            raise ItemError("Please select a valid ingredient.")

    def Remove_Other(self, ingredient):
        
        if ingredient in self._Other:
            self._Inventory[ingredient] += 1
            self._Other.remove(ingredient)
        else:
            raise ItemError("Ingredient not in item.")

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

class Fountain_Drinks_and_Sides (Item):

    def __init__(self, Inventory, Ingredient_Costs, Name,):
        
        if Name in ["apple juice", "orange juice", "fries", "nuggets"]:
            self._Name = Name
            self._Size = None
            self._Inventory = Inventory
            self._Ingredient_Costs = Ingredient_Costs
        else:
            raise ItemError("Invalid item.")

    def __str__(self):
        
        return self._Name.capitalize()

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

        return cost

    def Check_Ingredients (self):

        if not (self._Name in ["apple juice", "orange juice", "fries", "nuggets"]):
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
        elif self._Name == "fries":
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
            elif self._Name == "fries":
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

        elif self._Name == "fries":
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