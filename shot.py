import pygame

from circleshape import CircleShape
from constants import *  # noqa


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  # noqa

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)  # type: ignore # noqa

    def update(self, dt):
        self.position += self.velocity * dt  # type: ignore
