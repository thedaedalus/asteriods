import pygame

from circleshape import CircleShape
from constants import *  # noqa


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # noqa

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)  # type: ignore # noqa

    def update(self, dt):
        self.position += self.velocity * dt  # type: ignore
