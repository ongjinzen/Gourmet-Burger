import pytest

from errors import SystemError
from order import Order
from system import System
from bottled_drink import Bottled_Drink
from burger import Burger
from errors import ItemError
from fountain_drinks_and_sides import Fountain_Drinks_and_Sides
from wrap import Wrap



@pytest.fixture
def inventory_fixture():
    Inventory = {
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
        "chocolate sundae" : 1000,
        "strawberry sundae" : 500
    }
    return Inventory

@pytest.fixture
def ingredient_cost_fixture():
    Ingredient_costs = {
        "white": 1,
        "sesame": 1.5,
        "beef": 2,
        "chicken": 2.5,
        "pita": 3,
        "tortilla": 4,
        "pork": 3,
        "tuna": 3.5,
        "cheese": 2,
        "lettuce": 1,
        "onion": 3,
        "tomato": 2,
        "avocado": 10,
        "pepsi": 2.5,
        "coke": 3.5,
    }
    return Ingredient_costs
#UC 11 test-1
def test_submit_order(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    system1.Submit_Order(order1)
    assert(order1 in system1.View_Incomplete_Orders())

#UC 11 test-2
def test_submit_order_status(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    system1.Submit_Order(order1)
    assert(order1.Status == "Submitted")

#UC 12 test-1
def test_prepare_order_status(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    system1.Submit_Order(order1)
    assert(order1.Status == "Submitted")
    system1.Preparing_Order(order1)
    assert(order1.Status == "Preparing order")
#UC12 test 2
def test_complete_order_status(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    system1.Submit_Order(order1)
    assert(order1.Status == "Submitted")
    system1.Preparing_Order(order1)
    assert(order1.Status == "Preparing order")
    system1.Complete_Order(order1)
    assert(order1.Status == "Completed")

#UC 11 test-2
def test_submit_order_status(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    system1.Submit_Order(order1)
    assert(order1.Status == "Submitted")

#UC 12 test-1
def test_prepare_order_status(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    system1.Submit_Order(order1)
    assert(order1.Status == "Submitted")
    system1.Preparing_Order(order1)
    assert(order1.Status == "Preparing order")
#UC12 test 3
def test_complete_order_list(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    system1.Submit_Order(order1)
    assert(order1 in system1.View_Incomplete_Orders())
    assert(order1 not in system1.View_Complete_Orders())
    system1.Preparing_Order(order1)
    assert(order1 not in system1.View_Complete_Orders())
    assert(order1 in system1.View_Incomplete_Orders())
    system1.Complete_Order(order1)
    assert(order1 not in system1.View_Incomplete_Orders())
    assert(order1 in system1.View_Complete_Orders())
def test_complete_order_fail(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order= 1
    with pytest.raises(SystemError) as err:
        system1.Complete_Order(order)
    assert( err)