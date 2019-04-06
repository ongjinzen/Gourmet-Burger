from order import Order
from errors import *

class System():

    def __init__(self, Inventory, Ingredient_Costs):
        self._Inventory = Inventory
        self._Ingredient_Costs = Ingredient_Costs
        self._Completed_Orders = []
        self._Incomplete_Orders = []
        self._Main_Menu = ["Burger", "Wrap"]
        self._Drink_Menu = ["coke", "pepsi", "apple juice", "orange juice"]
        self._Side_Menu = ["fries", "nuggets"]

    def Create_Order(self):
        new_order = Order(self._Inventory, self._Ingredient_Costs)
        return new_order

    def Delete_Order(self, order):
        for item in order.Items:
            order.Remove_From_Order(item)

    def Submit_Order(self, order):
        
        if len(order.Items) < 1:
            raise OrderError("No items in order.")
        else:
            order.Status = "Submitted"
            self._Incomplete_Orders.append(order)

    def Preparing_Order(self, order):
        if order in self._Incomplete_Orders and order.Status == "Submitted":
            order.Status = "Preparing order"

    def Complete_Order(self, order):
        if order in self._Incomplete_Orders and order.Status == "Preparing order":
            order.Status = "Completed"
            self._Incomplete_Orders.remove(order)
            self._Completed_Orders.append(order)

    def Check_Status(self, ID):
        for order in self._Incomplete_Orders:
            if ID == order.ID:
                return order
        
        for order in self._Complete_Orders:
            if ID == order.ID:
                return order

        return "ID not found."

    def View_All_Orders(self):
        orders = []
        for order in self._Incomplete_Orders:
            orders.append(order)
        for order in self._Completed_Orders:
            orders.append(order)

        return orders
    
    def View_Incomplete_Orders(self):
        orders = []
        for order in self._Incomplete_Orders:
            orders.append(order)

        return orders

    def View_Complete_Orders(self):
        orders = []
        for order in self._Completed_Orders:
            orders.append(order)

        return orders

    def Update_Stock(self, Ingredient, amount):
        self._Inventory[Ingredient] += amount

    def New_Stock(self, Ingredient, price):
        self._Ingredient_Costs[Ingredient] = price

    def View_Menu()