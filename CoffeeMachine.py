MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resource(order_ingredients):
    """This function checks if enough ingredients are present and returns a boolean value"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def process_coins():
    """This function takes the inserted coins value and returns the total"""
    print("Please insert coins.")
    total = float(input("how many quarters?: ")) * 0.25
    total += float(input("how many dimes?: ")) * 0.10
    total += float(input("how many nickles?: ")) * 0.05
    total += float(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(user_payment, actual_value):
    """Returns true if payment is accepted, or False if insufficient funds"""
    if user_payment >= actual_value:
        change = round(user_payment - actual_value, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += actual_value
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False


def make_cofffee(user_drink, order_ingredients):
    """This function takes the customer's drink and ingredients as an input, makes the drink and updates the resources
    with depleted ingredients"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {user_drink}☕️. Enjoy!")


is_machine_on = True
while is_machine_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_machine_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if sufficient_resource(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_cofffee(choice, drink['ingredients'])
