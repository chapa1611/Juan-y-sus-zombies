"""Este modulo almacena todo los atributos y metodos del jugador"""
import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Constantes import *


class Juan(Sprite):
    def __init__(self, contenedor):
        self.puntos=0
        self.vida=3
        self.angulo=0
        self.contenedor=contenedor
        self.imagen=jugador[1][1]
        self.rect=self.imagen.get_rect()
        self.rect.move_ip(60, -130)
        self.rect.x %= self.contenedor[0]
        self.rect.y %= self.contenedor[1]
        self.sentido = 1
        self.juan = 2

    def animar(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_RIGHT]:
            self.sentido = 1
        elif teclas[K_LEFT]:
            self.sentido = 0

