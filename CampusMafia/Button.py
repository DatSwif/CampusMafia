import TextBox
import Colors

class Button(TextBox.TextBox):
    """Clickable button"""
    def __init__(self, mouse, scr, topLeft : tuple, dimensions : tuple, fscr_offset : list, 
                 text = "", textSize = 25, borderColor = None, textColor = Colors.WHITE, bgColor = Colors.BLACK, bgAlpha = 255):
        super().__init__(scr, topLeft, dimensions, fscr_offset, text, textSize, borderColor, textColor, bgColor, bgAlpha)
        self.isPressed = False
        self.isHovered = False
        self.mouse = mouse

    def update(self, isBlocked = False):
        self.isPressed = False
        self.isHovered = False
        if (not isBlocked) and (self.mouse.intersects((self.topLeft[0]+self.fscr_offset[0], self.topLeft[1]+self.fscr_offset[1]), self.dimensions)):
            if self.mouse.left is True:
                self.isPressed = True
                self.isHovered = True
            else:
                self.isHovered = True
        if self.isPressed:
            super().update(textSize=round(self.default_textSize*1.2), 
                           borderColor=Colors.ButtonBorderPressed, 
                           textColor=Colors.ButtonBorderPressed, 
                           bgColor=Colors.ButtonBackgroundPressed,
                           bgAlpha=0.7*255//1)
        elif self.isHovered:
            super().update(textSize=round(self.default_textSize*1.1),
                           borderColor=Colors.ButtonBorderHovered,
                           textColor=Colors.ButtonBorderHovered,
                           bgColor=Colors.ButtonBackgroundHovered,
                           bgAlpha=0.6*255//1)
        else:
            super().update()