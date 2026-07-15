# Online Voting Eligibility Checker

print("===== Online Voting Eligibility Checker =====")

age = int(input("Enter Age: "))
nationality = input("Enter Nationality: ")

# Check Eligibility
if age >= 18 and nationality.lower() == "indian":
    print("\nEligible to Vote")
else:
    print("\nNot Eligible to Vote")
