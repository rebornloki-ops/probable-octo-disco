account = {"balance": 1000, "pin": "1234"}
pin =input("Enter your PIN: ")
if pin == account["pin"]:
    amount =int(input("How much would you like to withdraw? "))
    if int(amount) <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrawal successful. Your new balance is {account['balance']}.")
    else:
        print("Insufficient funds.")
else:   
    # This happens if the PIN is wrong
    print("ACCOUNT LOCKED. ")