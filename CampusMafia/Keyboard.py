import pygame

class Keyboard(object):
    """Tracking pressed and held buttons on the keyboard"""
    def __init__(self):
        #wasd
        self.up = False     #w or uparrow
        self.left = False   #a or leftarrow
        self.down = False   #s or downarrow
        self.right = False  #d or rightarrow
        
        #item slots
        self.num1 = False 
        self.num2 = False 
        self.num3 = False

        #weapon slots
        self.shift = False

        #picking up and interacting with objects
        self.action = False #e
        
        #F11 for switching to and from fullscreen
        self.F11 = False

        #esc for accessing the ingame menu
        self.esc = False

    def update(self):
        """Update state of keyboard"""
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: ### left
            if self.left is False:
                self.left = True
            elif self.left is True:
                self.left = None
        else:
            self.left = False

        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: ### right
            if self.right is False:
                self.right = True
            elif self.right is True:
                self.right = None
        else:
            self.right = False

        if pressed[pygame.K_UP] or pressed[pygame.K_w]: ### up
            if self.up is False:
                self.up = True
            elif self.up is True:
                self.up = None
        else:
            self.up = False

        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: ### down
            if self.down is False:
                self.down = True
            elif self.down is True:
                self.down = None
        else:
            self.down = False

        if pressed[pygame.K_F11]:       # F11
            if self.F11 is False:
                self.F11 = True
            elif self.F11 is True:
                self.F11 = None
        else:
            self.F11 = False

        if pressed[pygame.K_e]:         # e
            if self.action is False:
                self.action = True
            elif self.action is True:
                self.action = None
        else:
            self.action = False

        if pressed[pygame.K_ESCAPE]:    # esc
            if self.esc == False:
                self.esc = True
            elif self.esc:
                self.esc = None
        else:
            self.esc = False

        if pressed[pygame.K_1] or pressed[pygame.K_KP1]:
            if self.num1 == False:
                self.num1 = True
            elif self.num1:
                self.num1 = None
        else:
            self.num1 = False

        if pressed[pygame.K_2] or pressed[pygame.K_KP2]:
            if self.num2 == False:
                self.num2 = True
            elif self.num2:
                self.num2 = None
        else:
            self.num2 = False
            
        if pressed[pygame.K_3] or pressed[pygame.K_KP3]:
            if self.num3 == False:
                self.num3 = True
            elif self.num3:
                self.num3 = None
        else:
            self.num3 = False

        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            if self.shift == False:
                self.shift = True
            elif self.shift:
                self.shift = None
        else:
            self.shift = False
