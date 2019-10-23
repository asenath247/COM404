def is_league_united(hero1,hero2):
    if hero1 == "superman" and hero2 == "wonderwoman":
        return True
    elif hero1 == "wonderwoman" and hero2 == "superman":
        return True
    else: 
        return False

def decide_plan(hero1,hero2):
    if is_league_united(hero1,hero2) == True:
        return "Time to save the world!"
    else:
        return "We must unite the league!"

def run():
    print("Enter name of first hero")
    hero1 = input()
    print("Enter name of second hero")
    hero2 = input()
    print("Please enter league or plan")
    userChoice = input()
    if userChoice == "league":
        print(is_league_united(hero1, hero2))
    elif userChoice == "plan":
        print(decide_plan(hero1, hero2))
    else:
        print("Invalid command. Please try again")

run()


