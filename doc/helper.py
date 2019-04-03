#Go through list of ingredients and return a dictionary with the total amount of each ingrediant.
def IngrediantTotals(order):
    ingrediantCount = {}
    for item in order.Items:
        
            ingrediantCount[item] = order.Items.count(item)
            


    return ingrediantCount