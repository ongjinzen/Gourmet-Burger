from errors import ItemError
from Item import *
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

def test_valid_bottled_drink(inventory_fixture, ingredient_cost_fixture):
    orig_coke = inventory_fixture["coke"]
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")
    assert(drink1._Name == "coke")
    assert(inventory_fixture["coke"] == (orig_coke - 1))
    assert(drink1.Calculate_Cost() == 3.5)
    assert(drink1.Check_Ingredients() == True)

    orig_pepsi = inventory_fixture["pepsi"]
    drink2 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "pepsi")
    assert(drink2._Name == "pepsi")
    assert(inventory_fixture["pepsi"] == (orig_pepsi - 1))
    assert(drink2.Calculate_Cost() == 2.5)
    assert(drink2.Check_Ingredients() == True)

def test_invalid_drink_type(inventory_fixture, ingredient_cost_fixture):
    
    try:
        drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "mountain dew")
    except ItemError as err:
        assert(err.message == "Invalid drink.")
    else:
        assert(False)

def test_drink_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["coke"] = 0
    
    try:
        drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")
    except ItemError as err:
        assert(err.message == f"This drink is out of stock.")
    else:
        assert(False)

def test_valid_burger(inventory_fixture, ingredient_cost_fixture):
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")
    
    assert(drink1.Check_Ingredients() == True)

def test_check_calculate_cost(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture, [])
    wrap1.Wrap_Type = "tortilla"
    wrap1.Filling_Type = "tuna"
    wrap1.Add_Other("cheese")
    wrap1.Add_Other("lettuce")
    wrap1.Add_Other("onion")
    wrap1.Add_Other("tomato")
    wrap1.Add_Other("avocado")

    assert(wrap1.Calculate_Cost() == 29.5)