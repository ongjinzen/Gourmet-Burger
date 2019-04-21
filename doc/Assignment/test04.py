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
    
# UC4 - test 1,2,3
def test_juice_sizes(inventory_fixture, ingredient_cost_fixture):
    
    juice1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "apple juice")
    
    try:
        juice1.Size = "medium"
    except ItemError as err:
        assert(err.message == "Not enough apple juice in stock.")
    else:
        assert(False)

    juice1.Size = "small"
    assert(juice1.Size == "small")
    inventory_fixture["apple juice"] = 10000
    juice1.Size = "large"
    assert(juice1.Size == "large")

#UC 4 test-4
def test_Multiple_drinks(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))
    juice1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "apple juice")
    juice1.Size = "small"
    inventory_fixture["apple juice"] = 10000
    juice2 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "apple juice")
    juice2.Size = "medium"
    juice3 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "apple juice")
    juice3.Size = "large"
    order1.Add_To_Order(juice1)
    order1.Add_To_Order(juice2)
    order1.Add_To_Order(juice3)
    assert(juice1 in order1.Items)
    assert(juice2 in order1.Items)
    assert(juice3 in order1.Items)

#UC4 -test 5
def test_invalid_juice_size(inventory_fixture, ingredient_cost_fixture):

    juice1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "apple juice")
    
    try:
        juice1.Size = "extra large"
    except ItemError as err:
        assert(err.message == "Invalid size.")
    else:
        assert(False)

    try:
        juice1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid size.")

#UC4 -test 6
def test_invalid_item(inventory_fixture, ingredient_cost_fixture):

    try:
        juice1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "pear juice")
    except ItemError as err:
        assert(err.message == "Invalid item.")
    else:
        assert(False)

# UC4 - test 6
def test_valid_drink(inventory_fixture, ingredient_cost_fixture):
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")

# UC4 - test 7
def test_clear_ingredients(inventory_fixture, ingredient_cost_fixture):
    orig_coke = inventory_fixture["coke"]
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")

    assert(inventory_fixture["coke"] == (orig_coke - 1))
    drink1.Clear_Ingredients()
    assert(inventory_fixture["coke"] == orig_coke)

# UC4 - test 8
def test_check_calculate_cost(inventory_fixture, ingredient_cost_fixture):
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")

    assert(drink1.Calculate_Cost() == 3.5)

# UC4 - test 9
def test_drink_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["coke"] = 0
    
    try:
        drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")
    except ItemError as err:
        assert(err.message == f"This drink is out of stock.")
    else:
        assert(False)