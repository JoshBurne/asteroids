import pygame
from constants import *
from player import *

def main():
    # Boot Up:
    print("Starting Asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT /2)
    dt = 0


    # game loop
    while True:
        # allow the window to be quit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill the screen with the RGB colour in the brackets
        screen.fill("#151515")

        player.draw(screen)
        player.update(dt)
        # Next frame (ie. next flipbook page)
        pygame.display.flip()
        time_passed = clock_object.tick(60)
        dt = time_passed / 1000
        





if __name__ == "__main__":
    main()

