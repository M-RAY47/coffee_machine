from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()

machine_on = True

while machine_on:
	options = menu.get_items()
	choice = input(f"What would you like? ({options})")
	if choice.upper() == "OFF":
		machine_on = False
	elif choice.upper() == "REPORT":
		coffee_maker.report()
		money_machine.report()
	else:
		drink = menu.find_drink(choice)
		is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
		is_payement_succeeded = money_machine.make_payment(drink.cost)
		if is_enough_ingredients and is_payement_succeeded:
			coffee_maker.make_coffee(drink)