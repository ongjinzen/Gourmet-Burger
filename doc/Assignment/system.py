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
        self._Generate_ID = 0

    def __str__(self):
        output = ""
        output += f"{len(self._Completed_Orders)} completed orders.\n"
        output += f"{len(self._Incomplete_Orders)} incomplete orders.\n\n"
        
        output += f"Inventory:\n"
        for ingredient in self._Inventory:
            output += f"{ingredient} : {self._Inventory[ingredient]}\n"

        return output

    @property
    def Inventory(self):
        return self._Inventory

    @property
    def Ingredient_Costs(self):
        return self._Ingredient_Costs

    @property
    def Completed_Orders(self):
        return self._Completed_Orders

    @property
    def Main_Menu(self):
        return self._Main_Menu

    @property
    def Drink_Menu(self):
        return self._Drink_Menu

    @property
    def Side_Menu(self):
        return self._Side_Menu

    @property
    def Incomplete_Orders(self):
        return self._Incomplete_Orders

    def Create_Order(self):
        new_order = Order(self._Inventory, self._Ingredient_Costs)
        return new_order

    def Delete_Order(self, order):
        
        i = len(order.Items) - 1

        while i >= 0:
            order.Remove_From_Order(order.Items[i])
            i -= 1

    def Submit_Order(self, order):
        
        if len(order.Items) < 1:
            raise OrderError("No items in order.")
        else:
            order.ID = self._Generate_ID
            self._Generate_ID += 1
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

    def View_Order(self, ID):
        for order in self._Incomplete_Orders:
            if ID == order.ID:
                return order
        
        for order in self._Completed_Orders:
            if ID == order.ID:
                return order

        raise SystemError("Order not found.")

    def Check_Status(self, ID):
        for order in self._Incomplete_Orders:
            if ID == order.ID:
                return order.Status
        
        for order in self._Completed_Orders:
            if ID == order.ID:
                return order.Status

        raise SystemError("Order not found.")

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

    def View_Main_Menu(self):
        return self._Main_Menu

    def View_Side_Menu(self):
        return self._Side_Menu

    def View_Drink_Menu(self):
        return self._Drink_Menu

    