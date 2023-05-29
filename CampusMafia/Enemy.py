import Character
import pygame
import TextBox
import Colors

class Enemy(Character.Character):
    """description of class"""
    def __init__(self, scr, abs_topLeft, fscr_offset, dimensions, sprites, baseMaxHP, baseArmor, baseSpeed, baseDamage, weapon, player):
        super().__init__(scr, abs_topLeft, fscr_offset, dimensions, sprites, baseMaxHP, baseArmor, baseSpeed, baseDamage)
        self.scr = scr
        self.fscr_offset = fscr_offset
        self.player = player
        self.weapon = weapon
        self.isAggro = False
        self.allies = None

    def update(self):
        super().update()

    def load_surroundings(self, allies, walls):
        self.allies = allies
        self.walls = walls

    def getDamaged(self, damage, knockback, kb_direction):
        inertia_x = kb_direction[0]*knockback
        if abs(self.inertia_x) < abs(inertia_x):
            self.inertia_x = inertia_x
        inertia_y = kb_direction[1]*knockback
        if abs(self.inertia_y) < abs(inertia_y):
            self.inertia_y = inertia_y
        if self.isAggro:
            super().getDamaged(damage)

    def checkAggro(self):
        if self.isAlive is False:
            self.isAggro = False
            return
        selfCenter = (self.abs_topLeft[0] + self.dimensions[0]/2,
                      self.abs_topLeft[1] + self.dimensions[1]/2)
        playerCenter = (self.player.abs_topLeft[0] + self.player.dimensions[0]/2,
                        self.player.abs_topLeft[1] + self.player.dimensions[1]/2)
        distance = ((selfCenter[0]-playerCenter[0])**2+(selfCenter[1]-playerCenter[1])**2)**0.5
        if distance < 600:
            self.isAggro = True
        else:
            self.isAggro = False

class Mukha(Enemy):
    def __init__(self, scr, abs_topLeft, fscr_offset, player):
        super().__init__(scr, abs_topLeft, fscr_offset, (128, 128), None, 100, 3, 4, 30, None, player)
        self.image = pygame.image.load('assets/characters/fly.png').convert_alpha()

    def get_intent(self):
        selfCenter = (self.abs_topLeft[0] + self.dimensions[0]/2,
                      self.abs_topLeft[1] + self.dimensions[1]/2)
        playerCenter = (self.player.abs_topLeft[0] + self.player.dimensions[0]/2,
                        self.player.abs_topLeft[1] + self.player.dimensions[1]/2)
        distance = ((selfCenter[0]-playerCenter[0])**2+(selfCenter[1]-playerCenter[1])**2)**0.5
        x = -(selfCenter[0]-playerCenter[0]) / distance
        y = -(selfCenter[1]-playerCenter[1]) / distance
        return (x, y)

    def checkPlayerDamage(self, kb_direction):
        if self.intersects(self.player):
            self.player.getDamaged(self.damage, 40, kb_direction)

    def update(self):
        self.checkAggro()
        if self.isAlive:
            super().update()
        if self.isAggro:
            intent_x, intent_y = self.get_intent()

            self.inertia_x *= 0.9
            self.inertia_y *= 0.9
            if abs(self.inertia_x) < 1:
                self.inertia_x = 0
            if abs(self.inertia_y) < 1:
                self.inertia_y = 0

            old_abs_topLeft = self.abs_topLeft
            self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_x*self.speed, 
                                old_abs_topLeft[1] + self.inertia_y + intent_y*self.speed)
            while abs(self.inertia_x) > 1 or abs(self.inertia_y > 1):
                collision = False
                for wall in self.walls:
                    if wall.intersects(self):
                        collision = True
                if collision:
                    self.inertia_x *= 0.9
                    self.inertia_y *= 0.9
                    self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_x*self.speed, 
                                        old_abs_topLeft[1] + self.inertia_y + intent_y*self.speed)
                else:
                    break
        
            if abs(self.inertia_x) < 1:
                self.inertia_x = 0
            if abs(self.inertia_y) < 1:
                self.inertia_y = 0
    
            self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_x*self.speed, 
                                old_abs_topLeft[1] + self.inertia_y + intent_y*self.speed)
            collision = False
            for wall in self.walls:
                if wall.intersects(self):
                    collision = True

            if collision:
                #collision_y
                self.abs_topLeft = (old_abs_topLeft[0],
                                    old_abs_topLeft[1] + self.inertia_y + intent_y*self.speed)
                collision_y = False
                for wall in self.walls:
                    if wall.intersects(self):
                        collision_y = True
                if collision_y:
                    #collision_x
                    self.abs_topLeft = (old_abs_topLeft[0] + self.inertia_x + intent_x*self.speed, 
                                        old_abs_topLeft[1])
                    collision_x = False
                    for wall in self.walls:
                        if wall.intersects(self):
                            collision_x = True
                    if collision_x:
                        #collision_xy
                        self.abs_topLeft = old_abs_topLeft

            self.checkPlayerDamage((intent_x, intent_y))

    def render(self):
        map_x = self.player.rel_topLeft[0] + self.fscr_offset[0] - self.player.abs_topLeft[0] + self.abs_topLeft[0]
        map_y = self.player.rel_topLeft[1] + self.fscr_offset[1] - self.player.abs_topLeft[1] + self.abs_topLeft[1]
        self.scr.blit(self.image, (map_x, map_y))

        if self.isAlive:
            text = f'{round(self.HP, 1)}/{round(self.maxHP)}'
            textObj, textRect = TextBox.TextBox.makeTextObj(text, (map_x+20, map_y-40), (0, 0), (self.dimensions[0]-20, 40), 10, Colors.WHITE)
            self.scr.blit(textObj, textRect)
            text = 'І.П.'
            textObj, textRect = TextBox.TextBox.makeTextObj(text, (map_x, map_y-40), (0, 0), (30, 40), 10, Colors.WHITE)
            self.scr.blit(textObj, textRect)

            pygame.draw.rect(self.scr, Colors.BLACK, (map_x, map_y-10, self.dimensions[0], 10))
            pygame.draw.rect(self.scr, Colors.RED, (map_x+2, map_y-8, (self.dimensions[0]-4)*self.HP/self.maxHP, 6))