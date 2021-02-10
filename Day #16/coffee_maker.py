from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

valid_prompts = ['report','espresso','latte','cappuccino','off']
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
valid_prompts = ['report','espresso','latte','cappuccino','off']

while True:
    prompt = input(f"What would you like ? ({menu.get_items()}): ").lower()
    if prompt not in valid_prompts:
        continue
    elif prompt == 'off':
        break
    elif prompt == 'report':
        coffee.report()
        continue
    drink = menu.find_drink(prompt)

    if coffee.is_resource_sufficient(drink) == False:
        continue

    if money.make_payment(drink.cost) == False:
        continue

    coffee.make_coffee(drink)
