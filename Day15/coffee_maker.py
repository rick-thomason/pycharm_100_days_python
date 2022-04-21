from data import MENU, resources

# TODO: 1. Print a report of the all the coffee machine resources
report = f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g'

is_off = False

# TODO: 2. Ask user what choice they would prefer
while not is_off:
    choice = input('Would you like an espresso/latte/cappuccino? ').lower()

    if choice == 'report':
        print(report)

    # Turns coffee maker off
    if choice == 'off':
        is_off = True



