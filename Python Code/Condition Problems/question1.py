age = int(input("Give me your age: "))

if age in range(0, 13):
    print("Child")
elif age in range(13, 19):
    print("Teenager")
elif age in range(19, 59):
    print("Adult")
elif age >= 59:
    print("Senior")