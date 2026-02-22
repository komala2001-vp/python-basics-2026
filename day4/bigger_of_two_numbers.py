#  Find the Bigger of Two Numbers
# This program uses if-elif-else condition

# Taking input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Checking which number is bigger
if num1 > num2:
    print("The bigger number is:", num1)

elif num2 > num1:
    print("The bigger number is:", num2)

else:
    print("Both numbers are equal")
