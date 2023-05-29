import pygame.mouse

class Mouse(object):
    """Tracking clicked and held buttons and position of the mouse"""
    def __init__(self):
        self.x : int
        self.y : int
        self.left = False #shoot, click buttons
        self.right = False #action, pick up

    def update(self):
        """Update state of mouse"""
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]

        if pygame.mouse.get_pressed()[0]:
            if self.left is False:
                self.left = True
            elif self.left:
                self.left = None
        else:
            self.left = False

        if pygame.mouse.get_pressed()[2]:
            if self.right is False:
                self.right = True
            elif self.right:
                self.right = None
        else:
            self.right = False

    def intersects(self, topLeft, dimensions):
        return ((self.x >= topLeft[0]) and 
                (self.x <= topLeft[0] + dimensions[0]) and 
                (self.y >= topLeft[1]) and 
                (self.y <= topLeft[1] + dimensions[1]))