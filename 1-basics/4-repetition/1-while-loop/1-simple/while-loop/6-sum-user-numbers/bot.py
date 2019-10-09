print("How many numbers should I sum up?")
num = int(input())

count = 0
total = 0

while count < num:
    count+=1
    print("Please enter number " + str(count) + " of " + str(num))
    userNum = int(input())
    total+=userNum    # total = total + userNum

print("The answer is " + str(total))
