import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import Powerup
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Powerup.containers = (powerups, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt_total = 0
    spawn_timer = 0.0

    while True:
        dt = clock.tick(60) / 1000  # Delta time in seconds
        dt_total += dt
        spawn_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Spawn Powerups at defined intervals
        if spawn_timer >= POWERUP_SPAWN_RATE:
            spawn_timer = 0.0
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            Powerup(x, y)

        # Update all sprites
        updatable.update(dt)

        # Handle collisions between asteroids and player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            # Handle collisions between asteroids and shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        # Handle collisions between powerups and player
        for powerup in powerups:
            if powerup.collides_with(player):
                powerup.kill()
                player.apply_powerup()

        # Clear the screen
        screen.fill("black")

        # Draw all sprites
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
