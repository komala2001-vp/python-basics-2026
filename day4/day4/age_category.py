# This program checks whether a person is Child, Teen, or Adult

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
else:
    print("Adult")
