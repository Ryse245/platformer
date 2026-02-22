import pygame
import random
from projectile import Projectile
from player import Player
from constants import *


#spawn projectile random x pos between 0 and SCREEN_WIDTH with a ref to the player to get their current position
class ProjectileSpawn(pygame.sprite.Sprite):
    
    def __init__(self, player: Player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player_ref = player
        self.spawn_timer = 0.0

    def spawn(self):
        x_pos = random.randint(0, SCREEN_WIDTH)
        proj = Projectile(x_pos, -PROJ_RAD, self.player_ref.position)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > PROJ_SPAWN_RATE:
            self.spawn_timer = 0
            self.spawn()