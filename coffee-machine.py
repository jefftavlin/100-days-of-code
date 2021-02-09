from data import MENU, resources, coins
from art import *
logo = text2art("Coffee Machine")

print(logo)

def print_resources(resources):
    for key, value in resources.items():
        print(f"{key.title()}: {value}")

def amount_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters, dimes, nickels, pennies

def enough_resources(prompt, resources):
    pass
    if resources['water'] < MENU[prompt]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    if resources['coffee'] < MENU[prompt]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    if prompt != 'espresso':
        if resources['milk'] < MENU[prompt]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False
    return True

def process_coins(prompt, quarters,nickels,dimes,pennies):
    amount = sum[quarters * 0.25,dimes * 0.10, nickels * 0.05, pennies * 0.01]
    cost = MENU[prompt]['cost']
    if amount > cost:
        

valid_prompts = ['report','espresso','latte','cappuccino','off']

while True:
    prompt = input("What would you like ? (espresso/latte/cappuccino): ").lower()
    if prompt not in valid_prompts:
        print('Please choose a valid option. (espresso/latte/cappuccino)')
        continue
    elif prompt == 'off':
        break
    elif prompt == 'report':
        print_resources(resources)

    print("Please insert coins.")
    if enough_resources(prompt, resources) == False:
        continue

    quarters, dimes, nickels, pennies = amount_coins()
