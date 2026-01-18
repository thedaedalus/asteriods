import random

import pygame

from base import CircleShape
from constants import *  # noqa
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius)  # noqa
        self.color = color  # type: ignore # noqa

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,  # type: ignore # noqa
            self.position,
            self.radius,
            LINE_WIDTH,  # type: ignore # noqa
        )

    def update(self, dt):
        self.position += self.velocity * dt  # type: ignore
        self.wrap_around_screen()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:  # type: ignore # noqa
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        new_asteroid1_vector = self.velocity.rotate(rand_angle)
        new_asteroid2_vector = self.velocity.rotate(-rand_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS  # type: ignore # noqa

        if new_asteroid_radius == ASTEROID_MIN_RADIUS * 2:  # type: ignore # noqa
            new_color = "Yellow"

        if new_asteroid_radius == ASTEROID_MIN_RADIUS * 1:  # type: ignore # noqa
            new_color = "green"

        new_asteroid1 = Asteroid(
            self.position.x,  # type: ignore # noqa
            self.position.y,  # type: ignore # noqa
            new_asteroid_radius,
            new_color,  # type: ignore # noqa
        )
        new_asteroid2 = Asteroid(
            self.position.x,  # type: ignore # noqa
            self.position.y,  # type: ignore # noqa
            new_asteroid_radius,
            new_color,  # type: ignore # noqa
        )
        new_asteroid1.velocity = new_asteroid1_vector * 1.2
        new_asteroid2.velocity = new_asteroid2_vector * 1.2
