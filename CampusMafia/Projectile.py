import Hitbox
import pygame.draw

class Projectile(object):
    """description of class"""
    def __init__(self, scr, origin, direction, fscr_offset, player, color, speed, damage, damageLoss, knockback, enemies, walls):
        self.scr = scr
        self.absPos = origin
        self.direction = direction
        self.fscr_offset = fscr_offset
        self.player = player
        self.color = color
        self.speed = speed
        self.damage = damage
        self.damageLoss = damageLoss
        self.knockback = knockback
        self.enemies = enemies
        self.walls = walls

        self.trace = [Hitbox.Hitbox(None, (self.absPos[0]+self.direction[0]*i*3, self.absPos[1]+self.direction[1]*i*3), None, (3, 3), None) for i in range(12)]
        
    def update(self):
        self.damage *= (1-self.damageLoss)
        self.knockback *= (1-self.damageLoss)
        for i, point in enumerate(self.trace):
            self.trace[i].abs_topLeft = (point.abs_topLeft[0]+self.direction[0]*self.speed,
                                         point.abs_topLeft[1]+self.direction[1]*self.speed)
        collision = False
        for enemy in self.enemies:
            for point in self.trace:
                if point.intersects(enemy):
                    collision = True
                    enemy.getDamaged(self.damage, self.knockback, self.direction)
                    break
            if collision:
                break
        for wall in self.walls:
            for point in self.trace:
                if point.intersects(wall):
                    collision = True
                    break
            if collision:
                break
        return collision

    def render(self):
        map_x = self.player.rel_topLeft[0] + self.fscr_offset[0] - self.player.abs_topLeft[0]
        map_y = self.player.rel_topLeft[1] + self.fscr_offset[1] - self.player.abs_topLeft[1]
        for point in self.trace:
            pygame.draw.rect(self.scr, self.color, ((map_x+point.abs_topLeft[0], map_y+point.abs_topLeft[1]), point.dimensions))