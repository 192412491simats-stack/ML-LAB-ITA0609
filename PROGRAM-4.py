# ATM Cash Withdrawal System

print("===== ATM Cash Withdrawal System =====")

# Stored account details
correct_pin = 1234
balance = 10000

# User input
pin = int(input("Enter PIN: "))

if pin == correct_pin:
    print("Current Balance: ₹", balance)

    amount = float(input("Enter Withdrawal Amount: ₹"))

    if amount <= balance:
        balance -= amount
        print("\nWithdrawal Successful!")
        print("Amount Withdrawn: ₹", amount)
        print("Remaining Balance: ₹", balance)
    else:
        print("\nInsufficient Balance!")
else:
    print("\nInvalid PIN!")
