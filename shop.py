items = {
    "cushion": 8.0,
    "chair": 75.0,
    "sofa": 350.0,
    "lamp": 40.0,
    "table": 90.0,
    "painting": 58.0
}

starting_money = 100.0

def display_items():
    print(f"Welcome to the furniture shop! Your balance is £{starting_money}.")
    for item, price in items.items():
        print(f"{item}: {price}")

def process_purchase(user_item):
    if user_item in items and items[user_item] <= starting_money:
        print(f"Here's your {user_item}!")
        balance = starting_money - items[user_item]
        return balance

    elif user_item in items and items[user_item] > starting_money:
        balance = starting_money
        purchase_attempts = 0

        while balance < items[user_item] and purchase_attempts < 3:
            has_extra_money = input(f"I'm sorry, you can't afford a {user_item} right now. Do you have any more money? y/n")
            if has_extra_money == "y":
                extra_money = float(input("How much more money do you have? "))
                if extra_money > 0:
                    balance += extra_money
                    if balance >= items[user_item]:
                        print(f"Here's your {user_item}!")
                    else:
                        pass
                else:
                    raise ValueError("Invalid value entered")

            elif has_extra_money == "n":
                print(f"I am sorry, you cannot afford a {user_item}.")
                break

            else:
                raise ValueError("Invalid value entered")

            purchase_attempts += 1

        if purchase_attempts >= 3:
            raise ValueError("Maximum purchase attempts reached. Exiting the shop.")

    elif user_item == "exit":
        pass

    else:
        raise ValueError("Invalid value entered")
    
    return starting_money

if __name__ == '__main__':
    display_items()

    try:
        user_item = input("Please type in the name of the item you wish to buy, or 'exit' if you wish to leave the shop: ")
        process_purchase(user_item)

    except ValueError as e:
        print(e)

    finally:
        print("Thank you for visiting the shop, come back again soon.")