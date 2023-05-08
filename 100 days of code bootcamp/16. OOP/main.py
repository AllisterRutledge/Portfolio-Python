from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    user_request = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_request == "off":
        machine_on = False
    elif user_request == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        coffee_order = menu.find_drink(user_request)
        if coffee_order is not None:
            if coffee_machine.is_resource_sufficient(coffee_order) and money_machine.make_payment(coffee_order.cost):
                coffee_machine.make_coffee(coffee_order)
