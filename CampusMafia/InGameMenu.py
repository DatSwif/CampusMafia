import Button
import TextBox
import Colors
import OptionsMenu

class InGameMenu(object):
    """description of class"""
    def __init__(self, scr, mouse, keyboard, fscr_offset, maxOffset):
        self.scr = scr
        self.mouse = mouse
        self.keyboard = keyboard
        self.fscr_offset = fscr_offset
        self.maxOffset = maxOffset

        self.tint = TextBox.TextBox(scr, 
                                    topLeft=(0-maxOffset[0], 0-maxOffset[1]), 
                                    dimensions=(3840, 2160), 
                                    fscr_offset=fscr_offset, 
                                    bgAlpha=100)
        self.menuBackground = TextBox.TextBox(scr, 
                                              topLeft=(5*50, 4*50), 
                                              dimensions=(16*50, 9*50), 
                                              fscr_offset=fscr_offset, 
                                              bgColor=Colors.BLACK,
                                              bgAlpha=230)
        self.title = TextBox.TextBox(scr, 
                                     topLeft=(10*50, 5*50), 
                                     dimensions=(6*50, 50),
                                     fscr_offset=fscr_offset,
                                     text="Пауза",
                                     bgAlpha=0)
        self.resumeButton = Button.Button(mouse, 
                                          scr, 
                                          topLeft=(7*50, 7*50), 
                                          dimensions=(6*50, 50), 
                                          fscr_offset=fscr_offset, 
                                          text="Відновити",
                                          textSize=18,
                                          borderColor=Colors.ButtonBorderDefault,
                                          textColor=Colors.ButtonBorderDefault,
                                          bgAlpha=180)
        self.optionsButton = Button.Button(mouse,
                                           scr, 
                                           topLeft=(7*50, 9*50),
                                           dimensions=(6*50, 50),
                                           fscr_offset=fscr_offset,
                                           text="Налаштування",
                                           textSize=18,
                                           borderColor=Colors.ButtonBorderDefault,
                                           textColor=Colors.ButtonBorderDefault,
                                           bgAlpha=180)
        self.optionsMenu = None
        self.quitButton = Button.Button(mouse, 
                                        scr, 
                                        topLeft=(17*50, 11*50+25), 
                                        dimensions=(3*50, 50), 
                                        fscr_offset=fscr_offset, 
                                        text="Вийти",
                                        textSize=18,
                                        borderColor=Colors.ButtonBorderDefault,
                                        textColor=Colors.ButtonBorderDefault,
                                        bgAlpha=180)

    def update(self):
        self.tint.update()
        self.menuBackground.update()
        self.title.update()
        self.resumeButton.update(isBlocked=(self.optionsMenu is not None))
        self.optionsButton.update(isBlocked=(self.optionsMenu is not None))
        self.quitButton.update(isBlocked=(self.optionsMenu is not None))
        if self.optionsMenu is not None:
            self.optionsMenu.update()
            if (self.optionsMenu.closeButton.isPressed) or (self.keyboard.esc is True):
                self.optionsMenu = None
        elif self.optionsButton.isPressed:
            self.optionsMenu = OptionsMenu.OptionsMenu(self.scr, self.mouse, self.keyboard, self.fscr_offset, self.maxOffset)