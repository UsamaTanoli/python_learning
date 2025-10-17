user_age = int(input("TYPE YOUR AGE: "))

if user_age < 13:
    print("you are 'Child'!")
elif user_age < 20:
    print("you are 'Teen Ager'!")
elif user_age < 60:
    print("you are 'Adult'!")
else:
     print("You are senior citizen")