class Bot:
    def __init__(self, name, age, weight, shield, energy):
        self.name = name
        self.age = age
        self.weight = weight
        self.shield = shield
        self.energy = energy

    def display_name(self):
        print(self.name)

    def display_age(self):
        print(self.age)

    def display_energy(self):
        print(self.energy)

    def display_shield(self):
        print(self.shield)
    
    def display_summary(self):
        print("{} is {} years old and weighs {}kg, has shield level of {} and energy level of {}".format(self.name,self.age,  self.weight, self.shield, self.energy))

    def __str__(self):
        return "{} is {} years old and weighs {}kg, has shield level of {} and energy level of {}". format(self.name,self.age, self.weight, self.shield, self.energy)



 

    def get_age(self):
        return self.age
    def get_energy(self):
        return self.energy
    def get_shield(self):
        return self.shield



    def decrement_energy(self):
        self.energy = self.energy-1
        #energy -=1
    
    def decrement_shield(self):
        self.shield -=1

    def increment_age(self):
        self.age +=1

    def increment_energy(self):
        self.energy +=1

    def increment_shield(self):
        self.shield +=1

    def set_name (self, name):
        self.name = name



