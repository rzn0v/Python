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


def is_resources_sufficient(ingredients):
    for items in ingredients:
        if ingredients[items] > resources[items]:
            print(f"Sorry, There's not enough {items}")
            return False
        return True
    

def process_coins(cost):
    print("Insert coins.")
    total = float(input("How many quarters?: "))*0.25
    total += float(input("How many dimes?: "))*0.1
    total += float(input("How many nickels?: "))*0.05
    total += float(input("How many pennies?: "))*0.01
    return total

def process_coffee(drink_name, ingredients):
    for items in ingredients:
        resources[items] = resources[items] - ingredients[items]
    print(f"Here is your {drink_name}. Enjoy!")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
to_continue = True
while to_continue:
    # Type "report" to get the current available resources.
    #Type "off" to turn off the machine.
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        to_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        drink_cost = MENU[choice]["cost"]
        if is_resources_sufficient(drink["ingredients"]):
            total = process_coins(drink_cost)
            if drink_cost > total:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money = money + drink_cost
                change = round(total - drink_cost,2)
                print(f"Here is your ${change} in change.")
                process_coffee(choice, drink["ingredients"])

