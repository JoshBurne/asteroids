import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import Shot

def main():
    # Boot Up:
    print("Starting Asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # SET SCREEN SIZE
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # GROUP OBJECTS
    clock_object = pygame.time.Clock()
    updatable_grp = pygame.sprite.Group()
    drawable_grp = pygame.sprite.Group()
    asteroids_grp = pygame.sprite.Group()   
    shots_grp = pygame.sprite.Group()
    
    # CONTAINERS
    AsteroidField.containers = (updatable_grp)
    Asteroid.containers = (asteroids_grp, updatable_grp, drawable_grp)
    Player.containers = (updatable_grp, drawable_grp)
    Shot.containers = (shots_grp, updatable_grp, drawable_grp)

    # INITIALISE OBJECTS
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT /2, PLAYER_SHOOT_COOLDOWN)
    asteroid_field = AsteroidField()
    
    dt = 0


    # game loop
    while True:
        # allow the window to be quit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill the screen with the RGB colour in the brackets
        screen.fill("#151515")

        for drawable in drawable_grp:
            drawable.draw(screen)
        
        updatable_grp.update(dt)
        
        # Next frame (ie. next flipbook page)
        pygame.display.flip()
        time_passed = clock_object.tick(60)
        dt = time_passed / 1000


        for asteroid in asteroids_grp:
            if CircleShape.collision_check(player, asteroid) == True:
                print("Game Over")
                sys.exit()
            
            for shot in shots_grp:
                if CircleShape.collision_check(shot, asteroid) == True:
                    asteroid.split()
                    shot.kill()
        





if __name__ == "__main__":
    main()

