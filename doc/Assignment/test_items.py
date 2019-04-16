import pytest

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
        "chocolate sundae": 1000,
        "strawberry sundae": 500,
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

# UC15 - Acceptance Criteria: 1
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

# UC3 - Acceptance Criteria: 1, 2
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

# UC3 - Acceptance Criteria: 1, 2
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

def test_valid_drink(inventory_fixture, ingredient_cost_fixture):
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")
    
    assert(drink1.Check_Ingredients() == True)

def test_check_calculate_cost(inventory_fixture, ingredient_cost_fixture):
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")

    assert(drink1.Calculate_Cost() == 3.5)

def test_clear_ingredients(inventory_fixture, ingredient_cost_fixture):
    orig_coke = inventory_fixture["coke"]
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")

    assert(inventory_fixture["coke"] == (orig_coke - 1))
    drink1.Clear_Ingredients()
    assert(inventory_fixture["coke"] == orig_coke)

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

def test_choc_sundae(inventory_fixture, ingredient_cost_fixture):
    orig_choc = inventory_fixture["chocolate sundae"]
    orig_white_bun = inventory_fixture["white"]


    choc1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "chocolate sundae")
    choc1.Size = "small"
    assert(choc1.Calculate_Cost() == 4)
    assert(inventory_fixture["chocolate sundae"] == (orig_choc - 200))
    assert(inventory_fixture["white"] == (orig_white_bun))

    choc1.Size = "medium"
    assert(choc1.Calculate_Cost() == 6)
    assert(inventory_fixture["chocolate sundae"] == (orig_choc - 400))
    assert(inventory_fixture["white"] == (orig_white_bun))

    choc1.Size = "large"
    assert(choc1.Calculate_Cost() == 11)
    assert(inventory_fixture["chocolate sundae"] == (orig_choc - 600))
    assert(inventory_fixture["white"] == (orig_white_bun))

def test_strawberry_no_stock(inventory_fixture, ingredient_cost_fixture):
    orig_strawberry = inventory_fixture["strawberry sundae"]
    orig_white_bun = inventory_fixture["white"]


    strawberry1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "strawberry sundae")
    strawberry1.Size = "small"
    assert(strawberry1.Calculate_Cost() == 4)
    assert(inventory_fixture["strawberry sundae"] == (orig_strawberry - 200))
    assert(inventory_fixture["white"] == (orig_white_bun))

    strawberry1.Size = "medium"
    assert(strawberry1.Calculate_Cost() == 6)
    assert(inventory_fixture["strawberry sundae"] == (orig_strawberry - 400))
    assert(inventory_fixture["white"] == (orig_white_bun))

    try:
        strawberry1.Size = "large"
    except ItemError as err:
        assert(err.message == "Not enough strawberry sundae in stock.")
    else:
        assert(False)