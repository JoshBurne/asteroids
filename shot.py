from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame

class Shot (CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, '#ffffff', self.position , self.radius, 2)
        
