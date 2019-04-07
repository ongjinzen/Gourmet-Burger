from system import System

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

system1 = System(Inventory, Ingredient_costs)
print(system1)

order1 = system1.Create_Order()

burg1 = order1.Create_Item("Burger")
burg1.Bun_Type = "white"
burg1.Add_Bun()
burg1.Add_Bun()
burg1.Patty_Type = "beef"
burg1.Add_Patty()
burg1.Add_Other("cheese")
print(f"burg1 costs {burg1.Calculate_Cost()}")
order1.Add_To_Order(burg1)
print(f"order1 costs {order1.Calculate_Cost()}\n")
system1.Submit_Order(order1)

print(system1)

system1.Preparing_Order(order1)

print(f"The status of order 1 is: {(system1.Check_Status(order1.ID))}")

system1.Complete_Order(order1)
print(f"The status of order 1 is: {(system1.Check_Status(order1.ID))}")
print(system1)