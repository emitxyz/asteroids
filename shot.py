import pygame
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, color="white", radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.color = color
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

        # Remove the shot if it goes off-screen
        if (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()