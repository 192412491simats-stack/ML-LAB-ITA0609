# Mobile Recharge Billing Calculator

recharge_amount = float(input("Enter Recharge Amount (₹): "))
discount_percent = float(input("Enter Promotional Discount (%): "))
cashback_percent = float(input("Enter Cashback (%): "))

# Discount Calculation
discount = recharge_amount * (discount_percent / 100)
amount_after_discount = recharge_amount - discount

# Cashback Calculation
cashback = amount_after_discount * (cashback_percent / 100)

# Final Effective Cost
final_cost = amount_after_discount - cashback

# Output
print("\n----- Mobile Recharge Bill -----")
print(f"Original Recharge Amount : ₹{recharge_amount:.2f}")
print(f"Discount Applied         : ₹{discount:.2f}")
print(f"Amount After Discount    : ₹{amount_after_discount:.2f}")
print(f"Cashback Earned          : ₹{cashback:.2f}")
print(f"Final Effective Cost     : ₹{final_cost:.2f}")
