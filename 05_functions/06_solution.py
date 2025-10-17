#Lambda functions, also known as anonymous functions, are small, unnamed functions that 
#can be defined in a single line. They are often used for simple operations
#that don't require a full function definition.

#Syntax: lambda arguments: expression

addition = lambda number1, number2: number1 + number2
print(addition(33, 44))

cube = lambda num: num ** 3
print(cube(3))



numbers = [1, 2, 3, 4, 5, 6]

# Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object to a list
even_numbers_list = list(even_numbers)

print(even_numbers_list)  # Output: [2, 4, 6]

