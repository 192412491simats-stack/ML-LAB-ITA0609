# Student Grade Calculator (Shows all grade ranges)

print("Grade System")
print("A : 90 - 100")
print("B : 80 - 89")
print("C : 70 - 79")
print("D : 60 - 69")
print("E : 50 - 59")
print("F : Below 50")

marks = float(input("\nEnter Student Average Marks: "))

if marks >= 90:
    print("Grade = A")
elif marks >= 80:
    print("Grade = B")
elif marks >= 70:
    print("Grade = C")
elif marks >= 60:
    print("Grade = D")
elif marks >= 50:
    print("Grade = E")
else:
    print("Grade = F")
