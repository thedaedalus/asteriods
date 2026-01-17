import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *  # noqa
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))  # noqa
    VERSION = pygame.version.ver
    print(
        f"Starting Asteroids with pygame version: {VERSION}\n"
        f"Screen width: {SCREEN_WIDTH}\n"  # noqa
        f"Screen height: {SCREEN_HEIGHT}"  # noqa
    )
    clock = pygame.time.Clock()
    dt = 0
    hit = None

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable  # type: ignore

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)  # noqa
    asteroidfield = AsteroidField()  # noqa

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass

        screen.fill("black")

        updatable.update(dt)
        for asteroid in asteroids:
            hit = asteroid.collides_with(player)
            if hit:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0


if __name__ == "__main__":
    main()
