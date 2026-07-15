# Electricity Bill Generator

print("===== Electricity Bill Generator =====")

units = int(input("Enter Electricity Units Consumed: "))

bill = 0

# Slab-wise tariff calculation
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)

print("\n===== Electricity Bill =====")
print("Units Consumed :", units)
print("Total Bill Amount : ₹", bill)
