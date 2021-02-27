logo = '''
  ____        __  __            _____                _
 / __ \      / _|/ _|          | ___ \              | |
| /  \/ ___ | |_| |_ ___  ___  | |_/ /_ __ ___  __ _| | __
| |    / _ \|  _|  _/ _ \/ _ \ | ___ \ '__/ _ \/ _` | |/ /
| \__/\ (_) | | | ||  __/  __/ | |_/ / | |  __/ (_| |   <
 \____/\___/|_| |_| \___|\___| \____/|_|  \___|\__,_|_|\_|
 '''

MENU = {
    'espresso': {
        'ingredients':{
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte':{
        'ingredients':{
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappucino':{
        'ingredients':{
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0
    }
}
storage = {
    'water':  300,
    'milk':  200,
    'coffee': 100,
    'money': 0
    }

profit = 0

def report():
    """ prints amounts of ingredients and cash stored """
    print(f"Water: {storage['water']}ml")
    print(f"Milk: {storage['milk']}ml")
    print(f"Coffee: {storage['coffee']}g")
    print(f"Money: ${storage['money']}")

def fill_storage():
    """ refills the stock """
    storage['water'] += int(input("How much water are you adding? "))
    storage['milk']  += int(input("How much milk are you adding? "))
    storage['coffee'] += int(input("How much coffee are you adding? "))

def collect_cash():
    """collects cash"""
    money = storage['money']
    print(f"You just took ${money}.")
    storage['money'] = 0

def check(order_ingred):
    """ checks if enough ingredients are available for selected choice.
    Returns True if sufficient, False otherwise """

# unclear why for loop is not working correctly, only checking the first item correctly
    # for item in order_ingred:
    #     if order_ingred[item] >= storage[item]:
    #         print(f"Sorry, the machine does not have enough {item}")
    #         return False
    #     return True

    if order_ingred["water"] > storage["water"] or order_ingred["milk"] > storage["milk"] or order_ingred["coffee"] > storage["coffee"]:
        print("Sorry, the machine does not have enough resources")
        return False
    return True

def accept_coins():
    """ collects the inserted amount of money from customer and returns total """
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def transaction(money_received, cost):
    """ returns True if payment is accepted, False otherwise """
    if money_received >= cost:
        storage['money'] += cost
        change = round(money_received - cost,2)
        print(f"Here is {change} in change.")
        return True
    else:
        print("You did not insert enough money; here is your refund.")
        return False

def brew(drink,ingredients):
    """ deduct required ingredients from storage"""
    for item in ingredients:
        storage[item] -= ingredients[item]
    print(f"Here is your {drink}")

def show_options():
    """ prints out a list of commands """
    print("\nYou can use the following commands: choose your drink, 'show' commands, 'report' or 'fill' resources, 'collect' money, or turn 'off'.")

print(logo)
show_options()
while True:
    choice = input("\nWhat would you like to buy (espresso, cappucino, latte)? ")
    if choice == 'report':
        report()
    elif choice == 'off':
         break
    elif choice == 'fill':
        fill_storage()
    elif choice == 'collect':
        collect_cash()
    elif choice == 'show':
        show_options()
    else:
        drink = MENU[choice]
        if check(drink['ingredients']):
            payment = accept_coins()
            if transaction(payment,drink['cost']):
                brew(choice,drink['ingredients'])
