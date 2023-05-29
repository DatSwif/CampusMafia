import InGame
import LevelsMenu
import MainMenu
import pygame
import Colors

class ScrSwitcher(object):
    """switching between menus and levels"""
    def __init__(self, scr, mouse, keyboard, windowedDimensions, fullscreenDimensions):
        self.scr = scr
        self.mouse = mouse
        self.keyboard = keyboard

        #camera options
        self.windowedDimensions = windowedDimensions
        self.fullscreenDimensions = fullscreenDimensions
        self.windowed = True
        self.fscr_offset = [0, 0]
        self.maxOffset = (abs(self.windowedDimensions[0] - self.fullscreenDimensions[0])//2, abs(self.windowedDimensions[1] - self.fullscreenDimensions[1])//2)

        self.inGame = None
        self.mainMenu = MainMenu.MainMenu(scr, mouse, keyboard, self.fscr_offset, self.maxOffset)
        self.levelsMenu = None

    def update(self):
        """update all the elements"""
        #check for fullscreen
        if self.keyboard.F11 is True:
            if self.windowed is True:
                self.windowed = False
                self.scr = pygame.display.set_mode(self.fullscreenDimensions, pygame.FULLSCREEN)
                self.fscr_offset[0] = abs(self.windowedDimensions[0] - self.fullscreenDimensions[0])//2
                self.fscr_offset[1] = abs(self.windowedDimensions[1] - self.fullscreenDimensions[1])//2
            else:
                self.windowed = True
                self.scr = pygame.display.set_mode(self.windowedDimensions)
                self.fscr_offset[0] = 0
                self.fscr_offset[1] = 0

        #update main menu
        if self.mainMenu is not None:
            self.mainMenu.update()
            if self.mainMenu.levelsButton.isPressed:
                self.mainMenu = None
                self.levelsMenu = LevelsMenu.LevelsMenu(self.scr, self.mouse, self.keyboard, self.fscr_offset)
        
        #update levels menu
        if self.levelsMenu is not None:
            self.levelsMenu.update()
            for i, b in enumerate(self.levelsMenu.levelButtons):
                if b.isPressed:
                    self.levelsMenu = None
                    self.inGame = InGame.InGame(self.scr, self.mouse, self.keyboard, self.fscr_offset, self.maxOffset, level=i)
                    pygame.mouse.set_visible(False)
            if self.levelsMenu is not None:
                if (self.levelsMenu.backButton.isPressed) or (self.keyboard.esc == True):
                    self.levelsMenu = None
                    self.mainMenu = MainMenu.MainMenu(self.scr, self.mouse, self.keyboard, self.fscr_offset, self.maxOffset)
        
        #update ingame screen
        if self.inGame is not None:
            if self.inGame.level.player.isAlive is False:
                self.inGame = None
                pygame.mouse.set_visible(True)
                pygame.draw.rect(self.scr, Colors.RED, pygame.Rect((0, 0), self.scr.get_size()))
                self.mainMenu = MainMenu.MainMenu(self.scr, self.mouse, self.keyboard, self.fscr_offset, self.maxOffset)
            else:
                self.inGame.update()
                if self.inGame.inGameMenu is not None:
                    if self.inGame.inGameMenu.quitButton.isPressed:
                        self.inGame = None
                        pygame.mouse.set_visible(True)
                        self.mainMenu = MainMenu.MainMenu(self.scr, self.mouse, self.keyboard, self.fscr_offset, self.maxOffset)