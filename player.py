from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, shot_timer):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = shot_timer
        



    def draw(self, screen):
        pygame.draw.polygon(screen, '#ffffff', self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)
            


        
    


# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        print(f"timer = {self.shot_timer}")

        if self.shot_timer < 0:
            self.shot_timer = 0
        elif self.shot_timer > 0:
            self.shot_timer -= dt

        print(self.shot_timer)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_timer == 0:
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            self.shoot(dt)
        