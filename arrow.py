import pygame

from utils import *
from math import atan2, sqrt, degrees

class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("arrow.png", -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.x = 0
        self.y = 0
        self.oldVector = (self.rect.left - self.rect.center[0], self.rect.left - self.rect.center[1])
        self.newVector = (self.rect.left - self.rect.center[0], self.rect.left - self.rect.center[1])
        self.original = self.image

    def update(self):
        self.rect.left, self.rect.top = self.x, self.y
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        self.newVector = (mousePos[0] - self.rect.center[0], mousePos[1] - self.rect.center[1])


        scalar = self.oldVector[0] * self.newVector[0] + self.oldVector[1] * self.newVector[1];
        cross = self.oldVector[0] * self.newVector[1] - self.oldVector[1] * self.newVector[0];
        vectorAngle = atan2(cross, scalar)
        
        self.image = pygame.transform.rotate(self.original, -degrees(vectorAngle)).convert()
        self.rect = self.image.get_rect(center = (self.x, self.y))
        # self.oldVector = self.newVector




# √(xa2 + ya2) * √(xb2 + yb2)