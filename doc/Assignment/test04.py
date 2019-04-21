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

#UC13 test 1
def test_viewStoc(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    assert(system1.Inventory == inventory_fixture)


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

#UC16 test2
def test_stock_decrease(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    origJ = inventory_fixture["apple juice"]
    order1 = system1.Create_Order()
    juice1 = order1.Create_Item("apple juice")
    juice1.Size = "small"
    order1.Add_To_Order(juice1)
    assert(inventory_fixture["apple juice"] == origJ-250)

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
    