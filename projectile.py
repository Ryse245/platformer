import pygame
import math
from circle import Circle
from constants import *

class Projectile(Circle):
    def __init__(self, x, y, target, color):
        super().__init__(x, y, PROJ_RAD)
        direction = target - self.position
        unit = direction / (math.sqrt((direction.x * direction.x) + (direction.y * direction.y)))
        self.velocity = unit * PROJ_SPEED
        self.lifetime = 0
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.lifetime += dt
        if self.lifetime > PROJ_LIFETIME:
            del self