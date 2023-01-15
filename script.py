# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# Output
# 3

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")
# Output
# We sell 7 different kinds of pizza!

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
# Output
# [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

pizza_and_prices.sort()
print(pizza_and_prices)
# Output
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
# Output
# [1, 'cheese']

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# Output
# [7, 'anchovies']

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
# Output
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]
# [7, 'anchovies']

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
# Output
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives']]




















