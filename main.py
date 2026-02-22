import pygame
import sys
from constants import *
from player import Player
from projectile import Projectile
from projectilespawn import ProjectileSpawn

def main():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    gravgroup = pygame.sprite.Group()
    projgroup = pygame.sprite.Group()
    Player.containers = (updateable, drawable, gravgroup)
    Projectile.containers = (updateable, drawable, projgroup)
    ProjectileSpawn.containers = (updateable)

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    spawn_one = ProjectileSpawn(player, PROJ_COLOR_ONE, True)
    spawn_two = ProjectileSpawn(player, PROJ_COLOR_TWO, False)
    proj_two_timer = 0

    print("Starting game!")

    while True:
        if spawn_two.enabled is False:
            proj_two_timer += dt
            if proj_two_timer > PROJ_LIFETIME * 2:
                spawn_two.enabled = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
            
        for gravitem in gravgroup:
            gravitem.applygravity()
        
        for projectile in projgroup:
            if projectile.check_collision(player):
                sys.exit("Game Over!")

        surface.fill((0,0,0))
        for drawing in drawable:
            drawing.draw(surface)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__=="__main__":
    main()