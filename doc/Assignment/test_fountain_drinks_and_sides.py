from errors import ItemError
from item import *
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

# UC4 - Acceptance Criteria: 1, 2, 3, 4
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

# UC4 - Acceptance Criteria: 5
def test_invalid_item(inventory_fixture, ingredient_cost_fixture):

    try:
        juice1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "pear juice")
    except ItemError as err:
        assert(err.message == "Invalid item.")
    else:
        assert(False)

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

# UC16 - Acceptance Criteria: 2
def test_change_juice_size_and_cost(inventory_fixture, ingredient_cost_fixture):

    orig_orange = inventory_fixture["orange juice"]
    juice1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "orange juice")
    assert(inventory_fixture[juice1._Name] == (orig_orange))
    assert(juice1.Calculate_Cost() == 0)
    juice1.Size = "small"
    assert(inventory_fixture[juice1._Name] == (orig_orange - 250))
    assert(juice1.Calculate_Cost() == 2)
    juice1.Size = "medium"
    assert(inventory_fixture[juice1._Name] == (orig_orange - 500))
    assert(juice1.Calculate_Cost() == 3)
    assert(juice1.Check_Ingredients() == True)

def test_fries_sizes(inventory_fixture, ingredient_cost_fixture):
    
    fries1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "fries")
    
    try:
        fries1.Size = "large"
    except ItemError as err:
        assert(err.message == "Not enough fries in stock.")
    else:
        assert(False)

    fries1.Size = "small"
    assert(fries1.Size == "small")

def test_invalid_fries_size(inventory_fixture, ingredient_cost_fixture):

    fries1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "fries")
    
    try:
        fries1.Size = "extra large"
    except ItemError as err:
        assert(err.message == "Invalid size.")
    else:
        assert(False)

    try:
        fries1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid size.")

def test_change_fries_size_and_cost(inventory_fixture, ingredient_cost_fixture):

    orig_fries = inventory_fixture["fries"]
    fries1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "fries")
    assert(inventory_fixture[fries1._Name] == (orig_fries))
    assert(fries1.Calculate_Cost() == 0)
    fries1.Size = "small"
    assert(inventory_fixture[fries1._Name] == (orig_fries - 200))
    assert(fries1.Calculate_Cost() == 2)
    fries1.Size = "medium"
    assert(inventory_fixture[fries1._Name] == (orig_fries - 400))
    assert(fries1.Calculate_Cost() == 3)
    assert(fries1.Check_Ingredients() == True)

def test_nugget_sizes(inventory_fixture, ingredient_cost_fixture):
    
    nuggets1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "nuggets")
    
    try:
        nuggets1.Size = "large"
    except ItemError as err:
        assert(err.message == "Not enough nuggets in stock.")
    else:
        assert(False)

    nuggets1.Size = "small"
    assert(nuggets1.Size == "small")

def test_invalid_nugget_size(inventory_fixture, ingredient_cost_fixture):

    nuggets1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "nuggets")
    
    try:
        nuggets1.Size = "extra large"
    except ItemError as err:
        assert(err.message == "Invalid size.")
    else:
        assert(False)

    try:
        nuggets1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid size.")

# UC16 - Acceptance Criteria: 2
def test_change_nuggets_size_and_cost(inventory_fixture, ingredient_cost_fixture):

    orig_nuggets = inventory_fixture["nuggets"]
    nuggets1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "nuggets")
    assert(inventory_fixture[nuggets1._Name] == (orig_nuggets))
    assert(nuggets1.Calculate_Cost() == 0)
    nuggets1.Size = "small"
    assert(inventory_fixture[nuggets1._Name] == (orig_nuggets - 4))
    assert(nuggets1.Calculate_Cost() == 4)
    nuggets1.Size = "medium"
    assert(inventory_fixture[nuggets1._Name] == (orig_nuggets - 8))
    assert(nuggets1.Calculate_Cost() == 7)
    assert(nuggets1.Check_Ingredients() == True)

def test_clear_ingredients(inventory_fixture, ingredient_cost_fixture):
    orig_nuggets = inventory_fixture["nuggets"]
    nuggets1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "nuggets")
    assert(nuggets1.Calculate_Cost() == 0)
    nuggets1.Size = "small"
    assert(inventory_fixture[nuggets1._Name] == (orig_nuggets - 4))

    nuggets1.Clear_Ingredients()
    assert(inventory_fixture[nuggets1._Name] == (orig_nuggets))