print("How many bars should be charged.")
bars = int(input())

chargedBars = 0

while chargedBars < bars:
    print("Charging "+"█" * chargedBars)
    chargedBars += 1


print("The battery is fully charged.")

