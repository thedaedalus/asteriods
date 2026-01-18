import random

import pygame

from asteroid import Asteroid
from constants import *  # noqa


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),  # noqa
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS,  # noqa
                y * SCREEN_HEIGHT,  # noqa
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),  # noqa
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH,  # noqa
                SCREEN_HEIGHT + ASTEROID_MAX_RADIUS,  # noqa
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)  # type: ignore # noqa
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity, color):
        asteroid = Asteroid(position.x, position.y, radius, color)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS:  # noqa
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)  # noqa
            if kind == 1:
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity, "Green")  # noqa
            if kind == 2:
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity, "yellow")  # noqa
            if kind == 3:
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity, "red")  # noqa
