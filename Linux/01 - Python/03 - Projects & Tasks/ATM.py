# server
accounts = [
    {"username": "Ahmed",
    "password": "pass123",
    "balance": 20000,
    "operations_history": []
    },

    {"username": "Ibrahim",
    "password": "123456",
    "balance": 10000,
    "operations_history": []
    },
]

MAX_WITHDRAW_PER_DAY = 30000
MAX_DEPOSIT_PER_DAY = 40000

operations = ("a: Check balance", "b: Withdraw", "c: Deposit", "d: List operations history")


# terminal
while(1):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    # check validity
    for i in accounts:
        if (i["username"] == username) & (i["password"] == password):
            while(1):
                # list operations 
                for j in operations:
                    print(j)
                # Ask user to enter an operation to perform
                quiry = input("Enter operation: ")

                # Check balance
                if quiry == "a":
                    print("Your balance is {}" .format(i["balance"]))
                    # Ask user if he/she wants to enter another operation
                    if input("Another operation? (y/n): ") == "y":
                        continue
                    else:
                        break

                # Withdraw money from balance
                elif quiry == "b":
                    while(1):
                        amount = int(input("Please enter amount to withdraw: "))
                        if amount > i["balance"]:
                            print("There is not enough balance in your account")
                        elif amount > MAX_WITHDRAW_PER_DAY:
                            print("This amount exceeds max allowed withdraw amount per day ({} L.E.)" .format(MAX_WITHDRAW_PER_DAY))
                        else:
                            i["balance"] = i["balance"] - amount
                            print("Sucessful Operation.")
                            i["operations_history"].append("operation: withdraw, amount: {}" .format(amount))
                            break
                    # Ask user if he/she wants to enter another operation
                    if input("Another operation? (y/n): ") == "y":
                        continue
                    else:
                        break

                # Deposit money into account
                elif quiry == "c":
                    while(1):
                        amount = int(input("Please enter amount to deposit in account: "))
                        if amount > MAX_DEPOSIT_PER_DAY:
                            print("This amount exceeds max allowed deposit amount per day ({} L.E.)" .format(MAX_DEPOSIT_PER_DAY))
                        else:
                            i["balance"] = i["balance"] + amount
                            print("Sucessful Operation.")
                            i["operations_history"].append("operation: deposit, amount: {}" .format(amount))
                            break 
                    # Ask user if he/she wants to enter another operation
                    if input("Another operation? (y/n): ") == "y":
                        continue
                    else:
                        break

                # list operations history
                elif quiry == "d":
                    while(1):
                        if len(i["operations_history"]) == 0:
                            print("No operations has been done on this account")
                        else:
                            for op in i["operations_history"]:
                                print(op)
                            break
                    # Ask user if he/she wants to enter another operation
                    if input("Another operation? (y/n): ") == "y":
                        continue
                    else:
                        break
            break

        else:
            print("username or password is incorrect, please try again")






