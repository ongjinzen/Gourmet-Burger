#test_sundae
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
        "sundae": 1000,
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


def test_order_sundae_small(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    orig_sundae = system1._Inventory["sundae"]
    orig_white_bun = system1._Inventory["white"]


    sundae1 = order1.Create_Item("sundae")
    sundae1.Size = "small"
    order1.Add_To_Order(sundae1)
    assert(sundae1 in order1.Items)
    assert(order1.Calculate_Cost() == 4)
    assert(system1.Inventory["sundae"] == (orig_sundae - 200))
    assert(system1.Inventory["white"] == (orig_white_bun))

def test_order_sundae_medium(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    orig_sundae = system1._Inventory["sundae"]
    orig_white_bun = system1._Inventory["white"]


    sundae1 = order1.Create_Item("sundae")
    sundae1.Size = "medium"
    order1.Add_To_Order(sundae1)
    assert(sundae1 in order1.Items)
    assert(order1.Calculate_Cost() == 6)
    assert(system1.Inventory["sundae"] == (orig_sundae - 400))
    assert(system1.Inventory["white"] == (orig_white_bun))

def test_order_sundae_large(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    orig_sundae = system1._Inventory["sundae"]
    orig_white_bun = system1._Inventory["white"]


    sundae1 = order1.Create_Item("sundae")
    sundae1.Size = "large"
    order1.Add_To_Order(sundae1)
    assert(sundae1 in order1.Items)
    assert(order1.Calculate_Cost() == 11)
    assert(system1.Inventory["sundae"] == (orig_sundae - 600))
    assert(system1.Inventory["white"] == (orig_white_bun))