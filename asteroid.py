import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        pass

    def split(self):
        old_velocity = self.velocity
        old_radius = self.radius
        old_x = self.position.x
        old_y = self.position.y
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            first_velocity = old_velocity.rotate(angle)
            second_velocity = old_velocity.rotate(-angle)
            radius = old_radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(old_x, old_y, radius)
            first_asteroid.velocity = first_velocity * 1.2
            second_asteroid = Asteroid(old_x, old_y, radius)
            second_asteroid.velocity = second_velocity * 1.2
            

