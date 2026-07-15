# Attendance Percentage Calculator

total_classes = int(input("Enter Total Classes Conducted: "))
attended_classes = int(input("Enter Classes Attended: "))

# Calculate attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

# Check eligibility
if attendance_percentage >= 75:
    status = "Eligible for Examination ✅"
else:
    status = "Not Eligible for Examination ❌"

# Display Result
print("\n----- Attendance Report -----")
print(f"Total Classes Conducted : {total_classes}")
print(f"Classes Attended        : {attended_classes}")
print(f"Attendance Percentage   : {attendance_percentage:.2f}%")
print(f"Status                  : {status}")
