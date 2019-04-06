from order import Order
from errors import ItemError

class System():

    def __init__(self, Inventory, Ingredient_Costs):
        self._Inventory = Inventory
        self._Ingredient_Costs = Ingredient_Costs
        self._Completed_Orders = []
        self._Incomplete_Orders = []

    def Create_Order(self):
        new_order = Order(self._Inventory, self._Ingredient_Costs)
        return new_order

    def Delete_Order(self, order):
        for item in order.Items:
            order.Remove_From_Order(item)

    def Submit_Order(self, order):
        order.Status = "Preparing"
        self._Incomplete_Orders.append(order)

    def 