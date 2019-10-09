print("Please enter a number")
num = int(input())

count = num-1
total = num

while count > 0:
    total = total*count
    count-=1

print("The factorial is " +str(total))