print("Please enter the first number")
number = input()

print("Please enter the second number.")
secondNum = input()

if number < secondNum:
    print("The first number is the smallest")
elif secondNum < number:
    print("The second number is smallest")
else:
    print("Both equal")