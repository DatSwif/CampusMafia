import pygame
import TextBox
import Colors

class HealthBar(object):
    def __init__(self, scr):
        self.scr = scr

    def update(self, HP, maxHP):
        if HP <= 0:
            HP = 1
        background = pygame.Surface((350, 50))
        background.set_alpha(200)
        background.fill(Colors.BLACK)
        HP_strip_top = pygame.Surface((346*HP/maxHP, 33))
        HP_strip_top.fill(Colors.RED)
        HP_strip_bot = pygame.Surface((346*HP/maxHP, 13))
        HP_strip_bot.fill(Colors.RED127)
        
        max_width, max_height = self.scr.get_size()
        topLeft = ((max_width-350)//2,
                   max_height-100)

        text = f'{round(HP, 1)}/{round(maxHP)}'
        textObj, textRect = TextBox.TextBox.makeTextObj(text, (topLeft[0], topLeft[1]-3), (0, 0), (200, 50), 25, Colors.WHITE)

        self.scr.blit(background, topLeft)
        self.scr.blit(HP_strip_top, (topLeft[0]+2, topLeft[1]+2))
        self.scr.blit(HP_strip_bot, (topLeft[0]+2, topLeft[1]+35))
        self.scr.blit(textObj, textRect) 

class WeaponSlot:
    def __init__(self, scr, player, number):
        self.scr = scr
        self.player = player
        self.number = number
        self.dimensions = (200, 104)

    def update(self):
        topLeft = (self.scr.get_size()[0]-228-4,
                   self.scr.get_size()[1]-128*(self.number+1)-4)

        background = pygame.Surface(self.dimensions)
        background.set_alpha(50)
        background.fill(Colors.BLACK)

        self.scr.blit(background, topLeft)

        if self.player.selectedWeapon == self.number:
            pygame.draw.rect(self.scr, Colors.GRAY127, (topLeft, self.dimensions), width=2)

        if self.player.weapons[self.number] is not None:
            image = self.player.weapons[self.number].inv_image
            self.scr.blit(image, (topLeft[0]+2, topLeft[1]+2))

class AccessorySlot:
    def __init__(self, scr, player, number):
        self.scr = scr
        self.player = player
        self.number = number
        self.dimensions = (64, 64)

    def update(self):
        topLeft = (32+72*self.number,
                   self.scr.get_size()[1]-96)

        background = pygame.Surface(self.dimensions)
        background.set_alpha(50)
        background.fill(Colors.BLACK)

        self.scr.blit(background, topLeft)
        
        if self.player.selectedAccessory == self.number:
            pygame.draw.rect(self.scr, Colors.GRAY127, (topLeft, self.dimensions), width=2)

        if self.player.accessories[self.number] is not None:
            image = self.player.accessories[self.number].inv_image
            self.scr.blit(image, topLeft)

class InGameUI(object):
    """description of class"""
    def __init__(self, scr, mouse, keyboard, fscr_offset, player):
        self.scr = scr
        self.mouse = mouse
        self.keyboard = keyboard
        self.fscr_offset = fscr_offset

        self.player = player

        self.weaponSlots = [WeaponSlot(scr, player, 0), WeaponSlot(scr, player, 1)]
        self.accessorySlots = [AccessorySlot(scr, player, 0), AccessorySlot(scr, player, 1), AccessorySlot(scr, player, 2)]
        self.healthBar = HealthBar(scr)
        self.crosshair = pygame.image.load('assets/images/crosshair.png').convert_alpha()
        self.crosshairRect = self.crosshair.get_rect()

    def update(self):
        self.healthBar.update(self.player.HP, self.player.maxHP)
        for slot in self.weaponSlots:
            slot.update()
        for slot in self.accessorySlots:
            slot.update()

        self.crosshairRect.center = (self.mouse.x, self.mouse.y)
        self.scr.blit(self.crosshair, self.crosshairRect)