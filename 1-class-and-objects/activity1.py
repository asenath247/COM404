class Person:
    def __init__(self, name, age=0, weight=0):
        self.name = name
        self.age = age
        self.weight = weight

    def display(self):
        print("{} is {} years old and weighs {} kg".format(self.name, self.age, self.weight))

asenath = Person("Asenath", 18, "Don't know")

