from difflib import get_close_matches

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
    "water": 1300,
    "milk": 800,
    "coffee": 300,
    "money": 0,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01

}


def print_report():
    """
Prints out a report for the remaining resources in the coffee machine
    """
    for key, value in resources.items():
        print(key.capitalize() + ": " + str(value) + "ml")
        if key == "milk":
            break

    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))


def check_sufficiency(order):
    """
    Checks if there are enough ingredients to execute the order
    """

    is_sufficient = True
    for key, value in MENU[order]["ingredients"].items():
        if resources[key] < value:
            is_sufficient = False
            break

    if not is_sufficient:
        print("Sorry there is not enough {}".format(key))

    return is_sufficient


def insert_coins():
    """
    Takes in the user's input by coin types and returns the sum.
    """
    sum_of_coins = 0
    for key, value in coins.items():
        count = int(input("How many {}?".format(key)))
        sum_of_coins += count * value
    return sum_of_coins


def check_transaction(order, money):
    """
    Takes in the order type and checks if the inserted money is sufficient.If successful, executes the order
    """

    is_successful = True
    if MENU[order]["cost"] > money:
        is_successful = False
        print("Sorry that's not enough money.Money refunded.")
    else:
        resources["money"] += MENU[order]["cost"]
        if money > MENU[order]["cost"]:
            change = money - MENU[order]["cost"]
            print("Here is ${:.2f} dollars in change.".format(change))

    return is_successful


def execute_order(order):
    """
    Executes the user's order
    """

    for key, value in MENU[order]["ingredients"].items():
        resources[key] -= value

    print("Here's your {}☕ Enjoy!".format(user_choice))


is_off = False
while not is_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    possible_words = list(MENU.keys())
    possible_words.extend(["off", "report"])
    # returns a list of close matches in case the user has made a typo
    user_choice = get_close_matches(user_choice, possible_words, cutoff=0.8)[0]

    if user_choice == "off":
        is_off = True
        continue

    if user_choice == "report":
        print_report()
        continue

    if check_sufficiency(user_choice):
        user_money = insert_coins()
        if check_transaction(user_choice, user_money):
            execute_order(user_choice)
