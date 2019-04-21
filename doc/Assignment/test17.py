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

#UC17 test1
def test_strawberry(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    orig = inventory_fixture["strawberry sundae"]
    order1 = system1.Create_Order()
    sun = order1.Create_Item("strawberry sundae")
    sun.Size = "small"
    order1.Add_To_Order(sun)
    assert(inventory_fixture["strawberry sundae"] == orig-200)

#UC17 test2
def test_chocolate(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    orig = inventory_fixture["chocolate sundae"]
    order1 = system1.Create_Order()
    sun = order1.Create_Item("chocolate sundae")
    sun.Size = "small"
    order1.Add_To_Order(sun)
    assert(inventory_fixture["chocolate sundae"] == orig-200)

#UC17 test3,4,5
def test_chocolate_sizes(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    inventory_fixture["chocolate sundae"] = 10000
    orig = inventory_fixture["chocolate sundae"]
    order1 = system1.Create_Order()
    sun = order1.Create_Item("chocolate sundae")
    sun.Size = "small"
    order1.Add_To_Order(sun)
    assert(inventory_fixture["chocolate sundae"] == orig-200)
    assert(order1.Calculate_Cost()== 4)
    inventory_fixture["chocolate sundae"] = 10000
    orig = inventory_fixture["chocolate sundae"]
    
    sun2 = order1.Create_Item("chocolate sundae")
    sun2.Size = "medium"
    order1.Add_To_Order(sun2)
    assert(inventory_fixture["chocolate sundae"] == orig-400)
    assert(order1.Calculate_Cost()== 10)
    inventory_fixture["chocolate sundae"] = 10000
    orig = inventory_fixture["chocolate sundae"]
    
    sun3 = order1.Create_Item("chocolate sundae")
    sun3.Size = "large"
    order1.Add_To_Order(sun3)
    assert(inventory_fixture["chocolate sundae"] == orig-600)
    assert(order1.Calculate_Cost()== 21)