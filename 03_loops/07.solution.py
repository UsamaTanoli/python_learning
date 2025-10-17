# user_input = int(input("Enter a number between 1 and 10: "))
# 
# while user_input <= 0 or user_input >= 11:
#     print("Please enter number b/w 1 and 10")
#     user_input = int(input("Enter Number: "))

# print(f"You have found the number {user_input}")

while True:
    usr_input = int(input("Enter a number between 1 and 10: "))
    if 1 <= usr_input <= 10:
        print(f"You have found the number {usr_input}")
        break
    print("Invalid input. Please enter a number between 1 and 10.")