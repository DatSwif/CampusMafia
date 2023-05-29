import TextBox
import Button
import OptionsMenu
import pygame
import Colors

class MainMenu(object):
    """description of class"""
    def __init__(self, scr, mouse, keyboard, fscr_offset, maxOffset):
        self.scr = scr
        self.mouse = mouse
        self.keyboard = keyboard
        self.fscr_offset = fscr_offset
        self.maxOffset = maxOffset

        self.backgroundImage = pygame.transform.scale(pygame.image.load('assets/images/kpi_image.png'), self.scr.get_size())

        self.title = TextBox.TextBox(scr,
                                     topLeft=(8*50, 2*50),
                                     dimensions=(10*50, 50),
                                     fscr_offset=fscr_offset,
                                     text="Мафія на кампусі",
                                     textSize=40,
                                     textColor=Colors.BLACK,
                                     bgAlpha=0)
        self.levelsButton = Button.Button(mouse,
                                          scr, 
                                          topLeft=(7*50, 5*50),
                                          dimensions=(6*50, 50),
                                          fscr_offset=fscr_offset,
                                          text="Рівні",
                                          textSize=18,
                                          borderColor=Colors.ButtonBorderDefault,
                                          textColor=Colors.ButtonBorderDefault,
                                          bgAlpha=180)
        self.optionsButton = Button.Button(mouse,
                                           scr, 
                                           topLeft=(7*50, 7*50),
                                           dimensions=(6*50, 50),
                                           fscr_offset=fscr_offset,
                                           text="Налаштування",
                                           textSize=18,
                                           borderColor=Colors.ButtonBorderDefault,
                                           textColor=Colors.ButtonBorderDefault,
                                           bgAlpha=180)
        self.optionsMenu = None

    def update(self):
        if self.backgroundImage.get_size() != self.scr.get_size():
            self.backgroundImage = pygame.transform.scale(self.backgroundImage, self.scr.get_size())
        self.scr.blit(self.backgroundImage, (0, 0))

        self.title.update()
        self.levelsButton.update(isBlocked=(self.optionsMenu is not None))
        self.optionsButton.update(isBlocked=(self.optionsMenu is not None))
        if self.optionsButton.isPressed:
            self.optionsMenu = OptionsMenu.OptionsMenu(self.scr, self.mouse, self.keyboard, self.fscr_offset, self.maxOffset)

        if self.optionsMenu is not None:
            self.optionsMenu.update()
            if (self.optionsMenu.closeButton.isPressed) or (self.keyboard.esc is True):
                self.optionsMenu = None