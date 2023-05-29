import Hitbox

class Character(Hitbox.Hitbox):
    """description of class"""
    def __init__(self, scr, abs_topLeft, fscr_offset, dimensions, sprites, baseMaxHP, baseArmor, baseSpeed, baseDamage):
        super().__init__(scr, abs_topLeft, fscr_offset, dimensions, sprites)
        self.HP = baseMaxHP
        self.maxHP = baseMaxHP
        self.armor = baseArmor
        self.speed = baseSpeed
        self.damage = baseDamage

        self.inertia_x = 0
        self.inertia_y = 0

        self.isAlive = True
        self.HP_regen = 0

    def update(self):
        if self.HP < self.maxHP:
            self.HP_regen = self.HP_regen + 0.0001
            if self.HP_regen > 0.02:
                self.HP_regen = 0.02

        self.HP += self.HP_regen
        if self.HP > self.maxHP:
            self.HP = self.maxHP
            self.HP_regen = 0

    def getDamaged(self, damage):
        self.HP_regen = 0
        if self.armor < damage:
            self.HP -= (damage - self.armor)
        if self.HP < 0:
            self.isAlive = False