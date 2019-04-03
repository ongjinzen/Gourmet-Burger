#test
from system import FoodSystem
def test_initialise():
    food =  { "chips": 1, "coke" : 3, 'lettuce' : 5, 'wrap' : 6 ,'burger' : 7}
    menu =  {'chips': 1.00, 'coke' : 2.50, 'lettuce' : 4.50, 'wrap' : 3.45,'burger' : 10.00}
    system = FoodSystem(food,menu)
    print(system)
    assert( system.ingredientsCost == menu)
    assert(system.inventory == food)
    pass
