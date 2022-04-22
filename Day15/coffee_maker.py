from data import MENU, resources

profit = 0

is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns if there is sufficient resources."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins.')
    total = int(input('How many quarters? ')) * 0.25
    total += int(input('How many dimes? ')) * 0.1
    total += int(input('How many nickels? ')) * 0.05
    total += int(input('How many pennies? ')) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is successful, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry that is not enough money. Money Refunded.')
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕️. Enjoy')


while is_on:
    choice = input('Would you like an espresso/latte/cappuccino? ').lower()
    # Turns coffee maker off
    if choice == 'off':
        is_on = False
        print('You have turned off the coffee maker.')
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}')
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

