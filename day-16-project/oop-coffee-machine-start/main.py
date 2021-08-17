from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
profit = 0

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(money_machine.report())
        print(coffee_maker.report())
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.process_coins()
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
