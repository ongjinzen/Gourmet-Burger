import pytest

from errors import SystemError
from order import Order
from system import System


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
        "sundae": 1000,
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

def test_create_system(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))

# UC11 - Acceptance Criteria: 1
# UC12 - Acceptance Criteria: 1, 2
# UC14 - Acceptance Criteria: 1
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

    assert(order1.ID == None)
    assert(order1.Status == None)
    try:
        system1.Check_Status(0)
    except SystemError as err:
        assert(err.message == "Order not found.")
    else:
        assert(False)

    system1.Submit_Order(order1)

    assert(order1.ID == 0)
    assert(order1 in system1.View_Incomplete_Orders())
    assert(system1.Check_Status(0) == "Submitted")

    system1.Preparing_Order(order1)

    assert(order1.ID == 0)
    assert(system1.Check_Status(0) == "Preparing order")
    assert(order1 in system1.View_Incomplete_Orders())

    system1.Complete_Order(order1)

    assert(order1.ID == 0)
    assert(system1.Check_Status(0) == "Completed")
    assert(order1 in system1.View_Complete_Orders())

def test_delete_order(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    assert(isinstance(order1, Order))

    orig_white_bun = system1.Inventory["white"]
    orig_beef = system1.Inventory["beef"]
    orig_cheese = system1.Inventory["cheese"]
    orig_tortilla = system1.Inventory["tortilla"]
    orig_tuna = system1.Inventory["tuna"]
    orig_lettuce = system1.Inventory["lettuce"]
    orig_onion = system1.Inventory["onion"]
    orig_tomato = system1.Inventory["tomato"]
    orig_avocado = system1.Inventory["avocado"]

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
    assert(wrap1 in order1.Items)
    assert(order1.Calculate_Cost() == 38.5)
    assert(len(order1.Items) == 2)

    assert(system1.Inventory["white"] == (orig_white_bun - 2))
    assert(system1.Inventory["beef"] == (orig_beef - 1))
    assert(system1.Inventory["cheese"] == (orig_cheese - 2))
    assert(system1.Inventory["tortilla"] == (orig_tortilla - 1))
    assert(system1.Inventory["tuna"] == (orig_tuna - 1))
    assert(system1.Inventory["lettuce"] == (orig_lettuce - 1))
    assert(system1.Inventory["onion"] == (orig_onion - 1))
    assert(system1.Inventory["tomato"] == (orig_tomato - 1))
    assert(system1.Inventory["avocado"] == (orig_avocado - 1))

    assert(order1.ID == None)
    assert(order1.Status == None)
    try:
        system1.Check_Status(0)
    except SystemError as err:
        assert(err.message == "Order not found.")
    else:
        assert(False)

    system1.Delete_Order(order1)
    assert(system1.Inventory["white"] == (orig_white_bun))
    assert(system1.Inventory["beef"] == (orig_beef))
    assert(system1.Inventory["cheese"] == (orig_cheese))
    assert(system1.Inventory["tortilla"] == (orig_tortilla))
    assert(system1.Inventory["tuna"] == (orig_tuna))
    assert(system1.Inventory["lettuce"] == (orig_lettuce))
    assert(system1.Inventory["onion"] == (orig_onion))
    assert(system1.Inventory["tomato"] == (orig_tomato))
    assert(system1.Inventory["avocado"] == (orig_avocado))

# UC5 - Acceptance Criteria: 4
def test_view_order(inventory_fixture, ingredient_cost_fixture):
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

    try:
        system1.View_Order(order1.ID)
    except SystemError as err:
        assert(err.message == "Order not found.")
    else:
        assert(False)

    system1.Submit_Order(order1)
    assert(system1.View_Order(order1.ID) == order1)

    system1.Preparing_Order(order1)
    assert(system1.View_Order(order1.ID) == order1)

    system1.Complete_Order(order1)
    assert(system1.View_Order(order1.ID) == order1)

def test_update_stock(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)
    orig_white_buns = system1.Inventory["white"]
    
    system1.Update_Stock("white", 5)
    assert(system1._Inventory["white"] == (orig_white_buns + 5))

    system1.Update_Stock("white", -10)
    assert(system1._Inventory["white"] == (orig_white_buns - 5))

def test_new_stock(inventory_fixture, ingredient_cost_fixture):
    system1 = System({}, {})

    assert(not("white" in system1.Inventory))

    system1.New_Stock("white", 1)

    assert(system1.Ingredient_Costs["white"] == 1)

# UC2 - Acceptance Criteria: 1
def test_view_menus(inventory_fixture, ingredient_cost_fixture):
    system1 = System(inventory_fixture, ingredient_cost_fixture)

    assert(system1.View_Main_Menu() == ["Burger", "Wrap"])
    assert(system1.View_Drink_Menu() == ["coke", "pepsi", "apple juice", "orange juice"])
    assert(system1.View_Side_Menu() == ["fries", "nuggets","sundaes"])

# UC5 - Acceptance Criteria: 1, 2
# UC9 - Acceptance Criteria: 1
def test_2_valid_order(inventory_fixture, ingredient_cost_fixture):


    system1 = System(inventory_fixture, ingredient_cost_fixture)
    assert(isinstance(system1, System))
    order1 = system1.Create_Order()
    order2 = system1.Create_Order()
    assert(isinstance(order1, Order))
    assert(isinstance(order2, Order))

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

    burg2 = order2.Create_Item("Burger")
    burg2.Bun_Type = "white"
    burg2.Add_Bun()
    burg2.Add_Bun()
    burg2.Patty_Type = "beef"
    burg2.Add_Patty()
    burg2.Add_Other("cheese")
    order2.Add_To_Order(burg2)
    assert(burg2 in order2.Items)
    assert(order2.Calculate_Cost() == 9)

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

    assert(inventory_fixture["white"] == (orig_white_bun - 4))
    assert(inventory_fixture["beef"] == (orig_beef - 2))
    assert(inventory_fixture["cheese"] == (orig_cheese - 3))
    assert(inventory_fixture["tortilla"] == (orig_tortilla - 1))
    assert(inventory_fixture["tuna"] == (orig_tuna - 1))
    assert(inventory_fixture["lettuce"] == (orig_lettuce - 1))
    assert(inventory_fixture["onion"] == (orig_onion - 1))
    assert(inventory_fixture["tomato"] == (orig_tomato - 1))
    assert(inventory_fixture["avocado"] == (orig_avocado - 1))

    assert(order1.ID == None)
    assert(order1.Status == None)
    try:
        system1.Check_Status(0)
    except SystemError as err:
        assert(err.message == "Order not found.")
    else:
        assert(False)

    system1.Submit_Order(order1)
    system1.Submit_Order(order2)
    assert(order1.ID == 0)
    assert(order2.ID == 1)
    assert(order1 in system1.View_Incomplete_Orders())
    assert(order2 in system1.View_Incomplete_Orders())
    assert(system1.Check_Status(0) == "Submitted")
    assert(system1.Check_Status(1) == "Submitted")

    system1.Preparing_Order(order1)

    assert(order1.ID == 0)
    assert(system1.Check_Status(0) == "Preparing order")
    assert(order1 in system1.View_Incomplete_Orders())

    system1.Preparing_Order(order2)

    assert(order2.ID == 1)
    assert(system1.Check_Status(1) == "Preparing order")
    assert(order2 in system1.View_Incomplete_Orders())

    system1.Complete_Order(order1)

    assert(order1.ID == 0)
    assert(system1.Check_Status(0) == "Completed")
    assert(order1 in system1.View_Complete_Orders())

    system1.Complete_Order(order2)

    assert(order2.ID == 1)
    assert(system1.Check_Status(0) == "Completed")
    assert(order2 in system1.View_Complete_Orders())
