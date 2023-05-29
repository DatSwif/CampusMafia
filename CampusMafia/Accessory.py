import Item

class Accessory(Item.Item):
    """description of class"""
    def __init__(self, name):
        super().__init__(name)
        if name == 'снікерс':
            self.damageBoost = 0.1
            self.healthBoost = 0.1
            self.speedBoost = 0
            self.armorBoost = 0
        elif name == 'Окуляри':
            self.damageBoost = 0
            self.healthBoost = 0
            self.speedBoost = 0
            self.armorBoost = 3
        elif name == 'Ролики':
            self.damageBoost = 0
            self.healthBoost = 0
            self.speedBoost = 3
            self.armorBoost = 1