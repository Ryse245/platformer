import pygame
from circle import Circle
from constants import *

class Player(Circle):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RAD)
        self.canjump = False

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            #move left
            self.move(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            #move right
            self.move(dt)
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            #jump
            self.jump()

    def move(self, dt):
        forward = pygame.Vector2(1, 0)
        self.position += forward * PLAYER_SPEED * dt

    def jump(self):
        if self.canjump is True:
            up = pygame.Vector2(0, -1)
            self.velocity += up * PLAYER_JUMP
            self.canjump = False
            print("Jump")       

    def applygravity(self):
        if (self.position.y + self.radius) < SCREEN_HEIGHT - RADIUS_OFFSET:
            down = pygame.Vector2(0, 1)
            self.velocity += down * GRAVITY
        else:
            if self.canjump is False:
                self.velocity = pygame.Vector2(0, 0)
            self.canjump = True

    def applyvelocity(self, dt):
        self.position += self.velocity * dt