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
#UC 2 Testing
#UC2 test-1 
def test_Menus(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    assert(system1.View_Drink_Menu() == ["coke", "pepsi", "apple juice", "orange juice"])
    assert(system1.View_Main_Menu() == ["Burger", "Wrap","Default Burger"])
    assert(system1.View_Side_Menu() == ["fries", "nuggets", "chocolate sundae", "strawberry sundae"])
#UC2 test-3 
#UC2 test-4
def test_valid_order(inventory_fixture, ingredient_cost_fixture):
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
    orig_pita = system1._Inventory["pita"]

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
    assert(system1.Inventory["pita"] == (orig_pita))

#UC 3 Testing
#UC 3test-1
def test_add_ingredients(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))


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

#UC 3 test-2
def test_add_to_many_ingredients(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    with pytest.raises(Exception) as err:
        burg1 = order1.Create_Item("Burger")
        burg1.Bun_Type = "white"
        burg1.Add_Bun()
        burg1.Add_Bun()
        burg1.Patty_Type = "beef"
        burg1.Add_Patty()
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
        burg1.Add_Other("cheese")
    order1.Add_To_Order(burg1)
    assert( err != [] ) 
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 27)
#UC 3 test 4
def test_take_away_ingrediets(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    
    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")
    burg1.Remove_Other("cheese")
    order1.Add_To_Order(burg1)
    
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 7)
#UC4  - test6
def test_invalid_drink_type(inventory_fixture, ingredient_cost_fixture):
    
    try:
        drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "mountain dew")
    except ItemError as err:
        assert(err.message == "Invalid drink.")
    else:
        assert(False)
# UC4 - test 9
def test_drink_no_stock(inventory_fixture, ingredient_cost_fixture):
    inventory_fixture["coke"] = 0
    
    try:
        drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")
    except ItemError as err:
        assert(err.message == f"This drink is out of stock.")
    else:
        assert(False)
# UC4 - test 6
def test_valid_drink(inventory_fixture, ingredient_cost_fixture):
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")
    
    assert(drink1.Check_Ingredients() == True)
# UC4 - test 8
def test_check_calculate_cost(inventory_fixture, ingredient_cost_fixture):
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")

    assert(drink1.Calculate_Cost() == 3.5)
# UC4 - test 7
def test_clear_ingredients(inventory_fixture, ingredient_cost_fixture):
    orig_coke = inventory_fixture["coke"]
    drink1 = Bottled_Drink(inventory_fixture, ingredient_cost_fixture, "coke")

    assert(inventory_fixture["coke"] == (orig_coke - 1))
    drink1.Clear_Ingredients()
    assert(inventory_fixture["coke"] == orig_coke)

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

# test 6
def test_invalid_item(inventory_fixture, ingredient_cost_fixture):

    try:
        juice1 = Fountain_Drinks_and_Sides(inventory_fixture, ingredient_cost_fixture, "pear juice")
    except ItemError as err:
        assert(err.message == "Invalid item.")
    else:
        assert(False)
#test 5
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





