import pygame
from player import Player

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_KINDS,
)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit frame rate to 60 fps
        dt = clock.tick(60) // 1000


if __name__ == "__main__":
    main()
