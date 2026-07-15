# Hospital BMI Calculator

print("===== Hospital BMI Calculator =====")

weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

# BMI Calculation
bmi = weight / (height ** 2)

# BMI Classification
if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal Weight"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

# Display Result
print("\n===== BMI REPORT =====")
print("BMI =", round(bmi, 2))
print("Health Status =", status)
