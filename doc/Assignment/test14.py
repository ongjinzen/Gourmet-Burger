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
    
# UC14 test 1
def test_stock_decrease(inventory_fixture, ingredient_cost_fixture):
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
    orig_pita= system1.Inventory["pita"]

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

    assert(system1.Inventory["white"] == (orig_white_bun - 2))
    assert(system1.Inventory["beef"] == (orig_beef - 1))
    assert(system1.Inventory["cheese"] == (orig_cheese - 2))
    assert(system1.Inventory["tortilla"] == (orig_tortilla - 1))
    assert(system1.Inventory["tuna"] == (orig_tuna - 1))
    assert(system1.Inventory["lettuce"] == (orig_lettuce - 1))
    assert(system1.Inventory["onion"] == (orig_onion - 1))
    assert(system1.Inventory["tomato"] == (orig_tomato - 1))
    assert(system1.Inventory["avocado"] == (orig_avocado - 1))
    assert(orig_pita==system1.Inventory["pita"])