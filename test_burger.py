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
    }
    return Ingredient_costs

def test_valid_bun_types(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    assert(burg1.Bun_Type == "white")
    burg1.Bun_Type = "sesame"
    assert(burg1.Bun_Type == "sesame")

    try:
        burg1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid number of buns selected.")

def test_invalid_bun_type(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    try:
        burg1.Bun_Type = "black"
    except ItemError as err:
        assert(err.message == "Invalid bun type.")
    else:
        assert(False)

    try:
        burg1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid number of buns selected.")

def test_valid_bun_amount(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    assert(burg1.Bun_Type == "white")
    assert(burg1.Num_Buns == 0)
    
    orig_white_bun = inventory_fixture[burg1.Bun_Type]
    burg1.Add_Bun()
    assert(burg1.Num_Buns == 1)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 1))

    burg1.Add_Bun()
    assert(burg1.Num_Buns == 2)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 2))
    
    burg1.Add_Bun()
    assert(burg1.Num_Buns == 3)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 3))

    burg1.Add_Bun()
    assert(burg1.Num_Buns == 4)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 4))

    try:
        burg1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid number of patties selected.")

def test_invalid_bun_amount(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    assert(burg1.Bun_Type == "white")
    assert(burg1.Num_Buns == 0)
    
    orig_white_bun = inventory_fixture[burg1.Bun_Type]
    burg1.Add_Bun()
    assert(burg1.Num_Buns == 1)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 1))

    burg1.Add_Bun()
    assert(burg1.Num_Buns == 2)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 2))
    
    burg1.Add_Bun()
    assert(burg1.Num_Buns == 3)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 3))

    burg1.Add_Bun()
    assert(burg1.Num_Buns == 4)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 4))

    try:
        burg1.Add_Bun()
    except ItemError as err:
        assert(err.message == "A burger cannot have more than 4 buns.")
    else:
        assert(False)

    burg1.Remove_Bun()
    burg1.Remove_Bun()

    try:
        burg1.Remove_Bun()
    except ItemError as err:
        assert(err.message == "A burger cannot have less than 2 buns.")
    else:
        assert(False)
    
def test_change_bun_type(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    assert(burg1.Bun_Type == "white")
    assert(burg1.Num_Buns == 0)
    orig_white_bun = inventory_fixture[burg1.Bun_Type]

    burg1.Add_Bun()
    assert(burg1.Num_Buns == 1)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 1))

    burg1.Add_Bun()
    assert(burg1.Num_Buns == 2)
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun - 2))

    burg1.Bun_Type = "sesame"
    assert(inventory_fixture[burg1.Bun_Type] == (orig_white_bun))
    assert(burg1.Num_Buns == 0)

def test_bun_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["white"] = 2
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    assert(burg1.Num_Buns == 1)
    burg1.Add_Bun()
    assert(burg1.Num_Buns == 2)
    
    try:
        burg1.Add_Bun()
    except ItemError as err:
        assert(err.message == f"Not enough {burg1.Bun_Type} buns in stock.")
    else:
        assert(False)

def test_valid_patty_types(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Patty_Type = "beef"
    assert(burg1.Patty_Type == "beef")
    burg1.Patty_Type = "chicken"
    assert(burg1.Patty_Type == "chicken")

    try:
        burg1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid number of buns selected.")

def test_invalid_patty_type(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    try:
        burg1.Patty_Type = "wagyu"
    except ItemError as err:
        assert(err.message == "Invalid patty type.")
    else:
        assert(False)

    try:
        burg1.Check_Ingredients()
    except ItemError as err:
        assert(err.message == "Invalid number of buns selected.")

def test_valid_patty_amount(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    assert(burg1.Bun_Type == "white")
    burg1.Add_Bun()
    burg1.Add_Bun()
    assert(burg1.Num_Buns == 2)
    burg1.Patty_Type = "beef"
    assert(burg1.Patty_Type == "beef")
    assert(burg1.Num_Patties == 0)
    
    
    orig_beef = inventory_fixture[burg1.Patty_Type]
    burg1.Add_Patty()
    assert(burg1.Num_Patties == 1)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 1))

    burg1.Add_Patty()
    assert(burg1.Num_Patties == 2)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 2))
    
    burg1.Add_Patty()
    assert(burg1.Num_Patties == 3)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 3))

    assert(burg1.Check_Ingredients() == True)


