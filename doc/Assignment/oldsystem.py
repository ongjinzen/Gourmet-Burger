from order import Order, GenerateID
from error import OrderError, checkOrderExist
class FoodSystem():

    def __init__(self,inventory = None, mains = None, sides = None, drinks = None):
        self._inventory = inventory
        
        self._mains = mains
        self._sides = sides
        self._drinks = drinks
        self._completedOrders = []
        self._incompleteOrders = []
        ingrediants = {}
        ingrediants.update(mains) 
        ingrediants.update(sides)
        ingrediants.update(drinks)
        self._ingredientsCost = ingrediants


    @property
    def inventory(self):
        return self._inventory
    @property
    def mains(self):
        return self._mains
    @property
    def drinks(self):
        return self._drinks
    @property
    def sides(self):
        return self._sides 
    @property
    def ingredientsCost(self):
        return self._ingredientsCost
    @property
    def completedOrders(self):
        return self._completedOrders
    @property
    def incompleteOrders(self):
        return self._incompleteOrders
    @inventory.setter
    def inventory(self,value):
        self._inventory = value

    def __str__(self):
        return f'System info \n  <Inventory>\n {self.inventory} \n <MENU>\n {self.ingredientsCost}\n <Incomplete Orders>\n {self.incompleteOrders}\n <Complete Orders>\n {self.completedOrders}\n'
    
    """
    Functions
    """
    def CreateOrder(self):
        newOrder = Order(self.inventory,self.ingredientsCost)
        return newOrder

    def DeleteOrder(self, orderToDelete):
        try:
            checkOrderExist(self, orderToDelete)
        except OrderError as err:
            print(f'{err.message}')
        else:

            for order in self.completedOrders :
                if order == orderToDelete :
                    self.completedOrders.remove(orderToDelete)
            for order in self.incompleteOrders:
                if order == orderToDelete :
                    self.incompleteOrders.remove(orderToDelete)
        
            pass
        
    def SubmitOrder(self, orderToSubmit):
        self.inventory = orderToSubmit.inventory
        orderToSubmit.status = "incomplete"
        self.incompleteOrders.append(orderToSubmit)
        pass

    def prepareOrder(self, orderToPrepare):
        try:
            checkOrderExist(self, orderToPrepare)
        except OrderError as err:
            print(f'{err.message}')
        else:
            orderToPrepare.status = "incomplete"
            pass

    def completeOrder(self, orderToComplete):
        try:
            checkOrderExist(self, orderToComplete)
        except OrderError as err:
            print(f'{err.message}')
        else:
            orderToComplete.status = "complete"
            self.completedOrders.append(orderToComplete)
            self.incompleteOrders.remove(orderToComplete)
            pass


    def checkStatus(self, orderToCheck):
        try:
            checkOrderExist(self, orderToCheck)
        except OrderError as err:
            print(f'{err.message}')
        else:
            allOrders = self.viewAllOrders()
            for order in allOrders:
                if order == orderToCheck:
                    status = order.status
            return status

    def viewAllOrders(self):
        incom = self.viewCompleteOrders()
        com = self.viewIncompleteOrders()
        incom.extend(com)
        return incom
    
    def viewID(self,ID):
        orders = self.viewAllOrders()
        for order in orders:
            if str(order.ID) == str(ID):
                return order
        return "no order with that ID found"
    def viewCompleteOrders(self):
        return self.completedOrders

    def viewIncompleteOrders(self):
        return self.incompleteOrders
    
    def updateStock(self, stock, num):
        self.inventory[stock] += num
        pass

    def newStock(self, stock, num, cost, dish):
        self.inventory[stock] = num
        self.ingredientsCost[stock] = cost
        if dish == 'main' :
            self.mains[stock] = cost
        if dish == 'side' :
            self.sides[stock] = cost
        if dish == 'drink' :
            self.drinks[stock] = cost
        pass
    def viewMenu(self):
        return self.ingredientsCost
    def viewMains(self):
        return self.mains
    def viewSides(self):
        return self.sides
    def viewDrinks(self):
        return self.drinks
