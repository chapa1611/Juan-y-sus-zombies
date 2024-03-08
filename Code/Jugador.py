import pygame
from pygame.locals import *
from pygame.sprite import Sprite
class Juan(Sprite):
    def __init__(self, contenedor):
        self.puntos=0
        self.vida=3
        self.angulo=0
        self.contenedor=contenedor
        self.imag=pygame.image.load("imagenes/juan.png")
        self.imagen=self.imag
        self.rect=self.imagen.get_rect()
        self.rect.move_ip(60, -100)
        self.rect.x %= self.contenedor[0]
        self.rect.y %= self.contenedor[1]