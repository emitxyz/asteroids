import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, POWERUP_RADIUS, POWERUP_COLOR, POWERUP_SPEED
from circleshape import CircleShape

class Powerup(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)
        self.color = POWERUP_COLOR
        # Random direction
        angle = random.uniform(0, 360)
        self.velocity = pygame.Vector2(1, 0).rotate(angle) * POWERUP_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

        # Wrap around the screen edges
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius