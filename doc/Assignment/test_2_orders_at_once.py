from errors import *
from system import System
from order import Order
import pytest

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



def test_2_valid_order(inventory_fixture, ingredient_cost_fixture):


    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    order2 = system1.Create_Order()
    assert(isinstance(order1, Order))
    assert(isinstance(order2, Order))

    orig_white_bun = inventory_fixture["white"]
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]
    orig_tortilla = inventory_fixture["tortilla"]
    orig_tuna = inventory_fixture["tuna"]
    orig_lettuce = inventory_fixture["lettuce"]
    orig_onion = inventory_fixture["onion"]
    orig_tomato = inventory_fixture["tomato"]
    orig_avocado = inventory_fixture["avocado"]

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

    burg2 = order2.Create_Item("Burger")
    burg2.Bun_Type = "white"
    burg2.Add_Bun()
    burg2.Add_Bun()
    burg2.Patty_Type = "beef"
    burg2.Add_Patty()
    burg2.Add_Other("cheese")
    order2.Add_To_Order(burg2)
    assert(burg2 in order2.Items)
    assert(order2.Calculate_Cost() == 9)

    wrap1 = order1.Create_Item("Wrap")
    wrap1.Wrap_Type = "tortilla"
    wrap1.Filling_Type = "tuna"
    wrap1.Add_Other("cheese")
    wrap1.Add_Other("lettuce")
    wrap1.Add_Other("onion")
    wrap1.Add_Other("tomato")
    wrap1.Add_Other("avocado")
    order1.Add_To_Order(wrap1)
    assert(order1.Calculate_Cost() == 38.5)

    assert(inventory_fixture["white"] == (orig_white_bun - 4))
    assert(inventory_fixture["beef"] == (orig_beef - 2))
    assert(inventory_fixture["cheese"] == (orig_cheese - 3))
    assert(inventory_fixture["tortilla"] == (orig_tortilla - 1))
    assert(inventory_fixture["tuna"] == (orig_tuna - 1))
    assert(inventory_fixture["lettuce"] == (orig_lettuce - 1))
    assert(inventory_fixture["onion"] == (orig_onion - 1))
    assert(inventory_fixture["tomato"] == (orig_tomato - 1))
    assert(inventory_fixture["avocado"] == (orig_avocado - 1))

    assert(order1.ID == None)
    assert(order1.Status == None)
    try:
        system1.Check_Status(0)
    except SystemError as err:
        assert(err.message == "Order not found.")
    else:
        assert(False)

    system1.Submit_Order(order1)
    system1.Submit_Order(order2)
    assert(order1.ID == 0)
    assert(order2.ID == 1)
    assert(order1 in system1.View_Incomplete_Orders())
    assert(order2 in system1.View_Incomplete_Orders())
    assert(system1.Check_Status(0) == "Submitted")
    assert(system1.Check_Status(1) == "Submitted")

    system1.Preparing_Order(order1)

    assert(order1.ID == 0)
    assert(system1.Check_Status(0) == "Preparing order")
    assert(order1 in system1.View_Incomplete_Orders())

    system1.Preparing_Order(order2)

    assert(order2.ID == 1)
    assert(system1.Check_Status(1) == "Preparing order")
    assert(order2 in system1.View_Incomplete_Orders())

    system1.Complete_Order(order1)

    assert(order1.ID == 0)
    assert(system1.Check_Status(0) == "Completed")
    assert(order1 in system1.View_Complete_Orders())



