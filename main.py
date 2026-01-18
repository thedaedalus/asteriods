import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *  # noqa
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa
    VERSION = pygame.version.ver
    print(
        f"Starting Asteroids with pygame version: {VERSION}\n"
        f"Screen width: {SCREEN_WIDTH}\n"  # noqa
        f"Screen height: {SCREEN_HEIGHT}"  # noqa
    )
    clock = pygame.time.Clock()
    dt = 0
    hit = None
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable  # type: ignore
    Shot.containers = (shots, updatable, drawable)  # type: ignore

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)  # noqa
    asteroidfield = AsteroidField()  # noqa

    while running:
        # poll for events
        log_state()  # logging
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        updatable.update(dt)
        for asteroid in asteroids:
            hit = asteroid.collides_with(player)
            if hit:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                hit = asteroid.collides_with(shot)
                if hit:
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0


if __name__ == "__main__":
    main()
