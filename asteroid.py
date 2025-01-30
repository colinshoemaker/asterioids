from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        ang = random.uniform(20,50)
        nvel = self.velocity.rotate(ang)
        n2vel = self.velocity.rotate(-ang)
        nrad = self.radius - ASTEROID_MIN_RADIUS
        n1 = Asteroid(self.position[0],self.position[1],nrad)
        n2 = Asteroid(self.position[0], self.position[1],nrad)
        n1.velocity = nvel*1.2
        n2.velocity = n2vel*1.2