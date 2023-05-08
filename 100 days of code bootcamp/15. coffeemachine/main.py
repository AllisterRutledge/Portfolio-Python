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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def check_resources(drink_request):
    """Returns True if there is enough resources for drink request or returns False if not."""
    enough_resources = True
    drink_ingredients = MENU[drink_request]['ingredients']
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}, try another order.")
            enough_resources = False
    return enough_resources


def process_coins():
    """Asks for number of coins and returns the sum of coins given."""
    print("Please insert coins.")
    total_coins = int(input("How many quarters?: ")) * 0.25
    total_coins += int(input("How many dimes?: ")) * 0.10
    total_coins += int(input("How many nickels?: ")) * 0.05
    total_coins += int(input("How many pennies?: ")) * 0.01
    return round(total_coins, 2)


def check_transaction(total_money, drink_request):
    """Returns True if total_money >= coffee order (and prints change value), but returns False if not."""
    order_cost = MENU[drink_request]["cost"]
    if total_money >= order_cost:
        global money
        money += order_cost
        change_due = round((total_money - order_cost), 2)
        if change_due > 0:
            print(f"Here is ${change_due} in change.")
        return True
    else:
        print("Sorry, insufficient funds. Money refunded.")
        return False


def make_coffee(drink_request):
    drink_ingredients = MENU[drink_request]['ingredients']
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink_request}. Enjoy!")


def place_order(drink_request):
    if check_resources(drink_request):
        user_money = process_coins()
        if check_transaction(user_money, drink_request):
            make_coffee(drink_request)


machine_on = True
while machine_on:
    user_request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_request == "off":
        machine_on = False
    elif user_request == "report":
        for material in resources:
            print(f"{material} : {resources[material]}")
        print(f"Money : ${money}")
    elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        place_order(user_request)
    else:
        print("Invalid input, try order again.")
