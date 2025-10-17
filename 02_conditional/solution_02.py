# age = int(input("Enter your age: "))
# day = input("Enter the day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")

# if day == "Wednesday":
#     discount = 2
# else:
#     discount = 0

# if age > 18:
#     price = 12 - discount
# else:
#     price = 8 - discount

# print("Ticket price:", price)

age = int(input("Enter your age: "))
day = input("Enter the day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").lower()

if day == "wednesday" or day == "wed":
    discount = 2
else:
    discount = 0

if age < 19:
    price = 8 - discount
else:
    price = 12 - discount

# print("Price of Ticket is : ", price)
print(f"Price of Ticket is {price}$ and discount is for {discount}$.")