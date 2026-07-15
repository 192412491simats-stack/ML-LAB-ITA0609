# Weather Data Analyzer

temperatures = []

print("Enter temperatures for 7 days:")

for i in range(7):
    temp = float(input(f"Day {i+1} Temperature (°C): "))
    temperatures.append(temp)

# Calculations
maximum = max(temperatures)
minimum = min(temperatures)
average = sum(temperatures) / len(temperatures)

# Display Results
print("\n----- Weather Report -----")
print("Temperatures:", temperatures)
print(f"Maximum Temperature : {maximum:.2f} °C")
print(f"Minimum Temperature : {minimum:.2f} °C")
print(f"Average Temperature : {average:.2f} °C")
