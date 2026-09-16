# Task 3 - Program 1: ATM Simulation (Menu-Driven)
# Demonstrates persistent variables outside the main loop, conditional checks, and input validation.


def atm_app():
    """
    Runs the menu-driven ATM simulation.
    Exits back to the caller when Option 5 is selected.
    """
    balance = 5000.0  # Initial account balance
    pin = "1234"      # Default account PIN

    print("\n========================================")
    print("            ATM SIMULATION              ")
    print("========================================")

    # PIN Authentication (3 attempts allowed)
    attempts = 3
    authenticated = False
    while attempts > 0:
        entered_pin = input("Please enter your 4-digit PIN: ").strip()
        if entered_pin == pin:
            authenticated = True
            print("PIN verified successfully!\n")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN. Attempts remaining: {attempts}")
            else:
                print("Too many incorrect attempts. Returning to main system.")
                return

    # Main ATM Menu Loop
    while True:
        print("------------- ATM MENU -------------")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Change PIN")
        print("5. Exit")
        print("------------------------------------")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print(f"\n>> Your Current Balance is: Rs. {balance:.2f}\n")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: Rs. "))
                if amount <= 0:
                    print(">> Error: Deposit amount must be positive.\n")
                else:
                    balance += amount
                    print(f">> Success: Rs. {amount:.2f} deposited.")
                    print(f">> New Balance: Rs. {balance:.2f}\n")
            except ValueError:
                print(">> Error: Invalid input. Please enter a valid number.\n")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: Rs. "))
                if amount <= 0:
                    print(">> Error: Withdrawal amount must be greater than zero.\n")
                elif amount > balance:
                    # Balance check BEFORE withdrawal to prevent negative balance
                    print(f">> Transaction Rejected: Insufficient balance.")
                    print(f">> Attempted: Rs. {amount:.2f} | Available: Rs. {balance:.2f}\n")
                else:
                    balance -= amount
                    print(f">> Success: Please collect Rs. {amount:.2f}.")
                    print(f">> Remaining Balance: Rs. {balance:.2f}\n")
            except ValueError:
                print(">> Error: Invalid input. Please enter a valid number.\n")

        elif choice == "4":
            old_pin = input("Enter your current PIN: ").strip()
            if old_pin != pin:
                print(">> Error: Current PIN incorrect. PIN change cancelled.\n")
            else:
                new_pin = input("Enter new 4-digit PIN: ").strip()
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print(">> Success: Your PIN has been changed successfully!\n")
                else:
                    print(">> Error: PIN must be exactly 4 digits.\n")

        elif choice == "5":
            print(">> Thank you for banking with us. Goodbye!\n")
            break

        else:
            print(">> Error: Invalid choice! Please select an option from 1 to 5.\n")


if __name__ == "__main__":
    atm_app()
