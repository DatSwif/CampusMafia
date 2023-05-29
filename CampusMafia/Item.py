import pygame

class Item(object):
    """description of class"""
    def __init__(self, name):
        self.name = name
        #image when in inventory
        self.inv_image = pygame.image.load(f'assets/items/inv_{name}.png').convert_alpha()
        #image when in the level
        self.lv_image = pygame.image.load(f'assets/items/lv_{name}.png').convert_alpha()
        #image when it can be picked up
        self.lit_image = pygame.image.load(f'assets/items/lit_{name}.png').convert_alpha()

