import pygame

from pygame.locals import *

from arrow import *


from math import sin, cos, pi
pygame.init()

clock = pygame.time.Clock()


DISPLAY = (640,480)


screen = pygame.display.set_mode(DISPLAY)

bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

arrow = Arrow()
sprite = pygame.sprite.RenderPlain(arrow)

arrow.x = (DISPLAY[0] - arrow.rect.width)/2
arrow.y = (DISPLAY[1] - arrow.rect.height)/2

print(arrow.rect.left)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(bg, (0,0))

    sprite.draw(screen)
    sprite.update()


    pygame.display.flip()
    clock.tick(60)