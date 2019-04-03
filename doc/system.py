

class FoodSystem():

    def __init__(self,inventory = None, ingredientsCost = None):
        self._inventory = inventory
        self._ingredientsCost = ingredientsCost
        self._completedOrders = []
        self._incompleteOrders = []

    @property
    def inventory(self):
        return self._inventory
    @property
    def ingredientsCost(self):
        return self._ingredientsCost
    @property
    def completedOrders(self):
        return self._completedOrders
    @property
    def incompleteOrders(self):
        return self._incompleteOrders

    def __str__(self):
        return f'System info \n  <Inventory>\n {self.inventory} \n <MENU>\n {self.ingredientsCost}\n <Incomplete Orders>\n {self.incompleteOrders}\n <Complete Orders>\n {self.completedOrders}\n'
    
    """
    Functions
    """
    def CreateOrder(self):
        newOrder = Order(self.inventory,self.ingredientsCost)
        return newOrder

    def DeleteOrder(self, orderToDelete):
        for order in self.completedOrders :
            if order == orderToDelete :
                self.completedOrders.remove(orderToDelete)
        for order in self.incompleteOrders:
            if order == orderToDelete :
                self.incompleteOrders.remove(orderToDelete)
    
        pass
    
    def SubmitOrder(self, orderToSubmit):
        toMany = []
        for item in orderToSubmit.Items:
            if orderToSubmit.Items.count(item) > self.inventory[item]:
                toMany.append(f'{orderToSubmit.Items.count(item) - self.inventory[item]} to many {item}\'s')

        if not toMany:
            return toMany
        else :
            orderToSubmit.status = "incomplete"
            self.incompleteOrders.append(orderToSubmit)
            pass

    def prepareOrder(self, orderToPrepare):
        orderToPrepare.status = "incomplete"
        pass

    def completeOrder(self, orderToComplete):
        orderToComplete.status = "complete"
        self.completedOrders.append(orderToComplete)
        self.incompleteOrders.remove(orderToComplete)
        pass


    def checkStatus(self, orderToCheck):
        allOrders = self.viewAllOrders()
        status = allOrders[orderToCheck].status
        return status

    def viewAllOrders(self):
        return self.viewIncompleteOrders.extend(self.viewCompleteOrders)
    
    def viewCompleteOrders(self):
        return self.completedOrders

    def viewIncompleteOrders(self):
        return self.incompleteOrders
    
    def updateStock(self, stock, num):
        self.inventory[stock] += num
        pass

    def newStock(self, stock, num, cost):
        self.inventory[stock] = num
        self.ingredientsCost[stock] = cost
        pass
    def viewMenu(self):
        return self.ingredientsCost
