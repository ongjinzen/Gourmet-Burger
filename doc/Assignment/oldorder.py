from error import OrderStatusError, checkOrderStatusError
from item import *

class GenerateID():

    def __init__(self):
        self._ID = 0

    def next(self):
        print(f"inside before {self._ID}")
        self._ID += 1
        print(f"inside after {self._ID}")
        return self._ID
    
    def __str__(self):
        return f'{self._ID}'


def IdGen(i =[0]):
    i[0] += 1
    return i[0]


class Order():
    def __init__(self,inventory, ingredientsCost):
        self._inventory = inventory
        self._ingredientsCost = ingredientsCost
        self._items = []
        self._ID = IdGen()
        self._status = "Ordering"
    
    @property
    def inventory(self):
        return self._inventory
    @property
    def ingredientsCost(self):
        return self._ingredientsCost
    @property
    def items(self):
        return self._items
    @property
    def ID(self):
        return self._ID
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,value):
        self._status = value
    @inventory.setter
    def inventory(self,value):
        self._inventory = value

    def __str__(self):
        return f'Order {self.ID} \n  status: {self.status} \n Items: {self.items} \n totat cost : ${self.calculateCost()}'
    
    '''
    methods
    '''

    def createItem(self, Name):
        if Name == "Burger":
            item = Burger(self.inventory, self.ingredientsCost)
        elif Name == "Wrap":
            item = Wrap(self.inventory, self.ingredientsCost)
        elif Name == "coke" or Name == "pepsi":
            item = Bottled_Drink(self.inventory, self.ingredientsCost, Name)
        elif Name in ["apple juice", "orange juice", "fries", "nuggets"]:
            item = Fountain_Drinks_and_Sides(self.inventory, self.ingredientsCost, Name)
        else:
            raise ItemError("Invalid item.")

        return item
    def deleteItem(self, item):
        Item.Clear_Ingredients()
        pass
    
    def calculateCost(self):
        cost =0
        for item in self.items:
            cost += self.ingredientsCost[item]

        return cost
    def addToOrder(self,item):
        try:
            checkOrderStatusError(self) 
            
        except OrderStatusError as err:
            print(f'order status = {self.status}')
            print(f'{err.message}')
        else:
            diff =  self.inventory #- item.Inventory
            for key in diff:
                diff[key] -+ item.Inventory[key]
            if diff["sesame"] != 0 or diff["white"] != 0:
                self.items.append("burger")
            if diff['pita'] != 0 or diff['tortilla'] != 0 :
                self.items.append("wrap")
            for key, value in diff.items():
                if value != 0:
                    for k in range(value):
                        self.items.append(key)
            self.inventory = item.Inventory
            pass
        
    def removeFromOrder(self, item):
        self.items.remove(item)
        pass
    def viewOrder(self):
        print(self)
        pass