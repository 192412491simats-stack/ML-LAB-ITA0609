# Restaurant Billing System

print("===== Restaurant Billing System =====")

# Food item prices
burger = 120
pizza = 250
pasta = 180

# Quantity input
qty_burger = int(input("Enter Burger Quantity: "))
qty_pizza = int(input("Enter Pizza Quantity: "))
qty_pasta = int(input("Enter Pasta Quantity: "))

# Calculate food cost
food_total = (burger * qty_burger) + (pizza * qty_pizza) + (pasta * qty_pasta)

# Service Charge (5%)
service_charge = food_total * 0.05

# GST (18%)
gst = food_total * 0.18

# Final Bill
total_bill = food_total + service_charge + gst

# Display Bill
print("\n===== CUSTOMER BILL =====")
print("Food Total       : ₹", food_total)
print("Service Charge   : ₹", service_charge)
print("GST (18%)        : ₹", gst)
print("----------------------------")
print("Total Bill       : ₹", total_bill)
