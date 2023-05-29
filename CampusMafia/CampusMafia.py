import pygame
from screeninfo import get_monitors

import Mouse
import Keyboard
import ScrSwitcher

def main():
    """Initialization and main cycle"""
    
    #init modules
    pygame.init()
    pygame.font.init()
    
    #screen setup
    windowedWidth = 1300
    windowedHeight = 750
    windowedDimensions = (windowedWidth, windowedHeight)

    monitor = get_monitors()[0]
    fullscreenWidth = monitor.width
    fullscreenHeight = monitor.height
    fullscreenDimensions = (fullscreenWidth, fullscreenHeight)
    windowed = True
    scr = pygame.display.set_mode(windowedDimensions)

    pygame.display.set_caption("Мафія на кампусі")
    clock = pygame.time.Clock()
    FPS = 60

    #initializing game components
    mouse = Mouse.Mouse()
    keyboard = Keyboard.Keyboard()
    scrSwitcher = ScrSwitcher.ScrSwitcher(scr, mouse, keyboard, windowedDimensions, fullscreenDimensions)

    run = True
    while run:
        #updating inputs
        keyboard.update()
        mouse.update()
        
        #updating 
        scrSwitcher.update()
        pygame.display.update()
        clock.tick(FPS)

        #checking for quit
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                run = False

if __name__ == "__main__":
    main()