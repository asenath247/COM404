from bot import Bot


class SuperBot (Bot):
    def __init__(self, name, age, weight, shield, energy, powerLevel): 
        super().__init__(name, age, weight,shield, energy)
        self.super_power_level = powerLevel

        
        
    def get_super_power_level(self):
        return self.super_power_level

    def set_super_power_level(self, powerLevel):
        self.super_power_level = powerLevel
        

