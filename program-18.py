# Blood Donation Eligibility Checker

print("===== Blood Donation Eligibility Checker =====")

age = int(input("Enter Age: "))
weight = float(input("Enter Weight (kg): "))
hemoglobin = float(input("Enter Hemoglobin Level (g/dL): "))

# Eligibility Check
if age >= 18 and age <= 65 and weight >= 50 and hemoglobin >= 12.5:
    print("\nEligible for Blood Donation")
else:
    print("\nNot Eligible for Blood Donation")
