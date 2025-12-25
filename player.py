import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        pass

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        return self.position
    
    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation = self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotation = self.rotate(-dt)
        
        if keys[pygame.K_w]:
            self.position = self.move(dt)

        if keys[pygame.K_s]:
            self.position = self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
        pass

    def shoot(self):
        if self.cooldown > 0:
            pass
        else:
            shot = Shot(self.position.x, self.position.y, 1)
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot_vector = pygame.Vector2(0,1).rotate(self.rotation)
            shot.velocity = PLAYER_SHOOT_SPEED * shot_vector
        pass
