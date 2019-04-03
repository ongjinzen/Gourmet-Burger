#test
from system import FoodSystem
import pytest


@pytest.fixture 
def system_fixture():
    food =  { "chips": 1, "coke" : 3, 'lettuce' : 5, 'wrap' : 6 ,'burger' : 7}
    menu =  {'chips': 1.00, 'coke' : 2.50, 'lettuce' : 4.50, 'wrap' : 3.45,'burger' : 10.00}
    system = FoodSystem(food,menu)
    #print(system)
    assert( system.ingredientsCost == menu)
    assert(system.inventory == food)
    return system

def test_new_stock(system_fixture):
    system_fixture.newStock('celery', 10000, 10.10)
    assert(system_fixture.ingredientsCost['celery'] == 10.10)
    assert(system_fixture.inventory['celery'] == 10000)