class Account:
    def __init__(self, id, username, pin, balance):
        self.id = id
        self.username = username
        self.pin = pin
        self.balance = balance

class ATM:
    def __init__(self):
        self.accounts = self.load_accounts()
    
    def create_account(self, aid, username, pin, initial_balance):
        if aid in self.accounts:
            print("Account ID already exists.")
            return False
        
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return False
        
        if len(pin) != 4:
            print("PIN must be 4 digits.")
            return False
        
        self.accounts[aid] = {
            'name': username,
            'pin': pin,
            'balance': initial_balance
        }
        self.save_accounts()
        print(f"Account created successfully for {username}!")
        return True

    def deposit_amount(self, aid, pin, amt):
        account = self.authenticate(aid, pin)
        if not account:
            return False
        
        if amt <= 0:
            print("Invalid amount. Deposit amount must be positive.")
            return False
        
        account['balance'] += amt
        self.save_accounts()
        print(f"Deposited ${amt:.2f}. New balance: ${account['balance']:.2f}")
        return True

    def withdraw_amount(self, aid, pin, amt):
        account = self.authenticate(aid, pin)
        if not account:
            return False
        
        if amt <= 0:
            print("Invalid amount. Withdrawal amount must be positive.")
            return False
        
        if amt > account['balance']:
            print("Insufficient funds.")
            return False
        
        account['balance'] -= amt
        self.save_accounts()
        print(f"Withdrew ${amt:.2f}. New balance: ${account['balance']:.2f}")
        return True

    def change_pin(self, aid, old_pin, new_pin):
        account = self.authenticate(aid, old_pin)
        if not account:
            return False
        
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("New PIN must be 4 digits.")
            return False
        
        account['pin'] = new_pin
        self.save_accounts()
        print("PIN changed successfully!")
        return True

    def check_balance(self, aid, pin):
        account = self.authenticate(aid, pin)
        if not account:
            return False
        
        print(f"Account balance for {account['name']}: ${account['balance']:.2f}")
        return True

    def authenticate(self, aid, pin):
        if aid not in self.accounts:
            print("No such account.")
            return None
        
        account = self.accounts[aid]
        if account['pin'] != pin:
            print("Incorrect PIN.")
            return None
        
        return account
    
    def load_accounts(self):
        accounts = {}
        try:
            with open("bank.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        li = line.split(",")
                        if len(li) >= 4:
                            account_id = li[0]
                            accounts[account_id] = {
                                'name': li[1],
                                'pin': li[2],
                                'balance': float(li[3])
                            }
        except:
            print("No existing accounts file found. Starting with empty accounts.")
        return accounts
    def save_accounts(self):
        try:
            with open("bank.txt", "w") as file:
                for account_id, data in self.accounts.items():
                    line = f"{account_id},{data['name']},{data['pin']},{data['balance']:.2f}\n"
                    file.write(line)
        except:
            print(f"Error saving accounts:")

def main():
    atm = ATM()
    
    while True:
        print("\n=== ATM SIMULATOR ===")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Change PIN")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Create New Account ---")
            aid = input("Account ID: ").strip()
            username = input("Username: ").strip()
            pin = input("PIN (4 digits): ").strip()
            try:
                bal = float(input("Initial balance: $").strip())
                atm.create_account(aid, username, pin, bal)
            except ValueError:
                print("Invalid balance amount.")
                
        elif choice == "2":
            print("\n--- Deposit Money ---")
            aid = input("Account ID: ").strip()
            pin = input("PIN: ").strip()
            try:
                amt = float(input("Deposit amount: $").strip())
                atm.deposit_amount(aid, pin, amt)
            except ValueError:
                print("Invalid amount.")
                
        elif choice == "3":
            print("\n--- Withdraw Money ---")
            aid = input("Account ID: ").strip()
            pin = input("PIN: ").strip()
            if pin == atm.authenticate(aid,pin):    
                try:
                 amt = float(input("Withdrawal amount: $").strip())
                 atm.withdraw_amount(aid, pin, amt)
                except ValueError:
                 print("Invalid amount.")
            else:
                print("Invalid pin")
                
        elif choice == "4":
            print("\n--- Check Balance ---")
            aid = input("Account ID: ").strip()
            pin = input("PIN: ").strip()
            atm.check_balance(aid, pin)
            
        elif choice == "5":
            print("\n--- Change PIN ---")
            aid = input("Account ID: ").strip()
            old_pin = input("Old PIN: ").strip()
            new_pin = input("New PIN (4 digits): ").strip()
            atm.change_pin(aid, old_pin, new_pin)
            
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select 1-6.")

main()