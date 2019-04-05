class GenerateID():

    def __init__(self):
        self._ID = 0

    def __call__(self):
        self._ID += 1
        return self._ID


    


class Order():
    def __init__(self,inventory, ingredientsCost):
        self._inventory = inventory
        self._ingredientsCost = ingredientsCost
        self._items = []
        self._ID = GenerateID()
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

    def __str__(self):
        return f'Order {self.ID} \n  status: {self.status} \n Items: {self.items} \n totat cost : ${calculateCost(self)}'
    
    '''
    methods
    '''

    def createItem(self):
        pass
    def deleteItem(self, item):
        pass
    
    def calculateCost(self):
        cost =0
        for item in self.items:
            cost += self.ingredientsCost[item]

        return cost
    def addToOrder(self,item):
        self.items.append(item)
        pass
    
    def removeFromOrder(self, item):
        self.items.remove(item)
        pass
    def viewOrder(self)
        print(self)
        pass