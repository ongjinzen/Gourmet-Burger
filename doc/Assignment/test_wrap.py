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
    }
    return Ingredient_costs

def test_valid_wrap_types(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Wrap_Type = "tortilla"
    assert(wrap1.Wrap_Type == "tortilla")
    wrap1.Wrap_Type = "pita"
    assert(wrap1.Wrap_Type == "pita")

    try:
        wrap1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "No filling selected.")

def test_invalid_wrap_type(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    try:
        wrap1.Wrap_Type = "black"
    except ItemError as err:
        assert(err.message == "Invalid wrap type.")
    else:
        assert(False)

    try:
        wrap1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "No wrap selected.")

def test_change_wrap_type(inventory_fixture, ingredient_cost_fixture):
    orig_tortilla = inventory_fixture["tortilla"]
    orig_pita = inventory_fixture["pita"]
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Wrap_Type = "tortilla"
    assert(inventory_fixture["tortilla"] == (orig_tortilla - 1))
    assert(inventory_fixture["pita"] == (orig_pita))

    wrap1.Wrap_Type = "pita"
    assert(inventory_fixture["tortilla"] == (orig_tortilla))
    assert(inventory_fixture["pita"] == (orig_pita - 1))

def test_wrap_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["pita"] = 0
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    
    try:
        wrap1.Wrap_Type = "pita"
    except ItemError as err:
        assert(err.message == f"Not enough pita wraps in stock.")
    else:
        assert(False)
    
    wrap1.Wrap_Type = "tortilla"
    assert(wrap1.Wrap_Type == "tortilla")

def test_valid_filling_types(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Filling_Type = "pork"
    assert(wrap1.Filling_Type == "pork")
    wrap1.Filling_Type = "tuna"
    assert(wrap1.Filling_Type == "tuna")

    wrap1.Wrap_Type = "tortilla"
    wrap1.Check_Ingredients()
    assert(wrap1.Check_Ingredients() == True)

def test_invalid_patty_type(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    try:
        wrap1.Filling_Type = "wagyu"
    except ItemError as err:
        assert(err.message == "Invalid filling type.")
    else:
        assert(False)

    try:
        wrap1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "No wrap selected.")

def test_change_filling_type(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    orig_tuna = inventory_fixture["tuna"]
    orig_pork = inventory_fixture["pork"]
    wrap1.Filling_Type = "tuna"
    assert(wrap1.Filling_Type == "tuna")
    assert(inventory_fixture[wrap1.Filling_Type] == (orig_tuna - 1))
    assert(inventory_fixture["pork"] == orig_pork)

    wrap1.Filling_Type = "pork"
    assert(wrap1.Filling_Type == "pork")
    assert(inventory_fixture["tuna"] == orig_tuna)
    assert(inventory_fixture[wrap1.Filling_Type] == (orig_pork - 1))


def test_filling_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["tuna"] = 0
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    
    try:
        wrap1.Filling_Type = "tuna"
    except ItemError as err:
        assert(err.message == f"Not enough tuna filling in stock.")
    else:
        assert(False)

    assert(wrap1.Filling_Type == None)
    orig_pork = inventory_fixture["pork"]
    wrap1.Filling_Type = "pork"
    assert(wrap1.Filling_Type == "pork")
    assert(inventory_fixture[wrap1.Filling_Type] == (orig_pork - 1))

def test_valid_other(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Add_Other("cheese")
    assert("cheese" in wrap1.Other)
    wrap1.Add_Other("lettuce")
    assert("lettuce" in wrap1.Other)

def test_invalid_other(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    try:
        wrap1.Add_Other("grape")
    except ItemError as err:
        assert(err.message == "Please select a valid ingredient.")
    else:
        assert(False)

def test_other_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["cheese"] = 2
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Add_Other("cheese")
    assert(wrap1.Other.count("cheese") == 1)
    wrap1.Add_Other("cheese")
    assert(wrap1.Other.count("cheese") == 2)
    
    try:
        wrap1.Add_Other("cheese")
    except ItemError as err:
        assert(err.message == f"Not enough cheese in stock.")
    else:
        assert(False)

def test_valid_wrap(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Wrap_Type = "pita"
    wrap1.Filling_Type = "tuna"
    wrap1.Add_Other("cheese")

    assert(wrap1.Check_Ingredients() == True)

def test_check_calculate_cost(inventory_fixture, ingredient_cost_fixture):
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Wrap_Type = "tortilla"
    wrap1.Filling_Type = "tuna"
    wrap1.Add_Other("cheese")
    wrap1.Add_Other("lettuce")
    wrap1.Add_Other("onion")
    wrap1.Add_Other("tomato")
    wrap1.Add_Other("avocado")

    assert(wrap1.Calculate_Cost() == 29.5)

def test_check_clear_ingredients(inventory_fixture, ingredient_cost_fixture):
    orig_pita = inventory_fixture["pita"]
    orig_pork = inventory_fixture["pork"]
    orig_cheese = inventory_fixture["cheese"]
    orig_lettuce = inventory_fixture["lettuce"]
    orig_onion = inventory_fixture["onion"]
    orig_tomato = inventory_fixture["tomato"]
    orig_avocado = inventory_fixture["avocado"]
    
    wrap1 = Wrap(inventory_fixture, ingredient_cost_fixture)
    wrap1.Wrap_Type = "pita"
    wrap1.Filling_Type = "pork"
    wrap1.Add_Other("cheese")
    wrap1.Add_Other("lettuce")
    wrap1.Add_Other("onion")
    wrap1.Add_Other("tomato")
    wrap1.Add_Other("avocado")

    assert((orig_pita - 1) == inventory_fixture["pita"])
    assert((orig_pork - 1) == inventory_fixture["pork"])
    assert((orig_cheese - 1) == inventory_fixture["cheese"])
    assert((orig_lettuce - 1) == inventory_fixture["lettuce"])
    assert((orig_onion - 1) == inventory_fixture["onion"])
    assert((orig_tomato - 1) == inventory_fixture["tomato"])
    assert((orig_avocado - 1) == inventory_fixture["avocado"])

    wrap1.Clear_Ingredients()

    assert(orig_pita == inventory_fixture["pita"])
    assert(orig_pork == inventory_fixture["pork"])
    assert(orig_cheese == inventory_fixture["cheese"])
    assert(orig_lettuce == inventory_fixture["lettuce"])
    assert(orig_onion == inventory_fixture["onion"])
    assert(orig_tomato == inventory_fixture["tomato"])
    assert(orig_avocado == inventory_fixture["avocado"])