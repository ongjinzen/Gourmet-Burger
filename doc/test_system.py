#test
from system import FoodSystem
import pytest


@pytest.fixture 
def system_fixture():
    food =  { "white buns": 5, "sesame buns" : 3, 'lettuce' : 5, 'tomato' : 6 ,'onion' : 7, 'beef patty':4, 'chicken patty' : 10, 'pita' :5, 'tortilla': 12, 'cheese':14, 'avacado': 15, 'pepsi': 20, 'coke': 12, 'juice': 1000, 'chips':5000, 'nuggets': 100}
    mains =  {"burger":5, "wrap" :6, "white buns": 1, "sesame buns" : 1.5, 'lettuce' : 1, 'tomato' : 2 ,'onion' : 3, 'beef patty':2, 'chicken patty' : 2.50, 'pita' :3, 'tortilla': 4, 'cheese':2, 'avacado': 10,}
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
    menu  =  {"burger":5,"wrap":6, "white buns": 1, "sesame buns" : 1.5, 'lettuce' : 1, 'tomato' : 2 ,'onion' : 3, 'beef patty':2, 'chicken patty' : 2.50, 'pita' :3, 'tortilla': 4, 'cheese':2, 'avacado': 10, 'pepsi': 2.50, 'coke': 3.50, 'juice medium ': 3.5,'juice large': 4,'juice small': 2.5, 'chips small':2,'chips meidum':3,'chips large':3.5, '4-nuggets': 4,'8-nuggets': 7,'12-nuggets': 10}
    
    assert( test == menu)

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
    order.addToOrder('burger')
    menu = system_fixture.ingredientsCost 
    food = system_fixture.inventory
    assert(order.inventory == food)
    assert(order.ingredientsCost == menu)
    assert(str(order.ID) == '33')
    assert(order.items[0] == "burger")
    assert(order.status == "Ordering")

def test_add2_item(system_fixture):
    order = system_fixture.CreateOrder()
    order.addToOrder('burger')
    order.addToOrder('small chips')
    menu = system_fixture.ingredientsCost 
    food = system_fixture.inventory
    assert(order.inventory == food)
    assert(order.ingredientsCost == menu)
    assert(str(order.ID) == '34')
    assert(order.items[0] == "burger")
    assert(order.items[1] == "small chips")
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