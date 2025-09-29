# ATM Withdrawal Program

# account balance
balance = 5000  

# step 1: user enters PIN
pin = input("Enter your 4-digit PIN: ")

# check PIN
if pin == "1234":  # simple PIN validation
    print("PIN verified successfully.")
    print("Current Balance is",balance)
    
    # enter withdrawal amount
    amount = int(input("Enter amount to withdraw: "))
    
    # check balance availability
    if amount <= balance:
        balance -= amount
        print("dispensed Cash:", amount)
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")
else:
    print("Invalid PIN! Try again.")
