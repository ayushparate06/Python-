# Lab Assignment 2
# Bank Account Menu Driven Program

balance = 0.0

def display_balance():
    print("Current Balance: ₹", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully!")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("Amount Withdrawn Successfully!")


while True:
    print("\n----- BANK MENU -----")
    print("1. Display Current Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 4:
        print("Thank you for using Bank System!")
        break

    elif choice == 1:
        display_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹ "))
        deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹ "))
        withdraw(amount)

    else:
        print("Invalid Choice! Please try again.")