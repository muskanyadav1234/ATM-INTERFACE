import os
from datetime import datetime

USER_DIR = "users"
if not os.path.exists(USER_DIR):
    os.mkdir(USER_DIR)
def register():
    username = input("Enter new usernsme:")
    pin = input("Set 4-digit PIN:")
    if len(pin) != 4 or  not pin.isdigit():
        print("PIN must be 4 digits.")
        return
    filepath = os.path.join(USER_DIR, f"{username}.txt")
    if os.path.exists(filepath):
        print("User already exists.")
        return
    with open(filepath,"w") as f:
        f.write(f"{pin}\n0\n")
        print("Registration successful.")
def login():
    username = input("Enter username:")
    filepath = os.path.join(USER_DIR,f"{username}.txt")
    if not os.path.exists(filepath):
        print("user not found.") 
        return
    with open(filepath,"r") as f:
        lines = f.readlines()
    pin = input("Enter 4-digit PIN.")
    if pin != lines[0].strip():
        print("Incorrect PIN.")
        return
    print(f"\welcome, {username}!")
    atm_menu(username)
def atm_menu(username):
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. Logout")
        choice = input("Select option: ")
        if choice == '1':
            check_balance(username)
        elif choice == '2':
            deposit(username)
        elif choice == '3':
            withdraw(username)
        elif choice == '4':
            view_transactions(username)
        elif choice == '5':
            print("Logged out.")
            break
        else:
            print("Invalid option.")

def get_file_lines(username):
    filepath = os.path.join(USER_DIR, f"{username}.txt")
    with open(filepath, "r") as f:
        return f.readlines()

def write_file_lines(username, lines):
    filepath = os.path.join(USER_DIR, f"{username}.txt")
    with open(filepath, "w") as f:
        f.writelines(lines)

def check_balance(username):
    lines = get_file_lines(username)
    balance = float(lines[1])
    print(f"Current Balance: ₹{balance:.2f}")

def deposit(username):
    amount = float(input("Enter amount to deposit: ₹"))
    lines = get_file_lines(username)
    balance = float(lines[1]) + amount
    lines[1] = f"{balance}\n"
    lines.append(f"{datetime.now()}: Deposited ₹{amount:.2f}\n")
    write_file_lines(username, lines)
    print(f"₹{amount:.2f} deposited successfully.")

def withdraw(username):
    amount = float(input("Enter amount to withdraw: ₹"))
    lines = get_file_lines(username)
    balance = float(lines[1])

    if amount > balance:
        print("Insufficient balance.")
        return

    balance -= amount
    lines[1] = f"{balance}\n"
    lines.append(f"{datetime.now()}: Withdrew ₹{amount:.2f}\n")
    write_file_lines(username, lines)
    print(f"₹{amount:.2f} withdrawn successfully.")

def view_transactions(username):
    lines = get_file_lines(username)[2:]
    print("\n--- Transaction History ---")
    if not lines:
        print("No transactions yet.")
    else:
        for line in lines:
            print(line.strip())

def main():
    print("=== ATM Interface ===")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        option = input("Select option: ")
        if option == '1':
            register()
        elif option == '2':
            login()
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()