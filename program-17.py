# Password Strength Checker

print("===== Password Strength Checker =====")

password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True

if (len(password) >= 8 and has_upper and has_lower
        and has_digit and has_special):
    print("\nStrong Password")
else:
    print("\nWeak Password")

print("\nPassword Requirements:")
print("✓ Minimum 8 characters")
print("✓ At least 1 uppercase letter")
print("✓ At least 1 lowercase letter")
print("✓ At least 1 digit")
print("✓ At least 1 special character")
