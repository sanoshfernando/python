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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

def cal_money():
    if resource_value ==1:
        print("Please insert coins.")
        quarters=int(input("how many quarters?:"))
        dimes=int(input("how many dimes?:"))
        nickles=int(input("how many nickles?:"))
        pennies=int(input("how many pennies?:"))
        global total_money
        total_money = quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    return

def processing_order():
    if resource_value == 1:
        cost = MENU[choice]["cost"]
        change=total_money-cost

        if change>=0:
            resources["money"] += MENU[choice]["cost"]
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    return
def check():
    global resource_value
    resource_value = 1
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    try:
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    except KeyError:
        arg_exept = 1
    if resources["water"] < 0:
        print(f"Sorry there is not enough water")
        resource_value = 0
    elif resources["milk"] < 0:
        print(f"Sorry there is not enough milk")
        resource_value = 0
    elif resources["coffee"] < 0:
        print(f"Sorry there is not enough coffee")
        resource_value = 0

    if resource_value == 0:
        resources["water"] += MENU[choice]["ingredients"]["water"]
        resources["coffee"] += MENU[choice]["ingredients"]["coffee"]
        resources["milk"] += MENU[choice]["ingredients"]["milk"]

is_machine_running=True

while is_machine_running:
    choice =input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="espresso":
        check()
        cal_money()
        processing_order()
    elif choice=="latte":
        check()
        cal_money()
        processing_order()
    elif choice=="cappuccino":
        check()
        cal_money()
        processing_order()
    elif choice=="report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
    elif choice =="off":
        is_machine_running=False
    else:
        print("Wrong command")
