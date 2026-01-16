import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    VERSION = pygame.version.ver
    print(
        f"Starting Asteroids with pygame version: {VERSION}\n"
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}"
    )
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0


if __name__ == "__main__":
    main()
