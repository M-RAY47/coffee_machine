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
	"cappucino": {
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
cash={
	"quarter": 0.25,
	"dime": 0.10,
	"nickle": 0.05,
	"pennie": 0.01
}

def resources_sufficent(drink_ingredients):
	"""To check if the resources Ingredients if they are sufficient"""
	for ingredient in drink_ingredients:
		if drink_ingredients[ingredient]>= resources[ingredient]:
			print(f"Sorry there is not enough {ingredient}.")
			return False
	return True

def insert_coins():
	"""To calculate all the coins inserted into the coffee machine, and retuns the total"""
	print("Please insert coins")
	total_cash= int(input("how many quarters?: "))*cash["quarter"]
	total_cash+= int(input("how many dimes?: "))*cash["dime"]
	total_cash+= int(input("how many nickle?: "))*cash["nickle"]
	total_cash+= int(input("how many pennies:"))*cash["pennie"]
	print(f"You have entered total amount: ${round(total_cash,2)}")
	return total_cash

def payment_successful(total_cash, drink_cost):
	"""Check if the user inserted enough coins for the drink he selected. Return true or false"""
	if total_cash < drink_cost:
		print("Sorry that's not enough money. Money refunded.")
		return False
	elif total_cash == drink_cost:
		global profit
		profit += drink_cost
		return True
	else:
		change = round(total_cash-drink_cost, 2)
		profit; profit += drink_cost
		print(f"Here is your change ${change}")
		return True

def make_coffee(drink):
	"""will make the coffee and extract the ingredients of the selected drink from the resources."""
	for ingredient in drink["ingredients"]:
		resources; resources[ingredient] -= drink['ingredients'][ingredient]

# TODO: 1. Print report of all coffee machine resources
coffee = "☕"

on = True
while on:
	choice = input("What would you like? (espresso/latte/cappucino): ")
	if choice.upper() == "OFF":
		on = False
	elif choice.upper() == "REPORT":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"coffee: {resources['coffee']}g")
		print(f"Money: ${profit}")
	else:
		drink = MENU[choice]
		if resources_sufficent(drink["ingredients"]):
			payment= insert_coins()
			if payment_successful(payment,drink["cost"]):
				make_coffee(drink)
				print(f"enjoy your {choice} {coffee}")
