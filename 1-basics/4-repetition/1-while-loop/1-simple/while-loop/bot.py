print("How many cables should I remove?")
cables = int(input())

liveCables = 0

while liveCables < cables:
    print("Avoiding...")
    liveCables += 1
    print("...Done ! " + str(liveCables) + " live cable avoided!")

    print("All live cables have been avoided.")