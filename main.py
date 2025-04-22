import pygame 
import constants
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
 
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.detectcollission(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.detectcollission(asteroid):
                    shot.kill()
                    asteroid.split()
            
        screen.fill('black')

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()

