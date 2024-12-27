import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    play = Player(x,y)
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        play.draw(screen)
        play.update(dt)
        pygame.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed /1000

if __name__ == "__main__":
    main()
