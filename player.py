import pygame

from base import CircleShape
from constants import *  # noqa
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # noqa
        self.rotation = 0
        self.shoot_timer = 0

    # in the Player class
    def triangle(self):
        forward = self.forward()
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius  # type: ignore
        b = self.position - forward * self.radius - right  # type: ignore
        c = self.position - forward * self.radius + right  # type: ignore
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), LINE_WIDTH)  # type: ignore # noqa

    def update(self, dt):
        self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # noqa

    def forward(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt  # noqa
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS  # noqa
        shot = Shot(self.position.x, self.position.y)  # type: ignore
        forward = self.forward()
        shot.velocity = forward * PLAYER_SHOOT_SPEED  # noqa
