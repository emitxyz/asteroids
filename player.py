import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.is_powered_up = False
        self.powerup_timer = 0.0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Handle powerup timer
        if self.is_powered_up:
            self.powerup_timer -= dt
            if self.powerup_timer <= 0:
                self.is_powered_up = False

    def shoot(self):
        if self.cooldown <= 0:
            if self.is_powered_up:
                shot = Shot(self.position.x, self.position.y, color=SHOT_COLOR_POWERUP, radius=SHOT_RADIUS_POWERUP)
                cooldown = SHOT_COOLDOWN_POWERUP
            else:
                shot = Shot(self.position.x, self.position.y)
                cooldown = PLAYER_SHOOT_COOLDOWN
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.cooldown = cooldown

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def apply_powerup(self):
        self.is_powered_up = True
        self.powerup_timer = POWERUP_DURATION