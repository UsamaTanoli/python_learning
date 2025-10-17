import math

pi = math.pi

# def circle_calculation(r):
#     area = f"Area of circle is: {pi * r**2}"
#     circumference = f"Circumference of circle is: {2 * pi * r}"
#     return area, circumference

# # Call the function and print the results on separate lines
# area, circumference = circle_calculation(5)
# print(area)
# print(circumference)




# def circle_calculation(r):
#     area = f"Area of circle is: {pi * r**2}"
#     circumference = f"Circumference of circle is: {2 * pi * r}"
#     return f"{area}\n{circumference}"

# # Call the function and store the result in one variable
# calculate = circle_calculation(3)

# # Print the result, which will show both on separate lines
# print(calculate)




def circle_calculation(r):
    area = f"Area of circle is: {pi * r**2:.3f}"
    circumference = f"Circumference of circle is: {2 * pi * r:.3f}"
    return f"{area}\n{circumference}"

# Call the function and store the result in one variable
calculate = circle_calculation(3)

# Print the result, which will show both on separate lines with 3 decimal places
print(calculate)
