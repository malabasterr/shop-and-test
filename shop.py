items = {
    "cushion": 8.0,
    "chair": 75.0,
    "sofa": 350.0
}

starting_money = 100.0

print(f"Welcome to the furniture shop! Your balance is £{starting_money}.")
for item, price in items.items():
    print(f"{item}: {price}")

try:
    user_item = input("Please type in the name of the item you wish to buy, or 'exit' if you wish to leave the shop: ")

    if user_item in items and items[user_item] <= starting_money:
        print(f"Here's your {user_item}!")

    elif user_item in items and items[user_item] > starting_money:

        balance = starting_money
        purchase_attempts = 0

        while balance < items[user_item] and purchase_attempts <3:
            has_extra_money = input(f"I'm sorry, you can't afford a {user_item} right now. Do you have any more money? y/n")
            if has_extra_money == "y":
                extra_money = float(input("How much more money do you have? "))
                if extra_money > 0:
                    balance = balance + extra_money
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

except ValueError as e:
    print(e)

finally:
    print("Thank you for visiting the shop, come back again soon.")