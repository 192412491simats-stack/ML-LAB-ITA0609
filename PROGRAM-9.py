# Library Fine Calculator

print("===== Library Fine Calculator =====")

days = int(input("Enter Number of Overdue Days: "))

# Fine Calculation
if days <= 5:
    fine = days * 2      # ₹2 per day
elif days <= 10:
    fine = days * 5      # ₹5 per day
else:
    fine = days * 10     # ₹10 per day

# Display Result
print("\n===== Fine Details =====")
print("Overdue Days :", days)
print("Library Fine : ₹", fine)
