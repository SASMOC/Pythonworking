import random

# Generate a random balance between £100 - £1000
balance = random.randint(100, 1000)

# Ask for the user's PIN code
for i in range(3):
    pin = input("Please enter your 4 digit PIN code: ")
    if pin == "1234":  # Replace "1234" with the correct PIN code
        print("PIN code accepted.")
        break
    else:
        print("Incorrect PIN code. Please try again.")
else:
    print("You have entered an incorrect PIN code 3 times. Your card has been retained.")
    exit()  # End the program if the user enters an incorrect PIN code 3 times

# Display the menu of options to the user
while True:
    print("\nMenu:")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Quit")

    choice = input("Please enter your choice (1-4): ")

    if choice == "1":
        print("Your balance is £" + str(balance))

    elif choice == "2":
        amount = int(input("Please enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. Your balance is now £" + str(balance))
        else:
            print("Insufficient funds.")

    elif choice == "3":
        amount = int(input("Please enter the amount to deposit: "))
        balance += amount
        print("Deposit successful. Your balance is now £" + str(balance))

    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