def test_invalid_patty_amount(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Patty_Type = "beef"
    assert(burg1.Patty_Type == "beef")
    assert(burg1.Num_Patties == 0)
    
    orig_beef = inventory_fixture[burg1.Patty_Type]
    burg1.Add_Patty()
    assert(burg1.Num_Patties == 1)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 1))

    burg1.Add_Patty()
    assert(burg1.Num_Patties == 2)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 2))
    
    burg1.Add_Patty()
    assert(burg1.Num_Patties == 3)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 3))

    try:
        burg1.Add_Patty()
    except ItemError as err:
        assert(err.message == "A burger cannot have more than 3 patties.")
    else:
        assert(False)

    burg1.Remove_Patty()
    burg1.Remove_Patty()

    try:
        burg1.Remove_Patty()
    except ItemError as err:
        assert(err.message == "A burger cannot have less than 1 patty.")
    else:
        assert(False)
    
def test_change_patty_type(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Patty_Type = "beef"
    assert(burg1.Patty_Type == "beef")
    assert(burg1.Num_Patties == 0)
    orig_beef = inventory_fixture[burg1.Patty_Type]

    burg1.Add_Patty()
    assert(burg1.Num_Patties == 1)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 1))

    burg1.Add_Patty()
    assert(burg1.Num_Patties == 2)
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef - 2))

    burg1.Patty_Type = "chicken"
    assert(inventory_fixture[burg1.Patty_Type] == (orig_beef))
    assert(burg1.Num_Patties == 0)

def test_patty_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["beef"] = 2
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    assert(burg1.Num_Patties == 1)
    burg1.Add_Patty()
    assert(burg1.Num_Patties == 2)
    
    try:
        burg1.Add_Patty()
    except ItemError as err:
        assert(err.message == f"Not enough {burg1.Patty_Type} patties in stock.")
    else:
        assert(False)

def test_valid_other(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Add_Other("cheese")
    assert("cheese" in burg1.Other)
    burg1.Add_Other("lettuce")
    assert("lettuce" in burg1.Other)

def test_invalid_other(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    try:
        burg1.Add_Other("grape")
    except ItemError as err:
        assert(err.message == "Please select a valid ingredient.")
    else:
        assert(False)

def test_other_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["cheese"] = 2
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Add_Other("cheese")
    assert(burg1.Other.count("cheese") == 1)
    burg1.Add_Other("cheese")
    assert(burg1.Other.count("cheese") == 2)
    
    try:
        burg1.Add_Other("cheese")
    except ItemError as err:
        assert(err.message == f"Not enough cheese in stock.")
    else:
        assert(False)

def test_valid_burger(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")

    assert(burg1.Check_Ingredients() == True)

def test_check_calculate_cost(inventory_fixture, ingredient_cost_fixture):
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Patty()
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    burg1.Add_Other("lettuce")
    burg1.Add_Other("onion")
    burg1.Add_Other("tomato")
    burg1.Add_Other("avocado")

    assert(burg1.Calculate_Cost() == 31)

def test_check_clear_ingredients(inventory_fixture, ingredient_cost_fixture):
    orig_white_bun = inventory_fixture["white"]
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]
    orig_lettuce = inventory_fixture["lettuce"]
    orig_onion = inventory_fixture["onion"]
    orig_tomato = inventory_fixture["tomato"]
    orig_avocado = inventory_fixture["avocado"]
    
    burg1 = Burger(inventory_fixture, ingredient_cost_fixture)
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Patty()
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    burg1.Add_Other("lettuce")
    burg1.Add_Other("onion")
    burg1.Add_Other("tomato")
    burg1.Add_Other("avocado")

    assert((orig_white_bun - 4) == inventory_fixture["white"])
    assert((orig_beef - 3) == inventory_fixture["beef"])
    assert((orig_cheese - 1) == inventory_fixture["cheese"])
    assert((orig_lettuce - 1) == inventory_fixture["lettuce"])
    assert((orig_onion - 1) == inventory_fixture["onion"])
    assert((orig_tomato - 1) == inventory_fixture["tomato"])
    assert((orig_avocado - 1) == inventory_fixture["avocado"])

    burg1.Clear_Ingredients()

    assert(orig_white_bun == inventory_fixture["white"])
    assert(orig_beef == inventory_fixture["beef"])
    assert(orig_cheese == inventory_fixture["cheese"])
    assert(orig_lettuce == inventory_fixture["lettuce"])
    assert(orig_onion == inventory_fixture["onion"])
    assert(orig_tomato == inventory_fixture["tomato"])
    assert(orig_avocado == inventory_fixture["avocado"])