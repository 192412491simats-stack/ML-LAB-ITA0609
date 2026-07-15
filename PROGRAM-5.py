# Online Shopping Bill Calculator

print("===== Online Shopping Bill Calculator =====")

amount = float(input("Enter Purchase Amount: ₹"))

# Discount Calculation
if amount >= 5000:
    discount = amount * 0.20   # 20% discount
elif amount >= 3000:
    discount = amount * 0.10   # 10% discount
else:
    discount = 0

amount_after_discount = amount - discount

# GST Calculation (18%)
gst = amount_after_discount * 0.18

# Final Bill
total_bill = amount_after_discount + gst

# Display Results
print("\n===== Bill Details =====")
print("Purchase Amount : ₹", amount)
print("Discount : ₹", discount)
print("Amount After Discount : ₹", amount_after_discount)
print("GST (18%) : ₹", gst)
print("Total Bill : ₹", total_bill)
