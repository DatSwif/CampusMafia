import Character
import pygame.image
import Weapon

class Player(Character.Character):
    """description of class"""
    def __init__(self, scr, mouse, keyboard, abs_topLeft, fscr_offset, dimensions):
        sprites = [pygame.image.load('assets/Characters/player_s_idle.png')]
        baseMaxHP = 100
        baseArmor = 0
        baseSpeed = 3
        baseDamage = 0
        super().__init__(scr, abs_topLeft, fscr_offset, dimensions, sprites, baseMaxHP, baseArmor, baseSpeed, baseDamage)
        self.baseMaxHP = self.maxHP
        self.baseArmor = self.armor
        self.baseSpeed = self.speed
        self.baseDamage = self.damage

        self.mouse = mouse
        self.keyboard = keyboard
        self.weapons = [Weapon.Weapon('Штурмова гвинтівка'), None]
        self.selectedWeapon = 0

        self.accessories = [None, None, None]
        self.selectedAccessory = 0

        self.rel_topLeft = (650-32, 375-64)

    def getDamaged(self, damage, knockback, kb_direction):
        inertia_x = kb_direction[0]*knockback
        if abs(self.inertia_x) < abs(inertia_x):
            self.inertia_x = inertia_x
        inertia_y = kb_direction[1]*knockback
        if abs(self.inertia_y) < abs(inertia_y):
            self.inertia_y = inertia_y
        super().getDamaged(damage)

    def update(self, walls):
        intent_vector_x = 0
        intent_vector_y = 0
        if self.keyboard.left is not False:
            intent_vector_x -= 1
        if self.keyboard.right is not False:
            intent_vector_x += 1
        if self.keyboard.up is not False:
            intent_vector_y -= 1
        if self.keyboard.down is not False:
            intent_vector_y += 1
        if intent_vector_x != 0 and intent_vector_y != 0:
            intent_vector_x *= 2**0.5/2
            intent_vector_y *= 2**0.5/2

        if self.keyboard.shift:
            self.selectedWeapon = 1 - self.selectedWeapon
        if self.keyboard.num1:
            self.selectedAccessory = 0
        if self.keyboard.num2:
            self.selectedAccessory = 1
        if self.keyboard.num3:
            self.selectedAccessory = 2

        super().update()
        self.armor = self.baseArmor
        self.speed = self.baseSpeed
        self.maxHP = self.baseMaxHP
        self.damage = self.baseDamage
        for accessory in self.accessories:
            if accessory is not None:
                self.speed += accessory.speedBoost
                self.maxHP *= (1 + accessory.healthBoost)
                self.damage *= (1 + accessory.damageBoost)
                self.armor += accessory.armorBoost

        self.inertia_x *= 0.9
        self.inertia_y *= 0.9
        if abs(self.inertia_x) < 1:
            self.inertia_x = 0
        if abs(self.inertia_y) < 1:
            self.inertia_y = 0

        old_abs_topLeft = self.abs_topLeft
        self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_vector_x*self.speed, 
                            old_abs_topLeft[1] + self.inertia_y + intent_vector_y*self.speed)
        while abs(self.inertia_x) > 1 or abs(self.inertia_y > 1):
            collision = False
            for wall in walls:
                if wall.intersects(self):
                    collision = True
            if collision:
                self.inertia_x *= 0.9
                self.inertia_y *= 0.9
                self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_vector_x*self.speed, 
                                    old_abs_topLeft[1] + self.inertia_y + intent_vector_y*self.speed)
            else:
                break
        
        if abs(self.inertia_x) < 1:
            self.inertia_x = 0
        if abs(self.inertia_y) < 1:
            self.inertia_y = 0
    
        self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_vector_x*self.speed, 
                            old_abs_topLeft[1] + self.inertia_y + intent_vector_y*self.speed)
        collision = False
        for wall in walls:
            if wall.intersects(self):
                collision = True

        if collision:
            #collision_y
            self.abs_topLeft = (old_abs_topLeft[0],
                                old_abs_topLeft[1] + self.inertia_y + intent_vector_y*self.speed)
            collision_y = False
            for wall in walls:
                if wall.intersects(self):
                    collision_y = True
            if collision_y:
                #collision_x
                self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_vector_x*self.speed, 
                                    old_abs_topLeft[1])
                collision_x = False
                for wall in walls:
                    if wall.intersects(self):
                        collision_x = True
                if collision_x:
                    #collision_xy
                    self.abs_topLeft = old_abs_topLeft

    def render(self):
        self.scr.blit(self.sprites[0], (self.fscr_offset[0]+self.rel_topLeft[0], self.fscr_offset[1]+self.rel_topLeft[1]))