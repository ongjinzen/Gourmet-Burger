#test
from system import FoodSystem
import pytest


@pytest.fixture 
def system_fixture():
    food = {
        "white": 10,
        "sesame": 10,
        "beef": 10,
        "chicken": 10,
        "pita": 10,
        "tortilla": 10,
        "pork": 10,
        "tuna": 10,
        "cheese": 10,
        "lettuce": 10,
        "onion": 10,
        "tomato": 10,
        "avocado": 10,
        "pepsi": 10,
        "coke": 10,
        "apple juice": 300,
        "orange juice": 600,
        "fries": 500,
        "nuggets": 10,
}
    mains =  {"burger":5, "wrap" :4, "white": 1, "sesame" : 1.5, 'lettuce' : 1, 'tomato' : 2 ,'onion' : 3, 'beef':2, 'chicken' : 2.50, 'pita' :3, 'tortilla': 4, 'pork': 3, 'tuna':3.5, 'cheese':2, 'avacado': 10,}
    drinks = { 'pepsi': 2.50, 'coke': 3.50, 'juice medium ': 3.5,'juice large': 4,'juice small': 2.5}
    sides =  {'chips small':2,'chips meidum':3,'chips large':3.5, '4-nuggets': 4,'8-nuggets': 7,'12-nuggets': 10}
    system = FoodSystem(food,mains,sides,drinks)
    #print(system)
    ingrediants = {}
    ingrediants.update(mains) 
    ingrediants.update(sides)
    ingrediants.update(drinks)
    assert( system.ingredientsCost == ingrediants )
    assert(system.inventory == food)
    return system

def test_new_stock(system_fixture):
    system_fixture.newStock('celery', 10000, 10.10,"main")
    assert(system_fixture.ingredientsCost['celery'] == 10.10)
    assert(system_fixture.inventory['celery'] == 10000)
    pass
def test_create_order(system_fixture):
    testOrder = system_fixture.CreateOrder()
   
    assert (str(testOrder.ID) == '1')
    assert(testOrder.inventory == system_fixture.inventory)
    assert(testOrder.ingredientsCost == system_fixture.ingredientsCost)
    assert(testOrder.items == [])
    assert(testOrder.status == "Ordering")
    pass

