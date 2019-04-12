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


def test_valid_order(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    orig_white_bun = system1._Inventory["white"]
    orig_beef = system1._Inventory["beef"]
    orig_cheese = system1._Inventory["cheese"]
    orig_tortilla = system1._Inventory["tortilla"]
    orig_tuna = system1._Inventory["tuna"]
    orig_lettuce = system1._Inventory["lettuce"]
    orig_onion = system1._Inventory["onion"]
    orig_tomato = system1._Inventory["tomato"]
    orig_avocado = system1._Inventory["avocado"]

    order1.Create_Item("Default Burger")
    assert(order1.Items != [])
    assert(order1.Calculate_Cost() == 8)

    

    assert(system1.Inventory["white"] == (orig_white_bun - 2))
    assert(system1.Inventory["beef"] == (orig_beef - 1))
    assert(system1.Inventory["cheese"] == (orig_cheese))
    assert(system1.Inventory["tortilla"] == (orig_tortilla ))
    assert(system1.Inventory["tuna"] == (orig_tuna ))
    assert(system1.Inventory["lettuce"] == (orig_lettuce - 1))
    assert(system1.Inventory["onion"] == (orig_onion ))
    assert(system1.Inventory["tomato"] == (orig_tomato ))
    assert(system1.Inventory["avocado"] == (orig_avocado))

    assert(order1.ID == None)
    assert(order1.Status == None)
    try:
        system1.Check_Status(0)
    except SystemError as err:
        assert(err.message == "Order not found.")
    else:
        assert(False)

   