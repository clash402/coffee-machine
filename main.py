# take_order()
# take_payment()
# process_payment()


# PROPERTIES
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18},"cost": 1.5,},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24},"cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24},"cost": 3.0,}
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0


# METHODS
def check_ingredients(menu, order, resources):
    for ingredient, amount in menu[order]["ingredients"].items():
        if not amount <= resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def take_coins(menu, order):
    print(f"The cost is ${menu[order]['cost']}. Please insert coins:")

    amount_due = menu[order]["cost"]
    is_taking_payment = True

    while is_taking_payment:
        coins = []
        coins.append(round(0.25 * int(input(f"How many quarters?: ")), 2))
        coins.append(round(0.10 * int(input(f"How many dimes?: ")), 2))
        coins.append(round(0.05 * int(input(f"How many nickles?: ")), 2))
        coins.append(round(0.01 * int(input(f"How many pennies?: ")), 2))
        total_inserted = round(sum(coins), 2)

        if total_inserted >= amount_due:
            if total_inserted > amount_due:
                change = round(total_inserted - amount_due, 2)
                print(f"Here is ${change} in change.")
            print(f"Here is your {order}. Enjoy!")
            is_taking_payment = False
        else:
            amount_left = round(amount_due - total_inserted, 2)
            print(f"Please insert ${amount_left} more.")
            amount_due = amount_left


def generate_report(resources, money):
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key.title()}: {value}g")
        else:
            print(f"{key.title()}: {value}ml")
    return f"Money: ${money}"


def run_machine(menu, resources, money):
    menu_items = list(MENU.keys())
    menu_items_string = ", ".join(menu_items)
    machine_is_on = True

    while machine_is_on:
        order = input(f"Would you like a {menu_items_string}? ").lower()

        if order in menu_items:
            ingredients_are_full = check_ingredients(menu, order, resources)

            if ingredients_are_full:
                take_coins(menu, order)
                money += menu[order]["cost"]

                for ingredient, amount in menu[order]["ingredients"].items():
                    resources[ingredient] -= amount

        elif order == "report":
            print(generate_report(resources, money))
        elif order == "off":
            print("Turning off")
            machine_is_on = False
        else:
            print(f"{order} is not an item on the menu.")


# MAIN
run_machine(MENU, resources, money)
