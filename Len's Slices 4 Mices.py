# Let's start with a greeting
print("Welcome to Len's Slices 4 Mices!")

# List of pizza's offered
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# List of price by pizza type
prices = [2, 6, 1, 3, 2, 7, 2]

# What if we have completely ran out of toppings or there are no prices listed?
if not toppings or not prices:
    print("Error: No toppings or prices available!")
    exit()

# How many $2 slices are on the menu
num_two_dollar_slices = prices.count(2)

# How many pizza types are on the menu
num_pizzas = len(toppings)

# Time to advertise
print(f'We sell {num_pizzas} different kinds of pizza! \n')

# Let's simplify the listings into a 2-dimensional list | I first manually input, but discovered zip()
pizza_and_prices = zip(prices, toppings)
pizza_and_prices = list(pizza_and_prices)

# Let's make sure every pizza has a price
if len(pizza_and_prices) != num_pizzas:
    print('Error: The number of pizzas does not match the number of prices!')

# Let's ensure we aren't paying people to eat our pizza
if any(price < 0 for price in prices):
    print("Error: We don't pay you to eat our pizza!")

# Clean up the menu by sorting by price
pizza_and_prices.sort()

# Oh no! We ran out of anchovies, thankfully we have some peppers in the back room
pizza_and_prices.pop()
pizza_and_prices.append((2.5, 'peppers'))

# Let's ensure our menu is still sorted properly after making these changes
pizza_and_prices.sort()

# Let's validate before categorizing
if not pizza_and_prices:
    print("No pizzas currently available! We apologize for the inconvenience, but will have more in stock soon.")
else:
    # Always safe operations
    cheapest_pizza = pizza_and_prices[0]
    priciest_pizza = pizza_and_prices[-1]
    
    # Let's do some formatting and print out the full menu. I am running some risk here though if there are not exatly 7 pizzas
    full_menu = (f'Our Full Menu: \n' 
        f'\t{pizza_and_prices[0][1]}\t\t${pizza_and_prices[0][0]} per slice, \n'
        f'\t{pizza_and_prices[1][1]}\t${pizza_and_prices[1][0]} per slice, \n'
        f'\t{pizza_and_prices[2][1]}\t\t${pizza_and_prices[2][0]} per slice, \n'
        f'\t{pizza_and_prices[3][1]}\t${pizza_and_prices[3][0]} per slice, \n'
        f'\t{pizza_and_prices[4][1]}\t\t${pizza_and_prices[4][0]} per slice, \n'
        f'\t{pizza_and_prices[5][1]}\t\t${pizza_and_prices[5][0]} per slice, \n'
        f'\t{pizza_and_prices[6][1]}\t${pizza_and_prices[6][0]} per slice, \n')
    # I know I can fix this with a for loop, but I am trying to focus on the logic of lists and tuples here


    print(full_menu)
    print(f'For those who watch their weight and their wallet: \n'
    f'\t{cheapest_pizza[1]} for ${cheapest_pizza[0]} per slice\n')
    print(f'For those who only want the finer things in life (without going to Hawaii): \n'
    f'\t{priciest_pizza[1]} for ${priciest_pizza[0]} per slice\n')
    
    # Only show special if we have enough pizzas
    if len(pizza_and_prices) >= 3:
        three_cheapest = pizza_and_prices[:3]
        special_of_the_day = (f'Special of the day "Three Blind Mice!": \n'
            f'\t{three_cheapest[0][1]} for ${three_cheapest[0][0]} per slice, \n'
            f'\t{three_cheapest[1][1]} for ${three_cheapest[1][0]} per slice, \n'
            f'\tand {three_cheapest[2][1]} for ${three_cheapest[2][0]} per slice. \n'
            f'Special price of $4 for all three slices!')
        print(special_of_the_day)
    else:
        print("Sorry, not enough variety for our 'Three Blind Mice' special today!")
