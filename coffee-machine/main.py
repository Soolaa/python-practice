MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        } ,
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "coffee" : 24,
            "milk" : 150,
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "coffee" : 24,
            "milk" : 100,
        },
        "cost" : 3.0,
    }
}

resources = {
    "water" : 300,
    "coffee" : 100,
    "milk" : 200,
    "money": 0
}

quarters = 0.25
dimes= 0.10
nickels = 0.05
pennies = 0.01

def report(resource):
    for key in resource:
        if key in ["water" , "milk"]:
            unit = " ml"
            print(f"{key} : {resource[key]}{unit}")
        elif key == "coffee":
            unit = " g"
            print(f"{key} : {resource[key]}{unit}")
        else:
            unit = "$"
            print(f"{key} : ${resource[key]}")
        #print(f"{key} : {resource[key]}{(lambda: ' ml' if key in ['water', 'coffee'] else '')()}")

def order(order, menu, resource):
    sum_of_coins = 0
    for ingredient , value in menu[order]["ingredients"].items():
        if menu[order]["ingredients"][ingredient] > resource[ingredient]:
            return f"Sorry. there is not enough {ingredient}"

    print ("Please insert coins.")
    sum_of_coins = int(input("How many quarters? ")) * quarters
    sum_of_coins += int(input("How many dimes? ")) * dimes
    sum_of_coins += int(input("How many nickles? ")) * nickels
    sum_of_coins += int(input("How many pennies? ")) * pennies
    #return f" sum: {sum_of_coins}"

    if sum_of_coins >= menu[order]["cost"]:
        resource["money"] += menu[order]["cost"]
        change = round(sum_of_coins - menu[order]["cost"], 2)
        print(f"Here is ${change} in change.")
        print (f"Here is your {order}. Enjoy")
    else:
        print("Sorry that's not enough money. Money refunded")
        return None

    for ingredient , value  in menu[order]["ingredients"].items():
        resource[ingredient] -= value


    return None


machine_status = True
while machine_status:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    #user_coins = input("Please insert coins. ")
    if user_order == "report":
        report(resources)
    elif user_order.lower() == "off":
        print("The machine is turning off...")
        machine_status = False
    else:
        print(order(user_order , MENU, resources))


