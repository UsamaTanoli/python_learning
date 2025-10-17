input_str = input("Enter string with atleast one non-repeatable char: ")

for char in input_str:
    if input_str.count(char) == 1:
        print(f"Character is {char}")
        break
    # print(input_str.count(char))