# Employee Salary Calculator

print("===== Employee Salary Calculator =====")

basic_salary = float(input("Enter Basic Salary: "))

# Calculations
pf = basic_salary * 0.12      # 12% PF
tax = basic_salary * 0.10     # 10% Tax

gross_salary = basic_salary
total_deductions = pf + tax
net_salary = gross_salary - total_deductions

# Display Results
print("\n===== Salary Details =====")
print("Gross Salary :", gross_salary)
print("PF Deduction (12%) :", pf)
print("Tax Deduction (10%) :", tax)
print("Total Deductions :", total_deductions)
print("Net Salary :", net_salary)


