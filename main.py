import sys
import pygame
from circleshape import CircleShape
from constants import *
from player import Player, Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroid_field = AsteroidField()
    
    Player.containers = ( updatable, drawable)
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    
    
    dt = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_collision(p1):
                print("Game Over!")
                sys.exit()
                
                
        screen.fill("black")
        
            
        
        for thing in drawable:
            thing.draw(screen)
        
        
        
        pygame.display.flip()
       
        #limit the framerate to 60s
        dt = clock.tick(60)/1000
    
    
    
    
if __name__ == "__main__":
    main()
