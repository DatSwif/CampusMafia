import Level
import InGameUI
import InGameMenu
import pygame.image
import pygame.mouse

class InGame(object):
    """description of class"""
    def __init__(self, scr, mouse, keyboard, fscr_offset, maxOffset, level):
        self.scr = scr
        self.mouse = mouse
        self.keyboard = keyboard
        self.fscr_offset = fscr_offset
        self.maxOffset = maxOffset

        self.level = Level.Level(scr, mouse, keyboard, fscr_offset, level)
        self.inGameUI = InGameUI.InGameUI(scr, mouse, keyboard, fscr_offset, self.level.player)
        self.inGameMenu = None

    def update(self):
        if self.inGameMenu is not None:
            self.level.update(paused=True)
            self.inGameUI.update()
            if self.inGameMenu.optionsMenu is None:
                if (self.keyboard.esc is True) or (self.inGameMenu.resumeButton.isPressed):
                    self.inGameMenu = None
                    pygame.mouse.set_visible(False)
            if self.inGameMenu is not None:
                self.inGameMenu.update()
        elif self.keyboard.esc is True:
            self.level.update(paused=True)
            self.inGameUI.update()
            self.inGameMenu = InGameMenu.InGameMenu(self.scr, self.mouse, self.keyboard, self.fscr_offset, self.maxOffset)
            pygame.mouse.set_visible(True)
        else:
            self.level.update(paused=False)
            self.inGameUI.update()