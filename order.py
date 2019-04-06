from errors import ItemError

class Order():

    def __init__(self, Inventory, Ingredient_Costs):
        self._Items = []
        self._Inventory = Inventory
        self._Ingredient_Costs = Ingredient_Costs
        self._ID = None
        self._Status = None

    def Create_Item(self, Name):

        if Name == "Burger":
            item = Burger(self._Inventory, self._Ingredient_Costs)
        elif Name == "Wrap":
            item = Wrap(self._Inventory, self._Ingredient_Costs)
        elif Name == "Bottled_Drink":
            item = Bottled_Drink(self._Inventory, self._Ingredient_Costs)
        elif Name == "Fountain_Drinks_and_Sides":
            item = Fountain_Drinks_and_Sides(self._Inventory, self._Ingredient_Costs)
        else:
            raise ItemError("Invalid item.")

        return item

    def Delete_Item(self, )