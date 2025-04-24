import pygame
from circleshape import CircleShape
from constants import *
from player import Player


def main():
    pygame.init()
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    
    
    Player.containers = (updatable, drawable)
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    dt = 2
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for thing in drawable:
            thing.draw(screen)
        
        
        
        pygame.display.flip()
       
        #limit the framerate to 60s
        dt = clock.tick(60)/1000
    
    
    
    
if __name__ == "__main__":
    main()
