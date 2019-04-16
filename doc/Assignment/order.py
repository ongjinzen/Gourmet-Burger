from bottled_drink import Bottled_Drink
from burger import Burger
from errors import ItemError
from fountain_drinks_and_sides import Fountain_Drinks_and_Sides
from wrap import Wrap


class Order ():

    def __init__(self, Inventory, Ingredient_Costs):
        self._Items = []
        self._Inventory = Inventory
        self._Ingredient_Costs = Ingredient_Costs
        self._ID = None
        self._Status = None

    def __str__(self):
        output = ""
        output += f"Order ID: {self._ID}\n"
        output += f"Order Status: {self._Status}\n"
        output += f"Items in this order: {len(self._Items)}"

        return output

    @property
    def Items(self):
        return self._Items
    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, status):
        self._Status = status

    def Create_Item(self, Name):

        if Name == "Burger":
            item = Burger(self._Inventory, self._Ingredient_Costs)
        #default burger is 2 white buns beef patty and 1 lettuce. 
        elif Name == "Default Burger":
            item = Burger(self._Inventory, self._Ingredient_Costs)
            item.Bun_Type = "white"
            item.Add_Bun()
            item.Add_Bun()
            item.Patty_Type = "beef"
            item.Add_Patty()
            item.Add_Other("lettuce")
        elif Name == "Wrap":
            item = Wrap(self._Inventory, self._Ingredient_Costs)
        elif Name == "coke" or Name == "pepsi":
            item = Bottled_Drink(self._Inventory, self._Ingredient_Costs, Name)
        elif Name in ["apple juice", "orange juice", "fries", "nuggets","sundae"]:
            item = Fountain_Drinks_and_Sides(self._Inventory, self._Ingredient_Costs, Name)
        else:
            raise ItemError("Invalid item.")

        return item
    
    

    def Delete_Item(self, Item):

        Item.Clear_Ingredients()

    def Calculate_Cost(self):
        cost = 0
        
        for item in self._Items:
            cost += item.Calculate_Cost()

        return cost

    def Add_To_Order(self, Item):
        
        assert(Item.Check_Ingredients() == True)
        self._Items.append(Item)

    def Remove_From_Order(self, Item):
        Item.Clear_Ingredients()
        self._Items.remove(Item)