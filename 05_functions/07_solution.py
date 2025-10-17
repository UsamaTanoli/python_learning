def sum_all(*args):
    # return sum(args)
    print(args)
    for i in args:
        print(f"i = {i} and i multiple with 4 {i * 4}")
    return sum(args)

result = sum_all(2,3,5)
print(result)
