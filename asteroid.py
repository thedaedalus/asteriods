import random

import pygame

from circleshape import CircleShape
from constants import *  # noqa
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # noqa

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)  # type: ignore # noqa

    def update(self, dt):
        self.position += self.velocity * dt  # type: ignore

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:  # type: ignore # noqa
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        new_asteroid1_vector = self.velocity.rotate(rand_angle)
        new_asteroid2_vector = self.velocity.rotate(-rand_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS  # type: ignore # noqa
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)  # type: ignore # noqa
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)  # type: ignore # noqa
        new_asteroid1.velocity = new_asteroid1_vector * 1.2
        new_asteroid2.velocity = new_asteroid2_vector * 1.2
