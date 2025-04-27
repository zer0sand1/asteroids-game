import random 
import pygame
from constants import *

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius )
        
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return 
        angle = random.uniform(20, 50)
        v1 =self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        r = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, r)
        a2 = Asteroid(self.position.x, self.position.y, r)
        a1.velocity = v1 *1.2
        a2.velocity = v2 * 1.2
        
        