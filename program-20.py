# Movie Ticket Booking System

print("===== Movie Ticket Booking System =====")

name = input("Enter Customer Name: ")

print("\nSeat Categories")
print("1. Silver  - ₹150")
print("2. Gold    - ₹250")
print("3. Platinum - ₹400")

choice = int(input("Enter Seat Category (1/2/3): "))
seats = int(input("Enter Number of Seats: "))

# Ticket Price
if choice == 1:
    category = "Silver"
    price = 150
elif choice == 2:
    category = "Gold"
    price = 250
elif choice == 3:
    category = "Platinum"
    price = 400
else:
    print("Invalid Choice!")
    exit()

total = seats * price

# Discount
if total >= 2000:
    discount = total * 0.10      # 10%
elif total >= 1000:
    discount = total * 0.05      # 5%
else:
    discount = 0

final_amount = total - discount

print("\n===== BOOKING DETAILS =====")
print("Customer Name :", name)
print("Seat Category :", category)
print("Number of Seats :", seats)
print("Ticket Cost : ₹", total)
print("Discount : ₹", discount)
print("Final Amount : ₹", final_amount)
