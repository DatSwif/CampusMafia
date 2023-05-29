import pygame.font
import pygame.draw
import Colors

class TextBox(object):
    """Rectangle with text"""
    def __init__(self, scr, topLeft : tuple, dimensions : tuple, fscr_offset : list, 
                 text = "", textSize = 25, borderColor = None, textColor = Colors.WHITE, bgColor = Colors.BLACK, bgAlpha = 255):
        self.scr = scr
        self.topLeft = topLeft
        self.dimensions = dimensions
        self.fscr_offset = fscr_offset
        self.rect = (topLeft, dimensions)

        #background
        self.bgAlpha = bgAlpha
        self.default_bgAlpha = bgAlpha
        self.bgColor = bgColor
        self.default_bgColor = bgColor
        
        #borders
        if borderColor is not None:
            self.borderColor = borderColor
            self.default_borderColor = borderColor

        else:
            self.borderColor = None
            self.default_borderColor = None

        #text
        self.text = text
        self.textSize = textSize
        self.default_textSize = textSize
        self.textColor = textColor
        self.default_textColor = textColor

    def update(self, text=None, textSize = None, borderColor = None, textColor = None, bgColor = None, bgAlpha = None):
        """redraw the text box, rerender if necessary"""
        
        self.rect = ((self.topLeft[0]+self.fscr_offset[0], self.topLeft[1]+self.fscr_offset[1]), self.dimensions)

        #background
        if bgAlpha is not None:
            self.bgAlpha = bgAlpha
        elif self.bgAlpha != self.default_bgAlpha:
            self.bgAlpha = self.default_bgAlpha

        if bgColor is not None:
            self.bgColor = bgColor
        elif self.bgColor != self.default_bgColor:
            self.bgColor = self.default_bgColor
            
        self.bgSurface = pygame.Surface(self.dimensions)
        self.bgSurface.set_alpha(self.bgAlpha)
        self.bgSurface.fill(self.bgColor)
        self.scr.blit(self.bgSurface, self.rect)

        #borders
        if borderColor is not None:
            self.borderColor = borderColor
            pygame.draw.rect(self.scr, self.borderColor, self.rect, width=2)
        elif self.borderColor != self.default_borderColor:
            self.borderColor = self.default_borderColor
            if self.default_borderColor is not None:
                self.borderColor = self.default_borderColor
                pygame.draw.rect(self.scr, self.borderColor, self.rect, width=2)

        #text
        if text is not None:
            self.text = text
        
        if textSize is not None:
            self.textSize = textSize
        elif self.textSize != self.default_textSize:
            self.textSize = self.default_textSize
        
        if textColor is not None:
            self.textColor = textColor
        elif self.textColor != self.default_textColor:
            self.textColor = self.default_textColor

        self.textObj, self.textRect = self.makeTextObj(self.text, self.topLeft, self.fscr_offset, self.dimensions, self.textSize, self.textColor)
        self.scr.blit(self.textObj, self.textRect) 

    @staticmethod
    def makeTextObj(text, topLeft, fscr_offset, dimensions, size, color):
        """Make a text image and a rect object for it"""
        font = pygame.font.Font('assets/fonts/StalinistOne-Regular.ttf', size)
        textObj = font.render(text, True, color)
        textRect = textObj.get_rect()
        textRect.center = (topLeft[0]+fscr_offset[0]+dimensions[0]//2,
                           topLeft[1]+fscr_offset[1]+dimensions[1]//2)
        return textObj, textRect