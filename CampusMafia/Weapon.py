import Item
import Projectile
import Colors
import math
import random

class Weapon(Item.Item):
    """description of class"""
    def __init__(self, name):
        super().__init__(name)
        if name == 'Дробовик':
            self.baseDamage = 8
            self.cooldown = 30
            self.damageLoss = 0.1
            self.knockback = 10
            self.projectilesAmount = 3
            self.recoil = 12
            self.projectileColor = Colors.YELLOW

        elif name == 'Штурмова гвинтівка':
            self.baseDamage = 5
            self.cooldown = 10
            self.damageLoss = 0.02
            self.knockback = 20
            self.projectilesAmount = 1
            self.recoil = 6
            self.projectileColor = Colors.ORANGE

        elif name == 'Снайперська гвинтівка':
            self.baseDamage = 15
            self.cooldown = 30
            self.damageLoss = 0
            self.knockback = 4
            self.projectilesAmount = 1
            self.recoil = 3
            self.projectileColor = Colors.PURPLE

        self.projectiles = []
        self.curr_cooldown = 0

    def update(self):
        if self.curr_cooldown > 0:
            self.curr_cooldown -= 1
        for i, proj in enumerate(self.projectiles):
            doDelete = proj.update()
            if doDelete:
                del self.projectiles[i]

    @staticmethod
    def getRealDirection(direction, recoil):
        vectorLength = (direction[0]**2 + direction[1]**2)**0.5
        nDir = (direction[0]/vectorLength, 
                direction[1]/vectorLength)
        radRecoil = recoil / 180 * math.pi
        d = random.uniform(-radRecoil, radRecoil)
        realDir = (nDir[0] * math.cos(d) + nDir[1] * math.sin(d),
                   nDir[1] * math.cos(d) - nDir[0] * math.sin(d))
        return realDir

    def tryShoot(self, scr, shooter, origin, direction, fscr_offset, player, enemies, walls):
        if self.curr_cooldown == 0:
            for i in range(self.projectilesAmount):
                realDirection = self.getRealDirection(direction, self.recoil)
                speed = 30
                self.projectiles.append(Projectile.Projectile(scr, 
                                                              origin=origin, 
                                                              direction=realDirection,
                                                              fscr_offset=fscr_offset,
                                                              player=player,
                                                              color=self.projectileColor,
                                                              speed=speed,
                                                              damage=self.baseDamage+shooter.damage,
                                                              damageLoss=self.damageLoss,
                                                              knockback=self.knockback,
                                                              enemies=enemies,
                                                              walls=walls))
            self.curr_cooldown = self.cooldown