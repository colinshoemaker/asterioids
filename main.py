import pygame
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot

def main():
    pygame.init()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updateable,)
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable,drawable, shots)

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    field = AsteroidField()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateable.update(dt)
        for ob in asteroids:
            for bt in shots:
                if ob.collide(bt): 
                    ob.kill()
                    bt.kill()
        for ob in asteroids:
            if ob.collide(player):
                return print("Game over!")
        for ea in drawable:
            ea.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000
    
    
if __name__ == "__main__":
    main()