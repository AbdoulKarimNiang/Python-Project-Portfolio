Flavours: dict = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 3.0,
    }
}

Resources = {
    'water': 300,
    'coffee': 100,
    'milk': 200,
}

coins = {
    'Quarter': 0.25,
    'Dime': 0.10,
    'Nickel': 0.05,
    'Penny': 0.01
}


def check_resources(user_input: str) -> bool:
    """ The program checks if there are enough resources. The input is the user_input and it returns a bool"""
    enough_resources = True
    ingredient_selection = Flavours[user_input]["ingredients"]
    for key in ingredient_selection:
        if Resources[key] - ingredient_selection[key] < 0:
            print(f"Sorry there is not enough {key}.")
            enough_resources = False
    return enough_resources


def quantity_reduction(client_order) -> dict:
    """ Reduce the amount of resources in the coffe maker"""
    ingredient_selection = Flavours[client_order]["ingredients"]
    for key in ingredient_selection:
        Resources[key] -= ingredient_selection[key]
    return Resources


def ask_money() -> float:
    """ Request the money to be inserted, and it returns the amount """
    amount: float = 0.00
    print(f"Please insert coins")
    for coins_name in coins:
        while True:
            num_coins_str: str = input(f"How many {coins_name}?: ")
            if not num_coins_str.isdigit():
                continue
            num_coins: float = float(num_coins_str)
            if num_coins <= 0:
                continue
            else:
                key_value: float = num_coins * coins[coins_name]
                amount += key_value
                break
    return amount



def check_cost_order(client_order: str, amount: float) -> bool:
    """ Check if the amount given is enough to get the product it returns a string with the amount given
     is enough or a sentence if the amount given is not enough """
    price_selection = Flavours[client_order]['price']
    if amount > price_selection:
        return True
    else:
        return False


should_continue = True
profit = 0
if __name__ == '__main__':
    while should_continue:
        order: str = input("What would you like? (espresso/latte/cappuccino)?: ").title()
        if order == 'Report':
            for key, value in Resources.items():
                print(f"{key} : {value}")
                print(f"profit: {profit}")
        elif order == 'Off':
            should_continue = False
        elif order not in Flavours:
            print("Please enter a valid beverage from the above list 👆🏾")
            continue
        elif check_resources(order):
            money_given = ask_money()
            product_cost = Flavours[order]['price']
            if check_cost_order(order, money_given):
                rest: float = money_given - product_cost
                rounding: float = round(rest, 2)
                print(f"Here is ${rounding} in change")
                enough_quantity = check_resources(order)
                if enough_quantity:
                    quantity_reduction(order)
                    print(f"Here is you {order}")
                    profit += product_cost
            else:
                print(f"Sorry that's not enough. Money refunded")
