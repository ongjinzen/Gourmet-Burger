import pytest

from errors import ItemError
from order import Order


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

def test_create_order(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

# UC2 - Acceptance Criteria: 2, 3
def test_create_and_add_item(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    orig_white_bun = inventory_fixture["white"]
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]

    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")

    assert(inventory_fixture["white"] == (orig_white_bun - 2))
    assert(inventory_fixture["beef"] == (orig_beef - 1))
    assert(inventory_fixture["cheese"] == (orig_cheese - 1))
    assert(order1.Calculate_Cost() == 0)

    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)

    assert(order1.Calculate_Cost() == 9)

def test_delete_item(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    orig_white_bun = inventory_fixture["white"]
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]

    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")

    assert(inventory_fixture["white"] == (orig_white_bun - 2))
    assert(inventory_fixture["beef"] == (orig_beef - 1))
    assert(inventory_fixture["cheese"] == (orig_cheese - 1))

    order1.Delete_Item(burg1)

    assert(inventory_fixture["white"] == (orig_white_bun))
    assert(inventory_fixture["beef"] == (orig_beef))
    assert(inventory_fixture["cheese"] == (orig_cheese))

# UC7 - Acceptance Criteria: 2, 3, 4
def test_remove_from_order(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    orig_white_bun = inventory_fixture["white"]
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]

    burg1 = order1.Create_Item("Burger")
    burg1.Bun_Type = "white"
    burg1.Add_Bun()
    burg1.Add_Bun()
    burg1.Patty_Type = "beef"
    burg1.Add_Patty()
    burg1.Add_Other("cheese")

    assert(inventory_fixture["white"] == (orig_white_bun - 2))
    assert(inventory_fixture["beef"] == (orig_beef - 1))
    assert(inventory_fixture["cheese"] == (orig_cheese - 1))
    assert(order1.Calculate_Cost() == 0)
    

    order1.Add_To_Order(burg1)
    assert(burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 9)

    order1.Remove_From_Order(burg1)
    assert(not(burg1 in order1.Items))
    assert(inventory_fixture["white"] == (orig_white_bun))
    assert(inventory_fixture["beef"] == (orig_beef))
    assert(inventory_fixture["cheese"] == (orig_cheese))
    assert(order1.Calculate_Cost() == 0)

def test_multiple_items(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    orig_white_bun = inventory_fixture["white"]
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]
    orig_tortilla = inventory_fixture["tortilla"]
    orig_tuna = inventory_fixture["tuna"]
    orig_lettuce = inventory_fixture["lettuce"]
    orig_onion = inventory_fixture["onion"]
    orig_tomato = inventory_fixture["tomato"]
    orig_avocado = inventory_fixture["avocado"]

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

    assert(inventory_fixture["white"] == (orig_white_bun - 2))
    assert(inventory_fixture["beef"] == (orig_beef - 1))
    assert(inventory_fixture["cheese"] == (orig_cheese - 2))
    assert(inventory_fixture["tortilla"] == (orig_tortilla - 1))
    assert(inventory_fixture["tuna"] == (orig_tuna - 1))
    assert(inventory_fixture["lettuce"] == (orig_lettuce - 1))
    assert(inventory_fixture["onion"] == (orig_onion - 1))
    assert(inventory_fixture["tomato"] == (orig_tomato - 1))
    assert(inventory_fixture["avocado"] == (orig_avocado - 1))

def test_invalid_item(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    drink1 = order1.Create_Item("apple juice")
    
    try:
        drink1.Size = "extra large"
    except ItemError as err:
        assert(err.message == "Invalid size.")
    else:
        assert(False)

    try:
        drink1.Size = "medium"
    except ItemError as err:
        assert(err.message == "Not enough apple juice in stock.")
    else:
        assert(False)

    drink1.Size = "small"
    assert(drink1.Size == "small")

def test_sides(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    fries1 = order1.Create_Item("fries")
    fries1.Size = "medium"
    order1.Add_To_Order(fries1)
    assert(fries1 in order1.Items)
    assert(order1.Calculate_Cost() == 3)

    nuggets1 = order1.Create_Item("nuggets")
    nuggets1.Size = "medium"
    order1.Add_To_Order(nuggets1)
    assert(nuggets1 in order1.Items)
    assert(order1.Calculate_Cost() == 10)

def test_add_invalid_order(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))
    burg1 = order1.Create_Item("Burger")

    try:
        order1.Add_To_Order(burg1)
    except ItemError as err:
        assert(err.message == "Invalid number of buns selected.")
    else:
        assert(False)

def test_default_burger(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    orig_white_bun = inventory_fixture["white"]
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]
    orig_tortilla = inventory_fixture["tortilla"]
    orig_tuna = inventory_fixture["tuna"]
    orig_lettuce = inventory_fixture["lettuce"]
    orig_onion = inventory_fixture["onion"]
    orig_tomato = inventory_fixture["tomato"]
    orig_avocado = inventory_fixture["avocado"]

    def_burg1 = order1.Create_Item("Default Burger")
    order1.Add_To_Order(def_burg1)
    assert(def_burg1 in order1.Items)
    assert(order1.Calculate_Cost() == 8)

    

    assert(inventory_fixture["white"] == (orig_white_bun - 2))
    assert(inventory_fixture["beef"] == (orig_beef - 1))
    assert(inventory_fixture["cheese"] == (orig_cheese))
    assert(inventory_fixture["tortilla"] == (orig_tortilla))
    assert(inventory_fixture["tuna"] == (orig_tuna))
    assert(inventory_fixture["lettuce"] == (orig_lettuce - 1))
    assert(inventory_fixture["onion"] == (orig_onion))
    assert(inventory_fixture["tomato"] == (orig_tomato))
    assert(inventory_fixture["avocado"] == (orig_avocado))

    assert(order1.ID == None)
    assert(order1.Status == None)

def test_default_burger_no_stock(inventory_fixture, ingredient_cost_fixture):
    order1 = Order(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(order1, Order))

    orig_white_bun = inventory_fixture["white"] = 0
    orig_beef = inventory_fixture["beef"]
    orig_cheese = inventory_fixture["cheese"]
    orig_tortilla = inventory_fixture["tortilla"]
    orig_tuna = inventory_fixture["tuna"]
    orig_lettuce = inventory_fixture["lettuce"]
    orig_onion = inventory_fixture["onion"]
    orig_tomato = inventory_fixture["tomato"]
    orig_avocado = inventory_fixture["avocado"]

    try:
        def_burg1 = order1.Create_Item("Default Burger")
    except ItemError as err:
        assert(err.message == "Not enough white buns in stock.")
    else:
        assert(False)
    assert(order1.Calculate_Cost() == 0)

    

    assert(inventory_fixture["white"] == (orig_white_bun))
    assert(inventory_fixture["beef"] == (orig_beef))
    assert(inventory_fixture["cheese"] == (orig_cheese))
    assert(inventory_fixture["tortilla"] == (orig_tortilla))
    assert(inventory_fixture["tuna"] == (orig_tuna))
    assert(inventory_fixture["lettuce"] == (orig_lettuce))
    assert(inventory_fixture["onion"] == (orig_onion))
    assert(inventory_fixture["tomato"] == (orig_tomato))
    assert(inventory_fixture["avocado"] == (orig_avocado))

    assert(order1.ID == None)
    assert(order1.Status == None)