from data import MENU, resources


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True

is_on = True

while is_on:
    choice = input('Would you like an espresso/latte/cappuccino? ').lower()
    # Turns coffee maker off
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g')
    else:
        drink = MENU[choice]
        is_resource_sufficient(drink['ingredients'])
