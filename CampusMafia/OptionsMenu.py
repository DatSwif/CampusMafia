import TextBox
import Button
import Colors

class OptionsMenu(object):
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
        self.closeButton = Button.Button(mouse, 
                                         scr, 
                                         topLeft=(17*50, 11*50+25), 
                                         dimensions=(3*50, 50), 
                                         fscr_offset=fscr_offset, 
                                         text="Назад",
                                         textSize=18,
                                         borderColor=Colors.ButtonBorderDefault,
                                         bgAlpha=180)
        self.title = TextBox.TextBox(scr, 
                                     topLeft=(10*50, 5*50), 
                                     dimensions=(6*50, 50),
                                     fscr_offset=fscr_offset,
                                     text="Налаштування",
                                     bgAlpha=0)
        self.controlsText = [
            TextBox.TextBox(scr,
                            topLeft=(7*50, 6*50),
                            dimensions=(12*50, 50),
                            fscr_offset=fscr_offset,
                            text="Використовуйте WASD або стрілки для руху",
                            textSize=18,
                            bgAlpha=0),
            TextBox.TextBox(scr,
                            topLeft=(7*50, 7*50),
                            dimensions=(12*50, 50),
                            fscr_offset=fscr_offset,
                            text="E або ПКМ для взаємодії з об'єктами",
                            textSize=18,
                            bgAlpha=0),
            TextBox.TextBox(scr,
                            topLeft=(7*50, 8*50),
                            dimensions=(12*50, 50),
                            fscr_offset=fscr_offset,
                            text="ЛКМ, щоб стріляти",
                            textSize=18,
                            bgAlpha=0),
            TextBox.TextBox(scr,
                            topLeft=(7*50, 9*50),
                            dimensions=(12*50, 50),
                            fscr_offset=fscr_offset,
                            text="F11 для повноекранного/віконного режиму",
                            textSize=18,
                            bgAlpha=0),
            TextBox.TextBox(scr,
                            topLeft=(7*50, 10*50),
                            dimensions=(12*50, 50),
                            fscr_offset=fscr_offset,
                            text="ESC щоб поставити гру на паузу",
                            textSize=18,
                            bgAlpha=0)
            ]

    def update(self):
        self.tint.update()
        self.menuBackground.update()
        self.closeButton.update()
        self.title.update()
        for b in self.controlsText:
            b.update()