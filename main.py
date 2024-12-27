import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    Player.containers =(updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    play = Player(x,y)
    asfield = AsteroidField()
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
        
        for upda in updatable:
            upda.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(play):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                #print("calcoloCollisione")
                if asteroid.collision(shot):
                    print ("distrutto")
                    asteroid.split()
                    shot.kill()

        
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed /1000

if __name__ == "__main__":
    main()
