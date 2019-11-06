from bot2 import SuperBot


class FlyingBot (SuperBot):
     def __init__(self, name, age, weight,shield, energy, powerLevel, hoverDistance): 
        super().__init__(name, age, weight,shield, energy, powerLevel)
        self.hover_distance = hoverDistance

        def get_hover_distance(self):
            return self.hover_distance

        def set_hover_distance(self, hoverDistance):
            self.hover_distance = hoverDistance

fb = FlyingBot("asenath", 18, "don't know",100,100, 78, 5)

fb.display_summary()

