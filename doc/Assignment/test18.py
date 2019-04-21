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

#UC 18 - test1 
def test_default(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    burg1 = order1.Create_Item( "Default Burger")
    assert(burg1.Bun_Type == "white")
    assert(burg1.Num_Buns == 2)
    assert(burg1.Num_Patties == 1)
    assert(burg1.Patty_Type == "beef")
    assert( "lettuce" in burg1.Other)
    assert( "tomato" not in burg1.Other)
#UC 18 test-2
def test_default_no_stock(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    system1.Inventory["lettuce"] = 0
    order1 = system1.Create_Order()
    with pytest.raises(ItemError) as err:
        burg1 = order1.Create_Item( "Default Burger")
    assert(err)

#UC 18 test-3
def test_default_cost(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))

    order1 = system1.Create_Order()
    
    burg1 = order1.Create_Item( "Default Burger")
    order1.Add_To_Order(burg1)
    assert(order1.Calculate_Cost() == 8)