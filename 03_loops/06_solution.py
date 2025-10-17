# number_input = int(input("Enter number to and number should be > 0: "))
# factorial = 1

# if number_input == 0:
#     print("Factorial of 0 is 1")
# elif number_input < 0:
#     print("Please don't give -(negetive) Numbers")
# else:
#     while number_input > 0:
#         factorial = factorial * number_input
#         number_input = number_input -1
#     # print(factorial)
#     print(f"Factorial of {number_input} is {factorial}")


# number_input = int(input("Enter a number greater than 0: "))
# factorial = 1

# if number_input == 0:
#     print("Factorial of 0 is 1")
# elif number_input < 0:
#     print("Please don't give negative numbers")
# else:
#     temp = number_input  # To preserve the original input
#     while temp > 0:
#         factorial *= temp  # Multiply factorial by the current value
#         temp -= 1  # Decrease the value of temp
#     print(f"Factorial of {number_input} is {factorial}")



number_input = int(input("Enter a number greater than 0: "))
factorial = 1

if number_input == 0:
    print("Factorial of 0 is 1")
elif number_input < 0:
    print("Please don't give negative numbers")
else:
    i = 1
    while i <= number_input:
        factorial *= i  # Multiply factorial by the current value of i
        i += 1  # Increment i
    print(f"Factorial of {number_input} is {factorial}")
