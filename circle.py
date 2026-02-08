import pygame

class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, rad):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.radius = rad
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def applygravity(self):
        pass

    def check_collision(self, other):
        return self.position.distance_to(other.position) < (self.radius + other.radius)