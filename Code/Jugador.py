"""Este modulo almacena todo los atributos y metodos del jugador"""

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Constantes import *

class Juan(Sprite):
    def __init__(self, contenedor):
        self.puntos = 0
        self.vida = 3
        self.angulo = 0
        self.contenedor = contenedor
        self.cont = 0
        self.cont2 = 0
        self.imagen = jugador2[self.cont]
        self.rect = self.imagen.get_rect()
        self.rect.move_ip(60, -130)
        self.rect.x %= self.contenedor[0]
        self.rect.y %= self.contenedor[1]
        self.bola = bola[self.cont2]
        self.rect2 = self.bola.get_rect()
        self.rect2.move_ip(130, -47)
        self.rect2.x %= self.contenedor[0]
        self.rect2.y %= self.contenedor[1]

    def animar(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_RIGHT]:
            self.cont = (self.cont+1)%4
            self.imagen = jugador2[self.cont]
            pygame.time.delay(100)
            if self.rect.x + self.rect.width < 800:
                self.rect.x += 5
        elif teclas[K_LEFT]:
            self.cont = (self.cont+1)%4
            self.imagen = jugador1[self.cont]
            pygame.time.delay(100)
            if self.rect.x > 0:
                self.rect.x -= 5
        else:
            self.cont = (self.cont+1)%4
            self.imagen = jugador2[self.cont]
            pygame.time.delay(200)

    def disparar(self):
        teclas = pygame.key.get_pressed()
        self.cont2 = (self.cont2+1)%4
        self.bola = bola[self.cont2]
        self.rect2.x += 5