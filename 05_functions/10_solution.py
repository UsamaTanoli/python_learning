def factroial(n):
    if n == 0:
        return 1
    else:
        return n * factroial(n - 1)

print(factroial(5))


##################################################################

def another_factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

result = another_factorial(5)
print(result, ": By Iterative method")