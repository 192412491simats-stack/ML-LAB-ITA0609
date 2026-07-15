# Vehicle Fuel Cost Estimator

distance = float(input("Enter distance to travel (km): "))
mileage = float(input("Enter vehicle mileage (km per liter): "))
fuel_price = float(input("Enter fuel price per liter (₹): "))

# Calculations
fuel_needed = distance / mileage
total_cost = fuel_needed * fuel_price

# Output
print("\n----- Fuel Cost Estimation -----")
print(f"Distance: {distance} km")
print(f"Mileage: {mileage} km/l")
print(f"Fuel Needed: {fuel_needed:.2f} liters")
print(f"Fuel Cost: ₹{total_cost:.2f}")
