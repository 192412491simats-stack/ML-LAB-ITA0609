# Inventory Stock Management

print("===== Inventory Stock Management =====")

product_name = input("Enter Product Name: ")
stock = int(input("Enter Current Stock: "))
minimum_stock = int(input("Enter Minimum Stock Level: "))

print("\n===== Inventory Report =====")
print("Product Name :", product_name)
print("Current Stock :", stock)
print("Minimum Stock :", minimum_stock)

if stock < minimum_stock:
    print("⚠ Low Stock Alert! Reorder Required.")
else:
    print("✓ Stock Level is Sufficient.")
