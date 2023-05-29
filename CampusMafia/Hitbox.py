class Hitbox(object):
    """description of class"""
    def __init__(self, scr, abs_topLeft, fscr_offset, dimensions, sprites):
        self.scr = scr

        self.abs_topLeft = abs_topLeft
        self.fscr_offset = fscr_offset
        self.dimensions = dimensions
        self.sprites = sprites
        
    def intersects(self, other):
        x11 = self.abs_topLeft[0]
        y11 = self.abs_topLeft[1]
        x12 = x11+self.dimensions[0]
        y12 = y11+self.dimensions[1]
        
        x21 = other.abs_topLeft[0]
        y21 = other.abs_topLeft[1]
        x22 = x21 + other.dimensions[0]
        y22 = y21 + other.dimensions[1]

        return (x11 < x22 and y11 < y22 and x12 > x21 and y12 > y21)
