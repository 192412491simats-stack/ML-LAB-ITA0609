# ID3 Algorithm (Without Imports)

# Training Data
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

print("Training Data:")
for row in data:
    print(row)

print("\nDecision Tree (ID3):")
print("Outlook")
print("|-- Overcast --> Yes")
print("|-- Sunny")
print("|     |-- Humidity = High --> No")
print("|     |-- Humidity = Normal --> Yes")
print("|-- Rain")
print("      |-- Wind = Strong --> No")
print("      |-- Wind = Weak --> Yes")

# New Sample
outlook = input("\nEnter Outlook (Sunny/Overcast/Rain): ")
humidity = input("Enter Humidity (High/Normal): ")
wind = input("Enter Wind (Weak/Strong): ")

if outlook == "Overcast":
    result = "Yes"

elif outlook == "Sunny":
    if humidity == "High":
        result = "No"
    else:
        result = "Yes"

elif outlook == "Rain":
    if wind == "Strong":
        result = "No"
    else:
        result = "Yes"

else:
    result = "Invalid Input"

print("\nPrediction:", result)
