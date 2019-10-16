def display_ladder(value):

    for count in range(value ):
        print("| |")
        print("***")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())

    display_ladder(steps)

create_ladder()



