import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable  # type: ignore

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_with(player):
                print("Game Over")
                pygame.quit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit frame rate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
