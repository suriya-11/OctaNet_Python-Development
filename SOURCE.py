import time

class ATM:
    def __init__(self, pin=1234, password="admin123", balance=500000):
        self.pin = pin
        self.password = password
        self.balance = balance
        self.attempts = 2  # Only 2 attempts for PIN

    def check_balance(self):
        print(f"\nYour current balance is: {self.balance}\n")

    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                self.balance += amount
                print(f"\n{amount} deposited successfully!")
            else:
                print("\nInvalid amount!")
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")
        self.check_balance()

    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"\n{amount} withdrawn successfully!")
            else:
                print("\nInsufficient funds or invalid amount!")
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")
        self.check_balance()

    def change_pin(self):
        try:
            new_pin = int(input("Enter new PIN: "))
            confirm_pin = int(input("Confirm new PIN: "))
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("\nPIN changed successfully!")
            else:
                print("\nPINs do not match!")
        except ValueError:
            print("\nInvalid input! Please enter numbers only.")

    def change_password(self):
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        if new_password == confirm_password:
            self.password = new_password
            print("\nPassword changed successfully!")
        else:
            print("\nPasswords do not match!")

    def run(self):
        print("Please insert your card...")
        time.sleep(2)

        while self.attempts > 0:
            try:
                entered_pin = int(input("Enter your ATM PIN: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if entered_pin == self.pin:
                print("\nWelcome to the ATM!\n")
                while True:
                    print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Change PIN\n5. Change Password\n6. Exit")
                    try:
                        choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input! Please enter a number from 1 to 6.")
                        continue

                    options = {
                        1: self.check_balance,
                        2: self.deposit,
                        3: self.withdraw,
                        4: self.change_pin,
                        5: self.change_password,
                        6: lambda: print("Thank you for using the ATM!"),
                    }
                    
                    if choice in options:
                        if choice == 6:
                            return
                        options[choice]()
                    else:
                        print("Invalid choice! Please try again.")
            else:
                self.attempts -= 1
                print(f"Wrong PIN! You have {self.attempts} attempt(s) left.")

        print("Too many incorrect attempts! Card blocked.")

# Running the ATM system
atm = ATM()
atm.run()
