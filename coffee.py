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
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    'water': 1000,
    'milk': 500,
    'coffee': 200,
    'cash': 0.0
}

bank = {
    "quarters": 25,
    "dimes": 10,
    "nickles": 5,
    "pennies": 1,
}







def collect_coins(list_collect):
    '''
    The input should be an empty list.
    The function returns a list of coins
    '''
    


    number_quarters = input("how many quarters?: ")
    if number_quarters == "":
        number_quarters = 0
    for i in range(int(number_quarters)):
        list_collect.append("quarters")

    number_dimes = input("how many dimes?: ")
    if number_dimes == "":
        number_dimes = 0
    for i in range(int(number_dimes)):
        list_collect.append("dimes")

    number_nickles = input("how many nickles?: ")
    if number_nickles == "":
        number_nickles = 0
    for i in range(int(number_nickles)):
        list_collect.append("nickles")

    number_pennies = input("how many pennies?: ")
    if number_pennies == "":
        number_pennies = 0
    for i in range(int(number_pennies)):
        list_collect.append("pennies")

    return list_collect





def counting(list_count):
    '''
    The input should be a list with coins.
    The function returns the sum of coins.
    '''
    a = 0
    for coin in list_count:
        a += bank[coin]
    return a * 0.01


def buy(price, money):
    '''
    the input is price of a coffee and money paid.
    the output is True + change/ True/ False
    '''
    if price < money:
        change = money - price
        return change
    if price > money:
        print(f"You have not enough money, you need ${price}.")
        change = -1.0
        return change
    if price == money:
        change = 0.0
        return change
        

#cooking

def cooking():
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == "":
        return
    elif coffee_choice != 'espresso' and coffee_choice != 'latte' and coffee_choice != 'cappuccino':
        print("Sorry I couldn't hear you, say it again, please.")
        cooking()
        return
    list_coins = []
    list_coins = collect_coins(list_coins)
    sum_coins = counting(list_coins)
    change = buy(MENU[coffee_choice]["cost"], sum_coins)


    if change < 0:
        print(f"Here are your money back ${sum_coins}")
        return
    elif resources["water"] < MENU[coffee_choice]["ingredients"]["water"]:
        print("Sorry, we are out of water.")
        print(f"Here are your money back ${sum_coins}")
        return
    elif resources["milk"] < MENU[coffee_choice]["ingredients"]["milk"]:
        print("Sorry, we are out of milk.")
        print(f"Here are your money back ${sum_coins}")
        return
    elif resources["coffee"] < MENU[coffee_choice]["ingredients"]["coffee"]:
        print("Sorry, we are out of coffee beans.")
        print(f"Here are your money back ${sum_coins}")
        return
    else:
        if change > 0:
            print(f"Here is your change ${change}")
        print(f'''
        Here is your coffee.


                ( (  (   (
               _.),)--),..)
            .-;'-.,__(__,.-';
           (( |             |
            `))             ;
                 {coffee_choice}
             ` \           /
            .-' `,._____.,' '-.
           (     '------'     )
            `-=..________..--'


            
        ''')
        resources["cash"] = resources["cash"] + sum_coins
        resources["water"] = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
        resources['milk'] = resources['milk'] - MENU[coffee_choice]["ingredients"]['milk']
        resources["coffee"] = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]

    if input("Would you like some more? Yes/No").lower() == 'yes':
        cooking()
    else:
        print("Buy, buy! =)")

cooking()

