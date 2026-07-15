# Bank Interest Calculator

print("===== Bank Interest Calculator =====")

# Input
principal = float(input("Enter Principal Amount: ₹"))
rate = float(input("Enter Annual Interest Rate (%): "))
time = float(input("Enter Time (Years): "))

# Simple Interest
simple_interest = (principal * rate * time) / 100

# Compound Interest
compound_amount = principal * (1 + rate / 100) ** time
compound_interest = compound_amount - principal

# Display Results
print("\n===== Interest Details =====")
print("Simple Interest (SI) : ₹", round(simple_interest, 2))
print("Compound Interest (CI) : ₹", round(compound_interest, 2))
print("Total Amount with CI : ₹", round(compound_amount, 2))
