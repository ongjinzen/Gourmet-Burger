class OrderError(Exception):
    def __init__(self, message):
        self._message = message
    @property
    def message(self):
        return self._message
    


def checkOrderExist(system, checkOrder):
    allOrders = system.viewAllOrders()
    exist = False
    for order in allOrders:
        if order == checkOrder:
            exist = True

    if exist == False:
        raise OrderError("could not find a matching order")
    pass

class OrderStatusError(Exception):
    def __init__(self, message):
        
        self._message = message
    
    @property
    def message(self):
        return self._message

def checkOrderStatusError(checkOrder):
    if checkOrder.status != "Ordering":
        raise OrderStatusError("Order has already been submitted")
    pass

class ItemError(Exception):

    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

class OrderError(Exception):
    
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

