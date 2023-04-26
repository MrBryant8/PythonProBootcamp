from Menu import Menu
from Coffee_maker import CoffeeMaker
from Money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()


is_on = True
while is_on:
    choice = input("What would you like?({})".format(menu.get_items()))
    if choice == "off":
        is_on = False
        continue
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
