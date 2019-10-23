health = 100
print("Your health is 100%. Escape is in progress...")

for count in range (0,5,1):
    print("…Oh dear, who is that?")
    name = input()
    if name == "Smiler's Bot":
        health -=20
        print("Time to jam out of here!")
    elif name == "Hacker":
        health +=20
        print("Yay! Better follow this one!")
else:
    print("Phew, just another emoji!")

print("Escaped! Health is" + str(health) +"%")
