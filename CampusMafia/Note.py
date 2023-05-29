import Hitbox
import pygame
import Colors
import TextBox

class Note(Hitbox.Hitbox):
    """description of class"""
    def __init__(self, scr, abs_topLeft, dimensions, fscr_offset, name, text):
        self.name = name
        self.text = text
        self.lv_image = pygame.image.load('assets/items/lv_Note.png').convert_alpha()
        self.lit_image = pygame.image.load('assets/items/lit_Note.png').convert_alpha()
        super().__init__(scr, abs_topLeft, fscr_offset, dimensions, None)
        
    def isReachable(self, other : Hitbox.Hitbox):
        x11 = self.abs_topLeft[0]
        y11 = self.abs_topLeft[1]
        x12 = x11+self.dimensions[0]
        y12 = y11+self.dimensions[1]
        
        x21 = other.abs_topLeft[0]
        y21 = other.abs_topLeft[1]
        x22 = x21 + other.dimensions[0]
        y22 = y21 + other.dimensions[1]

        return (x11 < x22+50 and y11 < y22+50 and x12+50 > x21 and y12+50 > y21)

    def renderStruct(self, player):
        rel_topLeft = (player.rel_topLeft[0] + self.fscr_offset[0] - player.abs_topLeft[0] + self.abs_topLeft[0],
                       player.rel_topLeft[1] + self.fscr_offset[1] - player.abs_topLeft[1] + self.abs_topLeft[1])
        if self.isReachable(player):
            textObj, textRect = TextBox.TextBox.makeTextObj(self.name, (0, 0), (0, 0), self.dimensions, 10, Colors.WHITE)
            textRect.center = (rel_topLeft[0] + self.dimensions[0]//2,
                               rel_topLeft[1] - 10)
            self.scr.blit(textObj, textRect)
            self.scr.blit(self.lit_image, rel_topLeft)
        else:
            self.scr.blit(self.lv_image, rel_topLeft)

    def render(self):
        size = self.scr.get_size()
        tint = pygame.Surface(size)
        tint.set_alpha(100)
        tint.fill(Colors.BLACK)
        self.scr.blit(tint, (0, 0))
        self.makeTitle(self.scr, size, self.name)
        for i, line in enumerate(self.text):
            self.makeTextLine(self.scr, size, line, i)

    @staticmethod
    def makeTitle(scr, size, name):
        font = pygame.font.Font('assets/fonts/LLLisa.ttf', 25)
        textObj = font.render(name, True, Colors.WHITE)
        textRect = textObj.get_rect()
        textRect.center = (size[0]//2,
                           100)
        scr.blit(textObj, textRect)

    @staticmethod
    def makeTextLine(scr, size, line, i):
        font = pygame.font.Font('assets/fonts/LLLisa.ttf', 14)
        textObj = font.render(line, True, Colors.WHITE)
        textRect = textObj.get_rect()
        textRect.topleft = (size[0]//3,
                           200+30*i)
        scr.blit(textObj, textRect)