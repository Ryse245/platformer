import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    gravgroup = pygame.sprite.Group()
    velgroup = pygame.sprite.Group()
    Player.containers = (updateable, drawable, gravgroup, velgroup)

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting game!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

        for velitem in velgroup:
            velitem.applyvelocity(dt)
            
        for gravitem in gravgroup:
            gravitem.applygravity()
        

        surface.fill((0,0,0))
        for drawing in drawable:
            drawing.draw(surface)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__=="__main__":
    main()