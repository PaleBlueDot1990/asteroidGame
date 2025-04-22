from circleshape import CircleShape
import pygame
import constants
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        newradius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0], self.position[1], newradius)
        asteroid1.velocity = self.velocity.rotate(angle) * constants.SPLIT_VELOCITY_FACTOR

        asteroid2 = Asteroid(self.position[0], self.position[1], newradius)
        asteroid2.velocity = self.velocity.rotate(-1*angle) * constants.SPLIT_VELOCITY_FACTOR


        
    
    
