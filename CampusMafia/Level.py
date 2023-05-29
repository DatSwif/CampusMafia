import pygame.image
import pygame.draw

import Player
import Weapon
import Accessory
import Pickup
import Note
import Colors
import Wall
import Enemy

class Level(object):
    """description of class"""
    def __init__(self, scr, mouse, keyboard, fscr_offset, level):
        self.scr = scr

        self.mouse = mouse
        self.keyboard = keyboard
        self.fscr_offset = fscr_offset

        self.map_x = 0
        self.map_y = 0

        self.player = Player.Player(scr, self.mouse, self.keyboard,  (360, 275), fscr_offset, (64, 128))

        self.structures, self.walls, self.enemies, self.map = self.getLevel(level, scr, fscr_offset, self.player)
        for enemy in self.enemies:
            enemy.load_surroundings(self.enemies, self.walls)

        self.currNote = None
        self.noteOpened = False

    def update(self, paused):
        pygame.draw.rect(self.scr, Colors.BLACK, ((0, 0), self.scr.get_size()))
        self.noteOpened = False
        if paused is False and self.currNote is None:
            self.player.update(self.walls)
            for i, weapon in enumerate(self.player.weapons):
                if weapon is not None:
                    self.player.weapons[i].update()
            self.map_x = self.player.rel_topLeft[0] + self.fscr_offset[0] - self.player.abs_topLeft[0]
            self.map_y = self.player.rel_topLeft[1] + self.fscr_offset[1] - self.player.abs_topLeft[1]
            if (self.mouse.left is True) and (self.player.weapons[self.player.selectedWeapon] is not None):
                directionStart = (self.player.rel_topLeft[0]+self.player.dimensions[0]/2,
                                  self.player.rel_topLeft[1]+self.player.dimensions[1]/2)
                direction = (self.mouse.x - directionStart[0],
                             self.mouse.y - directionStart[1])
                origin = (self.player.abs_topLeft[0]+self.player.dimensions[0]/2,
                          self.player.abs_topLeft[1]+self.player.dimensions[1]/2)
                self.player.weapons[self.player.selectedWeapon].tryShoot(self.scr, self.player, origin, direction, self.fscr_offset, self.player, self.enemies, self.walls)
            for enemy in self.enemies:
                enemy.update()
            if (self.keyboard.action is True) or (self.mouse.right is True):
                for obj in self.structures:
                    if not isinstance(obj, Wall.Wall):
                        if obj.isReachable(self.player):
                            if isinstance(obj, Pickup.Pickup):
                                item = obj.get_loot()
                                if isinstance(item, Weapon.Weapon):
                                    self.player.weapons[self.player.selectedWeapon] = item
                                elif isinstance(item, Accessory.Accessory):
                                    self.player.accessories[self.player.selectedAccessory] = item
                            elif isinstance(obj, Note.Note):
                                self.currNote = obj
                                self.noteOpened = True

        for obj in self.map:
            for coords in obj[1]:
                self.scr.blit(obj[0], (self.map_x+coords[0], self.map_y+coords[1]))

        for obj in self.structures:
            if not isinstance(obj, Wall.Wall):
                obj.renderStruct(self.player)

        self.player.render()
        for enemy in self.enemies:
            enemy.render()
        for weapon in self.player.weapons:
            if weapon is not None:
                for proj in weapon.projectiles:
                    proj.render()

        if self.currNote is not None:
            if ((self.keyboard.action is True) or (self.mouse.right is True)) and (self.noteOpened is False):
                self.currNote = None
            else:
                self.currNote.render()
        
    @staticmethod
    def getLevel(level, scr, fscr_offset, player):
        #read level data from a file
        structures = [Pickup.Pickup(scr, (175, 181), (32, 32), fscr_offset, Accessory.Accessory('снікерс')),
                      Pickup.Pickup(scr, (375, 181), (32, 32), fscr_offset, Accessory.Accessory('Окуляри')),
                      Pickup.Pickup(scr, (575, 181), (32, 32), fscr_offset, Accessory.Accessory('Ролики')),
                      Pickup.Pickup(scr, (159, 521), (64, 32), fscr_offset, Weapon.Weapon('Дробовик')),
                      Pickup.Pickup(scr, (359, 521), (64, 32), fscr_offset, Weapon.Weapon('Снайперська гвинтівка')),
                      Pickup.Pickup(scr, (559, 521), (64, 32), fscr_offset, Weapon.Weapon('Штурмова гвинтівка')),
                      Note.Note(scr, (775, 181), (32, 32), fscr_offset, 'Ще кнопки', ['Узагалі в меню налаштувань',
                                                                                       'було написано не все.',
                                                                                       'Ще можна натискати',
                                                                                       'Шифт, щоб міняти зброю,',
                                                                                       'та циферки, щоб обрати предмет,',
                                                                                       'який можна замінити.',
                                                                                       '',
                                                                                       'П.С. Якщо в тебе в руці щось є,',
                                                                                       'і ти це міняєш,',
                                                                                       'воно пропаде назавжди. UwU']),
                      Note.Note(scr, (775, 521), (32, 32), fscr_offset, 'Бюджет проєкту', ['Якби за цю гру давали',
                                                                                            'three hundred bucks,',
                                                                                            'а не 10 балів,',
                                                                                            'вона була би краща,',
                                                                                            'а так хавайте що дають'])]
        walls = [Wall.Wall((0, 0), (8, 731)),
                 Wall.Wall((0, 0), (2187, 8)),
                 Wall.Wall((2179, 0), (8, 731)),
                 Wall.Wall((0, 723), (2187, 8)),
                 Wall.Wall((151, 181), (80, 16)),
                 Wall.Wall((351, 181), (80, 16)),
                 Wall.Wall((551, 181), (80, 16)),
                 Wall.Wall((751, 181), (80, 16)),
                 Wall.Wall((151, 521), (80, 16)),
                 Wall.Wall((351, 521), (80, 16)),
                 Wall.Wall((551, 521), (80, 16)),
                 Wall.Wall((751, 521), (80, 16))]
        enemies = [Enemy.Mukha(scr, (2000, 380), fscr_offset, player)]
        map = [(pygame.image.load('assets/images/testlevelbg.png'), [(0, 0)]),
               (pygame.image.load('assets/images/table.png'), [(150, 180),
                                                               (350, 180),
                                                               (550, 180),
                                                               (750, 180),
                                                               (150, 520),
                                                               (350, 520),
                                                               (550, 520),
                                                               (750, 520)])]
        return structures, walls, enemies, map