def test_create2_order(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    assert (str(testOrder.ID) == '2')
    assert(testOrder.inventory == system_fixture.inventory)
    assert(testOrder.ingredientsCost == system_fixture.ingredientsCost)
    assert(testOrder.items == [])
    assert(testOrder.status == "Ordering")
    assert (str(testOrder2.ID) == '3')
    assert(testOrder2.inventory == system_fixture.inventory)
    assert(testOrder2.ingredientsCost == system_fixture.ingredientsCost)
    assert(testOrder2.items == [])
    assert(testOrder2.status == "Ordering")
    pass
def test_submit_order(system_fixture):
    testOrder = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    #print(system_fixture)
    assert(system_fixture.incompleteOrders[0] == testOrder)
    assert(testOrder.status == "incomplete")

def test_complete_order(system_fixture):
    testOrder = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    #print(system_fixture)
    assert(system_fixture.incompleteOrders[0] == testOrder)
    assert(testOrder.status == "incomplete")
    system_fixture.completeOrder(testOrder)
    assert(system_fixture.completedOrders[0] == testOrder)
    assert(system_fixture.incompleteOrders == [])
    assert(testOrder.status == "complete")

def test_checkstatus_order(system_fixture):
    testOrder = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    #print(system_fixture)
    assert(system_fixture.incompleteOrders[0] == testOrder)
    assert(testOrder.status == "incomplete")
    assert(system_fixture.checkStatus(testOrder) == "incomplete")

def test_ViewAll_order(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    system_fixture.completeOrder(testOrder)
    orders = system_fixture.viewAllOrders()
    #print(system_fixture)
    assert(orders[0] == testOrder)
    assert(orders[1] == testOrder2)
    assert(orders[2] == testOrder3)

def test_View_ID(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    system_fixture.completeOrder(testOrder)
    test = system_fixture.viewID(testOrder.ID)
    test2 = system_fixture.viewID(testOrder2.ID)
    test3 = system_fixture.viewID(testOrder3.ID)
    assert( test == testOrder)
    assert( test2 == testOrder2)
    assert( test3 == testOrder3)


def test_Complete_Orders(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    system_fixture.completeOrder(testOrder)
    test = system_fixture.viewCompleteOrders()
    assert(test[0] == testOrder )

def test_2Complete_Orders(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    system_fixture.completeOrder(testOrder)
    system_fixture.completeOrder(testOrder2)
    test = system_fixture.viewCompleteOrders()
    assert(test[0] == testOrder )
    assert(test[1] == testOrder2 )

def test_0Complete_Orders(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    test = system_fixture.viewCompleteOrders()
    assert(test == [] )

def test_inComplete_Orders(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    system_fixture.completeOrder(testOrder)
    system_fixture.completeOrder(testOrder2)
    test = system_fixture.viewIncompleteOrders()
    assert(test[0] == testOrder3 )

def test_2inComplete_Orders(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    system_fixture.completeOrder(testOrder)
    
    test = system_fixture.viewIncompleteOrders()
    assert(test[0] == testOrder2 )
    assert(test[1] == testOrder3 )

def test_0inComplete_Orders(system_fixture):
    testOrder = system_fixture.CreateOrder()
    testOrder2 = system_fixture.CreateOrder()
    testOrder3 = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    system_fixture.SubmitOrder(testOrder2)
    system_fixture.SubmitOrder(testOrder3)
    system_fixture.completeOrder(testOrder)
    system_fixture.completeOrder(testOrder2)
    system_fixture.completeOrder(testOrder3)
    test = system_fixture.viewIncompleteOrders()
    assert(test == [] )

def test_view_menu(system_fixture):
    test = system_fixture.viewMenu()
    mains =  {"burger":5, "wrap" :4, "white": 1, "sesame" : 1.5, 'lettuce' : 1, 'tomato' : 2 ,'onion' : 3, 'beef':2, 'chicken' : 2.50, 'pita' :3, 'tortilla': 4, 'pork': 3, 'tuna':3.5, 'cheese':2, 'avacado': 10,}
    drinks = { 'pepsi': 2.50, 'coke': 3.50, 'juice medium ': 3.5,'juice large': 4,'juice small': 2.5}
    sides =  {'chips small':2,'chips meidum':3,'chips large':3.5, '4-nuggets': 4,'8-nuggets': 7,'12-nuggets': 10}
    mains.update(sides)
    mains.update(drinks)
    
    assert( test == mains)

def test_error_check(system_fixture):
    testOrder = system_fixture.CreateOrder()
    system_fixture.SubmitOrder(testOrder)
    fail = 1
    system_fixture.completeOrder(fail)
'''
test order.py
'''

def test_order_setter(system_fixture):
    order = system_fixture.CreateOrder()
    menu  = system_fixture.ingredientsCost
    food =  system_fixture.inventory
    assert(order.inventory == food)
    assert(order.ingredientsCost == menu)
    assert(str(order.ID) == '32')
    assert(order.items == [])
    assert(order.status == "Ordering")

def test_add_item(system_fixture):
    order = system_fixture.CreateOrder()
    burg1 = order.createItem("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order.addToOrder(burg1)
    menu = system_fixture.ingredientsCost 
    food = system_fixture.inventory
    
    assert(order.inventory == food)
    assert(order.ingredientsCost == menu)
    assert(str(order.ID) == '33')
    assert(order.items[0] == "burger")
    assert(order.status == "Ordering")

def test_add2_item(system_fixture):
    order = system_fixture.CreateOrder()
    burg1 = order.createItem("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order.addToOrder(burg1)
    juice = order.createItem("apple juice")
    juice.size = "small"
    order.addToOrder(juice)
    menu = system_fixture.ingredientsCost 
    food = system_fixture.inventory
    assert(order.inventory == food)
    assert(order.ingredientsCost == menu)
    assert(str(order.ID) == '34')
    assert(order.items[0] == "burger")
    assert(order.items[1] == "beef")
    assert(order.items[2] == "cheese")
    assert(order.items[3] == "apple juice") 
    assert(order.status == "Ordering")

def test_calculate_cost(system_fixture):
    order = system_fixture.CreateOrder()
    order.addToOrder('burger')
    order.addToOrder('chips small')
    menu = system_fixture.ingredientsCost 
    food = system_fixture.inventory
    cost = order.calculateCost()
    assert(order.inventory == food)
    assert(order.ingredientsCost == menu)
    assert(str(order.ID) == '35')
    assert(order.items[0] == "burger")
    assert(order.items[1] == "chips small")
    assert(order.status == "Ordering")
    assert(cost == 7 )

def test_remove_item(system_fixture):
    order = system_fixture.CreateOrder()
    order.addToOrder('burger')
    order.addToOrder('small chips')
    menu = system_fixture.ingredientsCost 
    food = system_fixture.inventory
    assert(order.inventory == food)
    assert(order.ingredientsCost == menu)
    assert(str(order.ID) == '36')
    assert(order.items[0] == "burger")
    assert(order.items[1] == "small chips")
    assert(order.status == "Ordering")
    order.removeFromOrder('burger')
    assert(order.items[0] == "small chips")

def test_View_order(system_fixture):
    order = system_fixture.CreateOrder()
    order.addToOrder('burger')
    order.addToOrder('chips small')
    order.viewOrder()