import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        #allow the window to be quit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill the screen with the RGB colour in the brackets
        screen.fill("#151515")

        #Next frame (ie. next flipbook page)
        pygame.display.flip()




if __name__ == "__main__":
    main()

