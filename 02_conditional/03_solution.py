score = int(input("Enter your score: "))

if score > 100:
    grade = "Out of score book!"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "Fail"

if grade == "A" or grade == "B" or grade == "C" or grade == "D":
    print(f"Your Grade Is: {grade}")
elif grade == "Out of score book!":
    print(f"{grade}")
else:
    print(f"{grade}: please keep smart work because i know you did very hardwork")
