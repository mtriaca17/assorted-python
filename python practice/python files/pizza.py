def make_pizza(size, *toppings):
    """summarize pizza to be made"""
    print(f'Making a {size} -inch pizza with toppings')
    for topping in toppings:
        print(f'- {topping}')
