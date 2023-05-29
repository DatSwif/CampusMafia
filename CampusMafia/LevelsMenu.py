import TextBox
import Button
import Colors
import pygame

class LevelsMenu(object):
    """description of class"""
    def __init__(self, scr, mouse, keyboard, fscr_offset):
        self.scr = scr
        self.mouse = mouse
        self.keyboard = keyboard
        self.fscr_offset = fscr_offset
        
        self.backgroundImage = pygame.transform.scale(pygame.image.load('assets/images/kpi_image.png'), self.scr.get_size())

        self.title = TextBox.TextBox(scr,
                                     topLeft=(8*50, 2*50),
                                     dimensions=(10*50, 50),
                                     fscr_offset=fscr_offset,
                                     text="Рівні",
                                     textSize=40,
                                     textColor=Colors.BLACK,
                                     bgAlpha=0)
        self.levelButtons = [
            Button.Button(mouse,
                          scr,
                          topLeft=(11*50+25, 6*50),
                          dimensions=(3*50, 50),
                          fscr_offset=fscr_offset,
                          text="Демо",
                          borderColor=Colors.ButtonBorderDefault,
                          textColor=Colors.ButtonBorderDefault,
                          bgAlpha=160)]
        self.backButton = Button.Button(mouse,
                                        scr,
                                        topLeft=(20*50, 12*50),
                                        dimensions=(3*50, 50),
                                        fscr_offset=fscr_offset,
                                        text="Назад",
                                        textSize=18,
                                        borderColor=Colors.ButtonBorderDefault,
                                        textColor=Colors.ButtonBorderDefault,
                                        bgAlpha=160)
    def update(self):
        if self.backgroundImage.get_size() != self.scr.get_size():
            self.backgroundImage = pygame.transform.scale(self.backgroundImage, self.scr.get_size())
        self.scr.blit(self.backgroundImage, (0, 0))

        self.title.update()
        for b in self.levelButtons:
            b.update()
        self.backButton.update()