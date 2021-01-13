from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


# PROPERTIES
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True


# MAIN
while is_on:
    options = menu.get_items()
    order = input(f"What would you like to drink ({options})? ").lower()

    if order == "off":
        print("Turning off")
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)

        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
