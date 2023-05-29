import Hitbox
import TextBox
import Colors

class Pickup(Hitbox.Hitbox):
    """description of class"""
    def __init__(self, scr, abs_topLeft, dimensions, fscr_offset, item):
        super().__init__(scr, abs_topLeft, fscr_offset, dimensions, None) 
        self.isLooted = False
        self.item = item

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

    def get_loot(self):
        item = self.item
        self.isLooted = True
        self.item = None
        return item

    def renderStruct(self, player):
        if self.isLooted is False:
            rel_topLeft = (player.rel_topLeft[0] + self.fscr_offset[0] - player.abs_topLeft[0] + self.abs_topLeft[0],
                           player.rel_topLeft[1] + self.fscr_offset[1] - player.abs_topLeft[1] + self.abs_topLeft[1])
            if self.isReachable(player):
                textObj, textRect = TextBox.TextBox.makeTextObj(self.item.name, (0, 0), (0, 0), self.dimensions, 10, Colors.WHITE)
                textRect.center = (rel_topLeft[0] + self.dimensions[0]//2,
                                   rel_topLeft[1] - 10)
                self.scr.blit(textObj, textRect)
                self.scr.blit(self.item.lit_image, rel_topLeft)
            else:
                self.scr.blit(self.item.lv_image, rel_topLeft)