# Railway Ticket Fare Calculator

print("===== Railway Ticket Fare Calculator =====")

distance = float(input("Enter Distance (km): "))
age = int(input("Enter Age: "))

print("\nSelect Class")
print("1. Sleeper")
print("2. AC")
choice = int(input("Enter Choice (1/2): "))

# Base fare per km
if choice == 1:
    fare = distance * 1.5
    class_name = "Sleeper"
elif choice == 2:
    fare = distance * 3
    class_name = "AC"
else:
    print("Invalid Choice")
    exit()

# Concessions
if age < 12:
    discount = fare * 0.50      # 50% discount
elif age >= 60:
    discount = fare * 0.40      # 40% discount
else:
    discount = 0

final_fare = fare - discount

# Display Result
print("\n===== TICKET DETAILS =====")
print("Class :", class_name)
print("Distance :", distance, "km")
print("Base Fare : ₹", fare)
print("Discount : ₹", discount)
print("Final Fare : ₹", final_fare)
