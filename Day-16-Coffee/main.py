# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {"profit": 0}


def process_money(cost_coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many quarters?: "))
    nickel = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    calc_money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickel) + (0.01 * pennies)
    if calc_money >= cost_coffee:
        change = round((calc_money - cost_coffee), 2)
        money['profit'] += cost_coffee
        print(f"Here is ${change} in change.")
        return True
    elif calc_money < cost_coffee:
        return False


def check_requirement(order, req_water, req_coffee, req_milk, one_cost):
    if resources['water'] >= req_water:
        if resources['coffee'] >= req_coffee:
            if resources['milk'] >= req_milk:
                if process_money(one_cost):
                    resources['water'] -= req_water
                    resources['coffee'] -= req_coffee
                    resources['milk'] -= req_milk
                    print(f"Here is your {order}. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Sorry, there is not enough milk.")
        else:
            print("Sorry, there is not enough coffee.")
    else:
        print("Sorry, there is not enough water.")


def put_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money['profit']}")

def choose():
    order = input(" What would you like? (espresso/latte/cappuccino):")
    if order == 'report':
        put_report()
        choose()
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        one_req = MENU[order]['ingredients']
        one_cost = MENU[order]['cost']
        check_requirement(order, one_req['water'], one_req['coffee'], one_req['milk'], one_cost)
        choose()
    elif order == 'off':
        print("Coffee Machine is off now!")
        return


choose()