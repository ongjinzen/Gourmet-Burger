from order import Order
from errors import SystemError

class System():

    def __init__(self, Inventory, Ingredient_Costs):
        self._Inventory = Inventory
        self._Ingredient_Costs = Ingredient_Costs
        self._Current_Order = None
        self._Current_Item = None
        self._Completed_Orders = []
        self._Incomplete_Orders = []
        self._Main_Menu = ["Burger", "Wrap", "Default Burger", "Default Wrap"]
        self._Drink_Menu = ["coke", "pepsi", "apple juice", "orange juice"]
        self._Side_Menu = ["fries", "nuggets", "chocolate sundae", "strawberry sundae"]
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

    @property
    def Current_Order(self):
        return self._Current_Order

    @Current_Order.setter
    def Current_Order(self, order):
        self._Current_Order = order

    @property
    def Current_Item(self):
        return self._Current_Item

    @Current_Item.setter
    def Current_Item(self, item):
        self._Current_Item = item
        
    # Creates a new order 
    def Create_Order(self):
        new_order = Order(self._Inventory, self._Ingredient_Costs)
        return new_order

    # Deletes an order when it is cancelled and restores the inventory
    def Delete_Order(self, order):
        
        if isinstance(order, Order):
            i = len(order.Items) - 1

            while i >= 0:
                order.Remove_From_Order(order.Items[i])
                i -= 1
            if order in self._Completed_Orders:
                self._Completed_Orders.remove(order)
            elif order in self._Incomplete_Orders:
                self._Incomplete_Orders.remove(order)
        else:
            raise SystemError("Invalid order.")

    # Finalises an order and sends it to the list of incomplete orders
    def Submit_Order(self, order):
        
        if order.Status == None:
            if len(order.Items) < 1:
                raise OrderError("No items in order.")
            else:
                order.ID = self._Generate_ID
                self._Generate_ID += 1
                order.Status = "Submitted"
                self._Incomplete_Orders.append(order)
        else:
            raise SystemError("Order status error.")

    # Kitchen staff changing an order status when they are preparing it 
    def Preparing_Order(self, order):
        if order in self._Incomplete_Orders and order.Status == "Submitted":
            order.Status = "Preparing order"
        else:
            raise SystemError("Order status error.")

    # Changes an orders status to complete once it is ready, also moves it to the Completed orders list
    def Complete_Order(self, order):
        if order in self._Incomplete_Orders and order.Status == "Preparing order":
            order.Status = "Completed"
            self._Incomplete_Orders.remove(order)
            self._Completed_Orders.append(order)
        else:
            raise SystemError("Order status error.")

    # Returns the order when given a specific order ID, lokking through only orders submitted
    def View_Order(self, ID):
        for order in self._Incomplete_Orders:
            if ID == order.ID:
                return order
        
        for order in self._Completed_Orders:
            if ID == order.ID:
                return order

        raise SystemError("Order not found.")

    # Return the current status of an order once it has been submitted
    def Check_Status(self, ID):
        for order in self._Incomplete_Orders:
            if ID == order.ID:
                return order.Status
        
        for order in self._Completed_Orders:
            if ID == order.ID:
                return order.Status

        raise SystemError("Order not found.")

    # Returns a list of all orders that have been submitted
    def View_All_Orders(self):
        orders = []
        for order in self._Incomplete_Orders:
            orders.append(order)
        for order in self._Completed_Orders:
            orders.append(order)

        return orders

    # Returns a list of all orders that have been submitted but have not been cooked yet
    def View_Incomplete_Orders(self):
        orders = []
        for order in self._Incomplete_Orders:
            orders.append(order)

        return orders

    # Returns a list of all orders that are ready
    def View_Complete_Orders(self):
        orders = []
        for order in self._Completed_Orders:
            orders.append(order)

        return orders

    # Increases the amount of stock of a speciifed ingrediant by a specified amount
    def Update_Stock(self, Ingredient, amount):
        self._Inventory[Ingredient] += amount

    # Adds a new stock to the menu
    def New_Stock(self, Ingredient, price):
        self._Ingredient_Costs[Ingredient] = price

    # Returns a list of all main menu items
    def View_Main_Menu(self):
        return self._Main_Menu

    # Returns a list of all side menu items
    def View_Side_Menu(self):
        return self._Side_Menu

    # Returns a list of all drinks on the  menu 
    def View_Drink_Menu(self):
        return self._Drink_Menu