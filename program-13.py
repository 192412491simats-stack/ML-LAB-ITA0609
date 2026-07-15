# Parking Fee Calculator

vehicle_type = input("Enter Vehicle Type (Bike/Car/Bus): ").lower()
hours = float(input("Enter Parking Duration (hours): "))

# Parking rates per hour
if vehicle_type == "bike":
    rate = 10
elif vehicle_type == "car":
    rate = 30
elif vehicle_type == "bus":
    rate = 50
else:
    print("Invalid Vehicle Type!")
    exit()

# Calculate parking fee
parking_fee = rate * hours

# Output
print("\n----- Parking Fee Details -----")
print("Vehicle Type :", vehicle_type.capitalize())
print("Duration     :", hours, "hours")
print("Rate/Hour    : ₹", rate)
print("Total Fee    : ₹", parking_fee)
